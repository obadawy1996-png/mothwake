"""Trend-worded Short covers from caption-free source frames (v2: centred lines, no burned captions)."""
import json, subprocess
from pathlib import Path
R = Path(__file__).resolve().parents[2]; OUT = Path(__file__).parent / "covers_v2"; OUT.mkdir(exist_ok=True)
FONT = str(R / "brand/fonts/Cinzel[wght].ttf").replace("\\", "/").replace(":", "\:").replace("[", "\[").replace("]", "\]")
E = "episodes/"
C = {  # schedule index: (source clip, second, lines)
 0: (E+"SAVE_FILE/flow/G1_C5.mp4", 4.5, ["IT KNEW", "HIS WINDOW"]),
 1: (E+"PILOT_01/flow/SH012_C4.mp4", 5.0, ["THE TAPPING", "DIDN'T STOP"]),
 2: (E+"SAVE_FILE/flow/G2_C5.mp4", 6.0, ["THE GHOST CAR"]),
 3: (E+"PILOT_01/flow/SH025_C1.mp4", 4.0, ["WHICH DOOR?"]),
 4: (E+"SAVE_FILE/flow/G3_C5.mp4", 7.0, ["RULE 4"]),
 5: (E+"PILOT_01/flow/SH019_C5.mp4", 5.0, ["NIGHTLIGHT", "RULES"]),
 6: (E+"SAVE_FILE/flow/G4_C5.mp4", 6.0, ["LET HIM IN?"]),
 7: (E+"WEEK_01/flow/SH003_C4.mp4", 5.0, ["EXCEPT HIM"]),
 8: (E+"SAVE_FILE/flow/G5_C5.mp4", 7.0, ["THE SECRET", "ENDING"]),
 9: (E+"WEEK_01/flow/SH015_C4.mp4", 5.0, ["WHO'S UNDER", "THE LAMP?"]),
 10: (E+"WEEK_01/flow/SH022_C5.mp4", 5.0, ["SLEEP PARALYSIS", "DEMON"]),
 11: (E+"WEEK_01/flow/SH028_C4.mp4", 5.0, ["PAUSE AT 0:07"]),
 12: (E+"WEEK_02/flow/SH005_C4.mp4", 6.0, ["THE CREEPY", "CUSTOMER"]),
 13: (E+"WEEK_02/flow/SH010_C3.mp4", 6.0, ["WHO WROTE", "BACK?"]),
 14: (E+"WEEK_02/flow/SH026_C4.mp4", 6.0, ["CAN YOU", "FIND IT?"]),
 15: (E+"WEEK_02/flow/SH016_C4.mp4", 7.0, ["DON'T ARGUE"]),
 16: (E+"WEEK_02/flow/SH001_C4.mp4", 4.0, ["DRYER SIX"]),
 17: (E+"WEEK_02/flow/SH009_C3.mp4", 6.5, ["STILL", "COUNTING"]),
}
S = json.loads((Path(__file__).parent / "schedule.json").read_text(encoding="utf-8"))
for i, (src, t, lines) in C.items():
    y0 = 1280 if len(lines) == 2 else 1330
    txt = [f"drawtext=fontfile='{FONT}':text='{l.replace(chr(39), chr(8217)).replace(":", r"\:")}':fontcolor=0xB89A68:fontsize=104:"
           f"borderw=3:bordercolor=0x090A0D:x=(w-text_w)/2:y={y0 + k*130}" for k, l in enumerate(lines)]
    vf = ("scale=1080:1920:flags=lanczos,eq=brightness=-0.06,drawbox=y=1200:h=380:w=iw:color=0x090A0D@0.55:t=fill,"
          + ",".join(txt))
    out = OUT / (S[i]["file"][:-4] + ".jpg")
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(R / src), "-frames:v", "1", "-vf", vf,
                        "-q:v", "3", str(out)], capture_output=True, text=True)
    print(out.name, "ok" if not r.returncode else r.stderr[-150:])
    S[i]["cover"] = f"covers_v2/{out.name}"
(Path(__file__).parent / "schedule.json").write_text(json.dumps(S, indent=1, ensure_ascii=False), encoding="utf-8")
