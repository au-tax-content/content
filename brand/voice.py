"""Voiceover for Reels (anonymous: a synthetic voice, never Daniel's).

    from voice import synth_lines, fit_scenes, mux
    lines = ["Hook line.", "Point one ...", ...]          # one line per scene
    wavs, durs = synth_lines(lines, out_dir)              # free Kokoro voice (needs /root/tts model files)
    scenes = fit_scenes(scenes, durs)                     # stretch each scene to its line (+ pad)
    render_motion(scenes, __file__, ...)                  # writes reel.mp4 (silent track)
    mux(folder + "/reel.mp4", wavs, durs_of_scenes)       # lays the voice over the video

Kokoro model files (Apache-2.0): kokoro-v1.0.int8.onnx + voices-v1.0.bin from
github.com/thewh1teagle/kokoro-onnx releases, in /root/tts (or KOKORO_DIR).
At publish, post.json "voiceover": true keeps the video's sound and lays music quietly under it.
"""
import os, subprocess, json

KDIR = os.environ.get("KOKORO_DIR", "/root/tts")
PAD = 0.35


def synth_lines(lines, out_dir, voice="af_heart", speed=1.08):
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(KDIR, "kokoro-v1.0.int8.onnx"), os.path.join(KDIR, "voices-v1.0.bin"))
    os.makedirs(out_dir, exist_ok=True)
    wavs, durs = [], []
    for i, line in enumerate(lines):
        samples, sr = k.create(line, voice=voice, speed=speed, lang="en-us")
        p = os.path.join(out_dir, f"vo{i}.wav"); sf.write(p, samples, sr)
        wavs.append(p); durs.append(len(samples) / sr)
    return wavs, durs


def split_by_silence(audio, n, out_dir, lines=None):
    """Split one narration file into n parts at pauses. With lines given, each cut goes to the pause nearest
    where that line should end (by share of characters); otherwise the n-1 longest pauses are used."""
    r = subprocess.run(["ffmpeg", "-i", audio, "-af", "silencedetect=n=-35dB:d=0.18", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    starts = [float(l.split("silence_start: ")[1]) for l in r.splitlines() if "silence_start" in l]
    ends = [float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
    gaps = list(zip(starts, ends))
    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio],
                                 capture_output=True, text=True).stdout)
    if lines:
        # Pick n-1 pauses in order: close to where each line should end (share of spoken length), favouring long
        # pauses (sentence ends). Solved exactly with a small dynamic programme.
        w = [len(x) for x in lines]; tw = sum(w); acc = 0; targets = []
        for c in w[:-1]:
            acc += c; targets.append(total * acc / tw)
        # Score each segment's LENGTH against its expected length (no drift), minus a bonus for long pauses.
        rate = total / tw
        pos = [(0.0, 0.0)] + [((a + b) / 2, b - a) for a, b in gaps] + [(total, 0.0)]
        G, n_seg = len(pos), len(w)
        INF = float("inf")
        D = [[INF] * G for _ in range(n_seg + 1)]; B = [[-1] * G for _ in range(n_seg + 1)]
        D[0][0] = 0.0
        for k in range(1, n_seg + 1):
            exp_len = w[k - 1] * rate
            for j in range(1, G):
                if (k < n_seg and j == G - 1) or (k == n_seg and j != G - 1):
                    continue
                bonus = 0.0 if j == G - 1 else 6.0 * pos[j][1]
                for i in range(j):
                    if D[k - 1][i] == INF:
                        continue
                    v = D[k - 1][i] + (pos[j][0] - pos[i][0] - exp_len) ** 2 - bonus
                    if v < D[k][j]:
                        D[k][j], B[k][j] = v, i
        j, cut_idx = G - 1, []
        for k in range(n_seg, 0, -1):
            j = B[k][j]; cut_idx.append(j)
        cuts = [pos[j][0] for j in reversed(cut_idx) if j > 0]
    else:
        cuts = sorted((a + b) / 2 for a, b in sorted(gaps, key=lambda g: g[0] - g[1])[: n - 1])
    bounds = [0.0] + cuts + [total]
    os.makedirs(out_dir, exist_ok=True)
    wavs, durs = [], []
    for i in range(n):
        p = os.path.join(out_dir, f"vo{i}.wav")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", audio, "-ss", f"{bounds[i]:.3f}", "-to", f"{bounds[i+1]:.3f}",
                        "-af", "silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse",
                        "-ar", "48000", "-ac", "1", p], check=True)
        d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                 capture_output=True, text=True).stdout)
        wavs.append(p); durs.append(d)
    return wavs, durs


def fit_scenes(scenes, durs, pad=PAD, lead=0.15):
    return [(html, round(max(d, v + pad + lead), 2)) for (html, d), v in zip(scenes, durs)]


def mux(video, wavs, scene_durs, lead=0.15):
    """Place line i at the start of scene i (+lead) and replace the video's silent track with the narration."""
    tmp = video + ".vo.m4a"
    inputs, filt, t = [], [], 0.0
    for i, (w, d) in enumerate(zip(wavs, scene_durs)):
        inputs += ["-i", w]
        filt.append(f"[{i}:a]aresample=48000,adelay={int((t + lead) * 1000)}:all=1[a{i}]")
        t += d
    filt.append("".join(f"[a{i}]" for i in range(len(wavs))) + f"amix=inputs={len(wavs)}:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11,apad,atrim=0:{t:.3f}[out]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[out]",
                    "-ac", "2", "-c:a", "aac", "-b:a", "160k", tmp], check=True)
    out = video + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", tmp, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "copy", "-shortest", "-movflags", "+faststart", out], check=True)
    os.replace(out, video); os.remove(tmp)


def _dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)


def voiced_render(scenes, make_file, cover_scene=0, cover_y=285):
    """Render a Reel whose narration lives in <post>/vo/vo0.m4a, vo1.m4a, ... (one file per scene)."""
    from motion import render_motion
    folder = os.path.dirname(os.path.abspath(make_file))
    wavs = [os.path.join(folder, "vo", f"vo{i}.m4a") for i in range(len(scenes))]
    missing = [w for w in wavs if not os.path.exists(w)]
    if missing:
        raise FileNotFoundError(f"narration missing: {missing}")
    scenes = fit_scenes(scenes, [_dur(w) for w in wavs])
    render_motion(scenes, make_file, cover_scene=cover_scene, cover_y=cover_y)
    mux(os.path.join(folder, "reel.mp4"), wavs, [d for _, d in scenes])
