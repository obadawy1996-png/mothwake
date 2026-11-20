"""MOTHWAKE Flow-clip Short assembler (Windows-friendly).

  .venv\\Scripts\\python.exe scripts/production/assemble_flow_short.py episodes/PILOT_01/edits/SH012_edit.json

The edit JSON lists picture cuts (Flow clips with in/out), narration segments placed on the
timeline, captions and text cards. The output is a clean 1080x1920 master (never overwrites:
a new version number is added if the file exists). Clip audio is kept as a quiet room-tone bed
under the narration; final loudness is -14 LUFS with a true-peak limiter (Omar Studio lesson).
"""
import json, subprocess, sys, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
W, H, FPS = 1080, 1920, 30


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(spec, path):
    global W, H
    W, H = spec.get("size", [1080, 1920])
    st = spec.get("caption_style", {})
    size = st.get("size", 64)
    mv = st.get("marginv", 560)  # distance from bottom; ~800 keeps captions above TikTok/Reels UI
    lines = [
        "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        # Bone white text, charcoal outline (BGR hex in ASS)
        f"Style: Cap,Inter,{size},&H00D8E2E7,&H00B0DDF1,&H002B2325,&H96000000,1,0,0,0,100,100,0,0,1,5,2,2,90,90,{mv},1",
        # Whisper style: Lamp yellow italic (Theo / inner voice)
        f"Style: Whisper,Inter,{int(size*0.9)},&H00B0DDF1,&H00B0DDF1,&H002B2325,&H96000000,1,1,0,0,100,100,0,0,1,5,2,2,90,90,{mv},1",
        # Card: big Cinzel title in Old Gold, centred
        f"Style: Card,Cinzel,{int(size*1.15)},&H00689AB8,&H00689AB8,&H000D0A09,&HB4000000,1,0,0,0,100,100,2,0,3,18,0,5,90,90,0,1",
        "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    import re as _re
    for c in spec.get("captions", []):
        # *word* -> one highlighted key word in Lamp gold (owner growth plan §4.3)
        txt = _re.sub(r"\*([^*]+)\*", r"{\\c&H0060C8F0&}\1{\\r}", c["text"]).replace("\n", "\\N")
        lines.append(f"Dialogue: 0,{ass_time(c['start'])},{ass_time(c['end'])},{c.get('style','Cap')},,0,0,0,,{{\\fad(120,120)}}{txt}")
    for c in spec.get("labels", []):  # small positioned text, e.g. door numbers added in post
        lines.append(f"Dialogue: 2,{ass_time(c['start'])},{ass_time(c['end'])},Card,,0,0,0,,"
                     f"{{\\an5\\pos({c['x']},{c['y']})\\fs{c.get('size', 44)}\\bord6}}{c['text']}")
    for c in spec.get("cards", []):
        txt = c["text"].replace("\n", "\\N")
        lines.append(f"Dialogue: 1,{ass_time(c['start'])},{ass_time(c['end'])},Card,,0,0,0,,{{\\fad(200,200)}}{txt}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out_dir = ROOT / spec["out_dir"]; out_dir.mkdir(parents=True, exist_ok=True)
    base = spec["name"]; v = 1
    while (out_dir / f"{base}_v{v}.mp4").exists():
        v += 1
    out = out_dir / f"{base}_v{v}.mp4"
    work = ROOT / spec["out_dir"] / "_work"; work.mkdir(exist_ok=True)
    ass = work / f"{base}_v{v}.ass"; write_ass(spec, ass)

    inputs, fc, vlabels, alabels = [], [], [], []
    t = 0.0
    for i, cut in enumerate(spec["cuts"]):
        inputs += ["-i", str(ROOT / cut["src"])]
        sp = cut.get("speed", 1.0)  # <1 = slow motion (film breathing room)
        d = (cut["out"] - cut["in"]) / sp
        if cut.get("zoom"):  # punch-in crop, e.g. to remove unwanted generated text at a frame edge
            z = cut["zoom"]
            sc = (f"scale={int(W*z)}:{int(H*z)}:flags=lanczos,"
                  f"crop={W}:{H}:(iw-{W})*{cut.get('zx', 0.5)}:(ih-{H})*{cut.get('zy', 0.5)}")
        else:
            sc = f"scale={W}:{H}:flags=lanczos"
        if cut.get("fill") == "blur":  # vertical clip in a wide frame: sharp centre over a blurred, darkened copy
            fc.append(f"[{i}:v]trim={cut['in']}:{cut['out']},setpts=(PTS-STARTPTS)/{sp},fps={FPS},split[a{i}][b{i}]")
            fc.append(f"[a{i}]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=40:2,"
                      f"eq=brightness=-0.22:saturation=0.55[bg{i}]")
            fc.append(f"[b{i}]scale=-2:{H}:flags=lanczos[fg{i}]")
            fc.append(f"[bg{i}][fg{i}]overlay=(W-w)/2:0,setsar=1[v{i}]")
        else:
            fc.append(f"[{i}:v]trim={cut['in']}:{cut['out']},setpts=(PTS-STARTPTS)/{sp},fps={FPS},{sc},setsar=1[v{i}]")
        fc.append(f"[{i}:a]atrim={cut['in']}:{cut['out']},asetpts=PTS-STARTPTS,atempo={max(sp,0.5)},aresample=48000,"
                  f"aformat=channel_layouts=stereo,volume={cut.get('bed_db', -20)}dB[ab{i}]")
        vlabels.append(f"[v{i}]"); alabels.append(f"[ab{i}]"); t += d
    n = len(spec["cuts"])
    fc.append("".join(vlabels) + f"concat=n={n}:v=1:a=0[vcat]")
    fc.append("".join(alabels) + f"concat=n={n}:v=0:a=1[bed]")
    total = t

    # narration segments
    vo_labels = []
    for j, seg in enumerate(spec.get("vo", []) + spec.get("sfx", [])):
        k = n + j
        inputs += ["-i", str(ROOT / seg["file"])]
        delay = int(seg["at"] * 1000)
        fc.append(f"[{k}:a]atrim={seg['in']}:{seg['out']},asetpts=PTS-STARTPTS,aresample=48000,"
                  f"aformat=channel_layouts=stereo,volume={seg.get('db',0)}dB,adelay={delay}|{delay}[vo{j}]")
        vo_labels.append(f"[vo{j}]")
    if vo_labels:
        fc.append("".join(vo_labels) + f"amix=inputs={len(vo_labels)}:normalize=0[vomix]")
        fc.append("[bed][vomix]amix=inputs=2:normalize=0:duration=first[mix]")
    else:
        fc.append("[bed]anull[mix]")
    fc.append(f"[mix]loudnorm=I=-14:TP=-2:LRA=9,aresample=192000,alimiter=limit=0.79,aresample=48000[aout]")

    # watermark + captions
    wm_idx = n + len(spec.get("vo", [])) + len(spec.get("sfx", []))
    inputs += ["-i", str(ROOT / spec.get("watermark", "brand/kit/watermark_gold.png"))]
    fc.append(f"[{wm_idx}:v]scale=96:-1,format=rgba,colorchannelmixer=aa=0.55[wm]")
    fc.append("[vcat][wm]overlay=48:96[vw]")
    fontsdir = (ROOT / "brand/fonts").as_posix().replace(":", "\\:")
    assp = ass.as_posix().replace(":", "\\:")
    fade = spec.get("fade", 0)
    fx = f",fade=t=in:d={fade},fade=t=out:st={total-fade:.3f}:d={fade}" if fade else ""
    fc.append(f"[vw]subtitles='{assp}':fontsdir='{fontsdir}'{fx},format=yuv420p[vout]")

    fcfile = work / f"{base}_v{v}_fc.txt"; fcfile.write_text(";\n".join(fc), encoding="utf-8")
    cmd = [shutil.which("ffmpeg"), "-hide_banner", "-v", "error", "-n", *inputs,
           "-/filter_complex", str(fcfile), "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-r", str(FPS),
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.3f}", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-3000:]); sys.exit(1)
    print(json.dumps({"out": str(out.relative_to(ROOT)), "duration_s": round(total, 2)}))


if __name__ == "__main__":
    main()
