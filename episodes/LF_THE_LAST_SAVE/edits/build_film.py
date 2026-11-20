"""THE LAST SAVE v1: builds the 16:9 edit JSON from existing MOTHWAKE clips (0 Flow credits),
plus YouTube subtitles (SRT) and chapter timestamps. Vertical clips use the blur-fill widescreen mode.
Chapter footage is time-stretched (speed 0.6–1.0) to fit each narration take."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
E = "episodes/"
SF, W1, W2, PL = E + "SAVE_FILE/flow/", E + "WEEK_01/flow/", E + "WEEK_02/flow/", E + "PILOT_01/flow/"
LF = E + "LF_THE_LAST_SAVE/"
BLACK = LF + "flow/BLACK_6s.mp4"
WT = json.loads((ROOT / LF / "audio/vo/word_times.json").read_text(encoding="utf-8"))

def vo_len(p):
    import subprocess
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                        str(ROOT / LF / f"audio/vo/IVY_{p}.mp3")], capture_output=True, text=True)
    return float(r.stdout.strip())

CH = [  # (take, card text, [(src, in, out)], extra seconds after VO)
 ("P0", None, [(SF+"G2_C2",0,4),(SF+"G5_C2",3.5,8),(SF+"G4_C3",0,4),(W2+"SH016_C3",0,8),(W2+"SH016_C1",4.5,7.5)], 1.5),
 ("P1", "NIGHT ONE", [(SF+"G1_C1",0,8),(W1+"SH022_C1",0,6),(PL+"SH025_C1",0,6),(SF+"G1_C2",0,8),(SF+"G1_C3",0,4),
                      (SF+"G1_C4",2,8),(SF+"G4_C2",0,6),(SF+"G1_C5",0,8)], 2.0),
 ("P2", "NIGHT TWO", [(SF+"G2_C1",0,8),(SF+"G2_C2",4,8),(W1+"SH022_C2",0,6),(SF+"G2_C3",0,8),(SF+"G2_C4",0,4),
                      (SF+"G2_C5",0,8),(SF+"G2_C4",0,4)], 2.0),
 ("P3", "NIGHT THREE", [(SF+"G3_C1",0,8),(SF+"G3_C2",0,7),(SF+"G3_C3",0,8),(SF+"G3_C4",0,8),(SF+"G3_C5",0,8),
                        (W2+"SH016_C1",0,4),(W2+"SH016_C2",0,8)], 2.0),
 ("P4", "NIGHT FOUR", [(SF+"G4_C1",0,8),(SF+"G4_C3",0,8),(SF+"G4_C4",0,6),(PL+"SH025_C2",0,7),(SF+"G4_C2",0,6),
                       (SF+"G4_C5",0,8),(SF+"G1_C3",3.5,8)], 2.0),
 ("P5", "NIGHT FIVE", [(SF+"G5_C1",0,7),(SF+"G5_C2",3.5,8),(SF+"G5_C3",0,8),(SF+"G5_C4",0,3),(SF+"G5_C5",0,8),
                       (SF+"G5_C4",3,8)], 2.0),
 ("P6", "DAY SIX", [(SF+"G3_C3",3,8),(SF+"G3_C5",3,8),(SF+"G3_C2",0,6),(PL+"SH025_C2b",0,6),(SF+"G4_C5",0,8),
                    (SF+"G4_C4",0,6),(SF+"G4_C1",0,6),(W2+"SH016_C3",2,8),(SF+"G5_C3",4,8)], 6.0),
]
CARD_S, TITLE_S, VO_LEAD = 4.0, 5.0, 0.6
SFX = E + "SAVE_FILE/audio/sfx/"

def word_at(p, word, nth=1):
    k = 0
    for s, e, w in WT[p]:
        if re.sub(r"[^a-z]", "", w.lower()) == word:
            k += 1
            if k == nth:
                return s
    raise KeyError(f"{p}:{word}#{nth}")

SFX_CUES = {  # take: [(file, word, nth, length, dB)]  ("@start" = chapter start)
 "P0": [("low_drone.wav", "@start", 1, 8, -18), ("presence_swell.wav", "door", 1, 3.5, -8)],
 "P1": [("nightlight_hum.wav", "@start", 1, 50, -24), ("presence_swell.wav", "window", 2, 3.5, -8)],
 "P2": [("knock3.wav", "knocks", 1, 3.32, -4), ("low_drone.wav", "car", 2, 8, -14),
        ("bus_rumble.wav", "engine", 1, 8, -16), ("lullaby.wav", "music", 1, 5.58, -14)],
 "P3": [("lullaby.wav", "lullaby", 1, 5.58, -16), ("low_drone.wav", "lights", 1, 8, -14),
        ("presence_swell.wav", "watching", 1, 3.5, -6)],
 "P4": [("low_drone.wav", "@start", 1, 8, -16), ("knock3.wav", "knock", 1, 3.32, -2),
        ("presence_swell.wav", "feet", 1, 3.5, -8)],
 "P5": [("save_chime.wav", "save", 1, 1.05, -6), ("presence_swell.wav", "landed", 1, 3.5, -8)],
 "P6": [("low_drone.wav", "@start", 1, 8, -16), ("knock3.wav", "knock", 1, 3.32, -2),
        ("low_drone.wav", "choose", 1, 8, -12), ("presence_swell.wav", "asleep", 2, 3.5, -6)],
}
FIX = {"June": "Jun", "John": "Jun", "sunsure": "Sunshore", "Sunsure": "Sunshore", "safe": "save", "Pass": "Past",
       "pass": "past", "sleep,": "sleep,", "tire": "tyre", "15.": "fifteen.", "1": "one", "2": "two"}

cuts, vo, sfx, cards, chapters, srt = [], [], [], [], [], []
t = 0.0
for p, card, shots, extra in CH:
    if card:
        cuts.append({"src": BLACK, "in": 0, "out": CARD_S, "bed_db": -60})
        cards.append({"start": t + 0.3, "end": t + CARD_S - 0.3, "text": card})
        chapters.append((t, card.title()))
        t += CARD_S
    else:
        chapters.append((0.0, "Cold open"))
    L = vo_len(p)
    target = L + VO_LEAD + extra
    raw = sum(o - i for _, i, o in shots)
    sp = max(0.6, min(1.0, raw / target))
    pic = raw / sp
    if pic < target:  # stretch the last shot to cover the remainder
        last = shots[-1]
        need = target - (pic - (last[2] - last[1]) / sp)
        shots = shots[:-1] + [(last[0], last[1], last[1] + need * sp)]
    for src, i, o in shots:
        cuts.append({"src": src + ".mp4", "in": round(i, 3), "out": round(o, 3), "bed_db": -30,
                     "speed": round(sp, 3), "fill": "blur"})
    start = t
    vo.append({"file": LF + f"audio/vo/IVY_{p}.mp3", "in": 0, "out": round(L, 3), "at": round(start + VO_LEAD, 3)})
    for f, w, n, ln, db in SFX_CUES.get(p, []):
        at = start if w == "@start" else start + VO_LEAD + word_at(p, w, n)
        sfx.append({"file": SFX + f, "in": 0, "out": ln, "at": round(at, 3), "db": db})
    # subtitles: phrases split on punctuation or ~8 words
    cur = []
    for s, e, w in WT[p]:
        w2 = FIX.get(w.rstrip(".,?!"), w.rstrip(".,?!")) + w[len(w.rstrip(".,?!")):]
        cur.append((s, e, w2))
        if w[-1:] in ".?!," and len(cur) >= 3 or len(cur) >= 8:
            srt.append((start + VO_LEAD + cur[0][0], start + VO_LEAD + cur[-1][1] + 0.25, " ".join(x[2] for x in cur)))
            cur = []
    if cur:
        srt.append((start + VO_LEAD + cur[0][0], start + VO_LEAD + cur[-1][1] + 0.25, " ".join(x[2] for x in cur)))
    t += target
    if p == "P0":
        cuts.append({"src": BLACK, "in": 0, "out": TITLE_S, "bed_db": -60})
        cards.append({"start": t + 0.3, "end": t + TITLE_S - 0.3, "text": "THE LAST SAVE\nA MOTHWAKE STORY"})
        t += TITLE_S
cards.append({"start": t - 5.5, "end": t - 0.3, "text": "LET HIM IN, OR KEEP PLAYING?\nSOME THINGS SHOULD STAY ASLEEP."})

spec = {"name": "THE_LAST_SAVE_film", "out_dir": LF + "masters", "size": [1920, 1080], "fade": 1.0,
        "watermark": "brand/kit/watermark_gold.png", "caption_style": {"size": 64, "marginv": 90},
        "cuts": cuts, "vo": vo, "sfx": sfx, "captions": [], "cards": cards, "labels": []}
out = ROOT / LF / "edits/FILM_edit.json"
out.write_text(json.dumps(spec, indent=1, ensure_ascii=False), encoding="utf-8")

def ts(x, sep=","):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d}{sep}{int(round((s - int(s)) * 1000)):03d}"
(ROOT / LF / "masters").mkdir(exist_ok=True)
(ROOT / LF / "masters/THE_LAST_SAVE_en.srt").write_text(
    "\n".join(f"{n}\n{ts(a)} --> {ts(b)}\n{txt}\n" for n, (a, b, txt) in enumerate(srt, 1)), encoding="utf-8")
(ROOT / LF / "masters/YOUTUBE_CHAPTERS.txt").write_text(
    "\n".join(f"{int(c // 60)}:{int(c % 60):02d} {name}" for c, name in chapters), encoding="utf-8")
print(json.dumps({"total_s": round(t, 1), "cuts": len(cuts), "sfx": len(sfx), "subs": len(srt),
                  "chapters": [(round(c, 1), n) for c, n in chapters]}))
