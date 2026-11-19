#!/usr/bin/env python3
"""Synthesise the MOTHWAKE sound identity from scratch (no samples → no licence risk).

Outputs (48 kHz, 24-bit WAV, loudness-normalised with ffmpeg loudnorm):
  brand/sound/mothwake_signature.wav  ~1.6 s  wing-flutter + low "wake" swell + faint lamp ping
  brand/sound/mothwake_open_sub.wav   ~0.9 s  optional sub-bass breath under the first shot
  brand/sound/mothwake_outro.wav      ~3.2 s  flutter flies off, ping, low tone settles
"""
from __future__ import annotations

import subprocess
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "brand" / "sound"
SR = 48000
rng = np.random.default_rng(1913)


def env(n, a, r):
    e = np.ones(n)
    ai, ri = int(a * SR), int(r * SR)
    e[:ai] = np.linspace(0, 1, ai) ** 2
    e[-ri:] *= np.linspace(1, 0, ri) ** 1.5
    return e


def lowpass(x, cutoff):
    # one-pole lowpass, run twice
    a = np.exp(-2 * np.pi * cutoff / SR)
    for _ in range(2):
        y = np.empty_like(x)
        acc = 0.0
        for i, v in enumerate(x):
            acc = (1 - a) * v + a * acc
            y[i] = acc
        x = y
    return x


def flutter(dur, rate=19.0, pan_drift=0.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    band = lowpass(noise, 2400) - lowpass(noise, 300)
    beat = (0.5 + 0.5 * np.sin(2 * np.pi * rate * t + np.sin(2 * np.pi * 1.3 * t))) ** 3
    sig = band * beat * env(n, 0.05, dur * 0.6)
    L = sig * (0.5 - pan_drift * t / dur * 0.5 + 0.5) / 1.0
    R = sig * (0.5 + pan_drift * t / dur * 0.5 + 0.5) / 1.0
    return np.stack([L, R], 1) * 0.6


def tone(dur, f0, a=0.4, r=1.0, fifth=True):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f0 * t) + 0.35 * np.sin(2 * np.pi * f0 * 2 * t + 0.3)
    if fifth:
        s += 0.45 * np.sin(2 * np.pi * f0 * 1.5 * t)
    s *= env(n, a, r)
    return np.stack([s, s], 1) * 0.35


def ping(dur, f=1318.5, delay=0.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2.76 * t)) * np.exp(-t * 3.2)
    s = np.concatenate([np.zeros(int(delay * SR)), s])[:n]
    return np.stack([s * 0.8, s], 1) * 0.12


def mix(*parts, dur):
    n = int(dur * SR)
    out = np.zeros((n, 2))
    for p, at in parts:
        i = int(at * SR)
        m = min(n - i, len(p))
        out[i:i + m] += p[:m]
    return out / max(1e-9, np.abs(out).max()) * 0.9


def write(path: Path, x: np.ndarray, lufs: float):
    raw = path.with_suffix(".raw.wav")
    pcm = (x * 32767).astype("<i2")
    with wave.open(str(raw), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-af",
                    f"loudnorm=I={lufs}:TP=-2:LRA=11", "-ar", str(SR), "-c:a", "pcm_s24le", str(path)], check=True)
    raw.unlink()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sig = mix((flutter(0.9, 21, 0.4), 0.0), (tone(1.5, 55.0, 0.35, 0.9), 0.15), (ping(1.4), 0.35), dur=1.65)
    write(OUT / "mothwake_signature.wav", sig, -18)
    sub = mix((tone(0.9, 41.2, 0.25, 0.5, fifth=False), 0.0), dur=0.9)
    write(OUT / "mothwake_open_sub.wav", sub, -24)
    out = mix((flutter(1.6, 17, 1.0), 0.0), (ping(2.2, 1174.7), 0.9), (tone(2.8, 49.0, 0.6, 1.6), 0.4), dur=3.2)
    write(OUT / "mothwake_outro.wav", out, -18)
    print("wrote", *sorted(p.name for p in OUT.glob("*.wav")))


if __name__ == "__main__":
    main()
