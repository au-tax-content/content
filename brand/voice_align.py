"""Split one narration file into its script lines using speech recognition (checks each cut lands on the right word).

Needs: pip install sherpa-onnx, and the Whisper tiny.en model unpacked under /root/asr
(github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-tiny.en.tar.bz2).

    from voice_align import split_lines
    parts = split_lines("batch.wav", lines)     # -> list of (start, end) seconds, one per line
"""
import glob, re, subprocess
import numpy as np

_rec = None


def _recognizer():
    global _rec
    if _rec is None:
        import sherpa_onnx
        d = glob.glob("/root/asr/*/tiny.en-encoder.int8.onnx")[0].rsplit("/", 1)[0] + "/"
        _rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d + "tiny.en-encoder.int8.onnx", decoder=d + "tiny.en-decoder.int8.onnx",
                                                          tokens=d + "tiny.en-tokens.txt", language="en", task="transcribe")
    return _rec


def load(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def heard(samples):
    r = _recognizer(); s = r.create_stream(); s.accept_waveform(16000, samples); r.decode_stream(s); return s.result.text.strip()


def words(t):
    return [w for w in re.sub(r"[^a-z ]", " ", t.lower().replace("-", " ")).split()]


def pauses(path, db=-35, min_d=0.15):
    r = subprocess.run(["ffmpeg", "-i", path, "-af", f"silencedetect=n={db}dB:d={min_d}", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(l.split("silence_start: ")[1]) for l in r.splitlines() if "silence_start" in l]
    en = [float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
    return [((a + b) / 2) for a, b in zip(st, en)]


def split_lines(path, lines, log=print):
    audio = load(path); total = len(audio) / 16000
    cands = pauses(path)
    rate = total / sum(len(l) for l in lines)
    start, spans = 0.0, []
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            spans.append((start, total)); break
        want = words(line); last = want[-1][:4]
        exp = len(line) * rate
        chosen = None
        for c in cands:
            if c <= start + 0.45 * exp:
                continue
            if c > start + 2.2 * exp:
                break
            got = words(heard(audio[int(start * 16000):int(c * 16000)]))
            if got and got[-1][:4] == last and len(got) >= 0.6 * len(want):
                chosen = c; break
        if chosen is None:          # fall back to the pause nearest the expected length
            chosen = min((c for c in cands if c > start), key=lambda c: abs(c - start - exp))
            log(f"  no word match for line {i}: '{line[:40]}' -> fallback {chosen:.2f}s")
        spans.append((start, chosen)); start = chosen
    return spans
