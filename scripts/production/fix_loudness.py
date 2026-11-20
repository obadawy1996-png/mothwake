"""Two-pass loudness fix for a master (picture is stream-copied, never re-encoded).

  .venv\\Scripts\\python.exe scripts/production/fix_loudness.py <in.mp4> <out.mp4> [--I -14] [--TP -2]

Pass 1 measures with loudnorm (print_format=json); pass 2 applies linear normalisation with the
measured values, then an oversampled limiter (Omar Studio lesson: limit before AAC to stop overshoot).
Refuses to overwrite <out.mp4>.
"""
import json, re, shutil, subprocess, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--I", type=float, default=-14.0); ap.add_argument("--TP", type=float, default=-2.0)
a = ap.parse_args()
ff = shutil.which("ffmpeg")
r = subprocess.run([ff, "-hide_banner", "-nostats", "-i", a.inp, "-vn", "-af",
                    f"loudnorm=I={a.I}:TP={a.TP}:LRA=11:print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S)[-1])
lim = 10 ** ((a.TP - 1.0) / 20)  # limiter ceiling 1 dB under the target true peak
af = (f"loudnorm=I={a.I}:TP={a.TP}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
      f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,"
      f"aresample=192000,alimiter=limit={lim:.3f}:level=false,aresample=48000")
r2 = subprocess.run([ff, "-hide_banner", "-v", "error", "-n", "-i", a.inp, "-c:v", "copy", "-af", af,
                     "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.out], capture_output=True, text=True)
if r2.returncode:
    print(r2.stderr[-2000:]); sys.exit(1)
print(json.dumps({"in": a.inp, "out": a.out, "measured_I": m["input_i"], "measured_TP": m["input_tp"]}))
