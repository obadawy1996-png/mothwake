"""MOTHWAKE clip QC (Windows-friendly, Phase 2).

Usage:  .venv\\Scripts\\python.exe scripts/production/qc_clip_check.py <video> [--whisper tiny|base|none]

Checks (report only, never edits media):
  - stream facts (ffprobe): resolution, aspect, fps, duration, audio present
  - scene cuts at two thresholds (PySceneDetect ContentDetector 27 and a low 8) -> hidden-cut candidates
  - black frames (ffmpeg blackdetect) and frozen frames (ffmpeg freezedetect)
  - audio peak / integrated loudness (ffmpeg ebur128)
  - optional speech timing (faster-whisper) for caption sync
Verdict: PASS / PASS WITH WARNINGS / NEEDS REVISION / FAILED  (automated only; a human frame review is still required)
"""
import argparse, json, re, shutil, subprocess, sys
from pathlib import Path


def ff(name):
    p = shutil.which(name)
    if not p:
        sys.exit(f"{name} not found on PATH")
    return p


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path):
    r = run([ff("ffprobe"), "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)])
    j = json.loads(r.stdout or "{}")
    v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), {})
    a = next((s for s in j.get("streams", []) if s.get("codec_type") == "audio"), None)
    num, den = (v.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
    return {
        "width": v.get("width"), "height": v.get("height"),
        "fps": round(float(num) / float(den or 1), 3) if float(den or 1) else None,
        "duration_s": round(float(j.get("format", {}).get("duration", 0)), 3),
        "has_audio": a is not None,
    }


def ffmpeg_filter_log(path, vf=None, af=None):
    cmd = [ff("ffmpeg"), "-hide_banner", "-nostats", "-i", str(path)]
    if vf:
        cmd += ["-vf", vf]
    if af:
        cmd += ["-af", af]
    if not vf:
        cmd += ["-vn"]
    if not af:
        cmd += ["-an"]
    cmd += ["-f", "null", "-"]
    return run(cmd).stderr


def scenes(path, threshold):
    from scenedetect import detect, ContentDetector
    return [round(s[0].seconds, 3) for s in detect(str(path), ContentDetector(threshold=threshold))][1:]


def whisper_words(path, model):
    from faster_whisper import WhisperModel
    import numpy as np
    # Decode with our FFmpeg (avoids PyAV version mismatches on Windows): 16 kHz mono float32.
    raw = subprocess.run([ff("ffmpeg"), "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000",
                          "-f", "f32le", "-"], capture_output=True).stdout
    audio = np.frombuffer(raw, dtype=np.float32)
    m = WhisperModel(model, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(audio, vad_filter=True)
    return [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--whisper", default="none")
    ap.add_argument("--expect", default="1080x1920", help="expected WxH, e.g. 720x1280 for Flow 720p 9:16")
    a = ap.parse_args()
    p = Path(a.video)
    rep = {"file": str(p), "probe": probe(p), "warnings": [], "errors": []}
    pr = rep["probe"]

    w, h = (int(x) for x in a.expect.split("x"))
    if (pr["width"], pr["height"]) != (w, h):
        rep["warnings"].append(f"resolution {pr['width']}x{pr['height']} != expected {a.expect}")
    if pr["width"] and pr["height"] and abs(pr["width"] / pr["height"] - 9 / 16) > 0.01:
        rep["errors"].append("aspect is not 9:16")

    rep["cuts_main"] = scenes(p, 27.0)
    low = scenes(p, 8.0)
    rep["hidden_cut_candidates"] = [t for t in low if all(abs(t - c) > 0.3 for c in rep["cuts_main"])]
    if rep["hidden_cut_candidates"]:
        rep["warnings"].append(f"{len(rep['hidden_cut_candidates'])} low-threshold cut(s): check props/costume on both sides")

    blk = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", ffmpeg_filter_log(p, vf="blackdetect=d=0.25:pix_th=0.08"))
    rep["black_segments"] = [(float(s), float(e)) for s, e in blk]
    frz = re.findall(r"freeze_start: ([\d.]+)", ffmpeg_filter_log(p, vf="freezedetect=n=0.003:d=1.0"))
    rep["frozen_starts"] = [float(x) for x in frz]
    if rep["black_segments"]:
        rep["warnings"].append(f"black frames at {rep['black_segments']}")
    if rep["frozen_starts"]:
        rep["warnings"].append(f"frozen >=1s at {rep['frozen_starts']}")

    if pr["has_audio"]:
        log = ffmpeg_filter_log(p, af="ebur128=peak=true")
        i = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
        tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", log)
        rep["loudness_lufs"] = float(i[-1]) if i else None
        rep["true_peak_dbfs"] = float(tp[-1]) if tp else None
        if rep["true_peak_dbfs"] is not None and rep["true_peak_dbfs"] > -1.0:
            rep["errors"].append(f"true peak {rep['true_peak_dbfs']} dBFS (> -1, clipping risk)")
    else:
        rep["warnings"].append("no audio stream (fine for a raw Flow clip, not for a master)")

    if a.whisper != "none" and pr["has_audio"]:
        rep["speech"] = whisper_words(p, a.whisper)

    rep["verdict"] = "FAILED" if rep["errors"] and not pr["duration_s"] else (
        "NEEDS REVISION" if rep["errors"] else ("PASS WITH WARNINGS" if rep["warnings"] else "PASS"))
    rep["note"] = "Automated checks only. A human frame review is still required before approval."
    print(json.dumps(rep, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
