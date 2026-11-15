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
        chars = [len(x) for x in lines]; cum = 0; cuts = []
        for c in chars[:-1]:
            cum += c; target = total * cum / sum(chars)
            s0, e0 = min((g for g in gaps if not cuts or (g[0] + g[1]) / 2 > cuts[-1]), key=lambda g: abs((g[0] + g[1]) / 2 - target))
            cuts.append((s0 + e0) / 2)
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
