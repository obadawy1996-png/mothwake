#!/usr/bin/env python3
"""Build EP001 storyboard.md + shots_draft.json from one shot table (planning only, no media)."""
import json, re, math
from pathlib import Path

ROOT = Path("/home/user/mothwake")
EP = ROOT / "episodes/EP001"
VO = {l["id"]: l for l in json.loads((EP / "vo.json").read_text())["lines"]}
WPM = 145
BEAT = 0.8


def words(t):
    return len(re.findall(r"[A-Za-z0-9'’]+", t))


import subprocess
AUD = EP / "audio/processed"
BLOCKS = {"S00_coldopen": ["L001", "L002", "L003"],
          "N02_act1": [f"L{i:03d}" for i in range(4, 16)],
          "N03_act2": ["L016", "L017", "L019", "L020", "L021", "L023", "L027", "L028", "L029", "L030", "L031", "L032"],
          "N04_night2": ["L033", "L036", "L037"],
          "N05_act3": ["L038", "L040", "L042", "L043", "L044", "L045", "L046"],
          "ECHO_coffee": ["L018"], "VISITOR_1974": ["L022"], "ECHO_tape1981": ["L024"], "ECHO_tape1996": ["L025"],
          "ECHO_tape2009": ["L026"], "CAL_onmic": ["L034"], "ECHO_night2_window": ["L035"], "ECHO_wall_intro": ["L039"],
          "ECHO_voicemail": ["L041"], "ECHO_ending_radio": ["L047"]}
MEAS = {}
for f in BLOCKS:
    w = AUD / f"{f}.wav"
    MEAS[f] = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(w)],
                                   capture_output=True, text=True, check=True).stdout)
LINE_MEAS = {}


def est_secs(lid):
    l = VO[lid]
    w = words(l["text"])
    s = w / WPM * 60 + l["beats"] * BEAT
    if l["speaker"] == "ECHO":
        s = max(1.6, w / 110 * 60 + 0.6)
    return s


for f, ids in BLOCKS.items():
    tot = sum(est_secs(i) for i in ids)
    for i in ids:
        LINE_MEAS[i] = MEAS[f] * est_secs(i) / tot
assert set(LINE_MEAS) == set(VO), set(VO) - set(LINE_MEAS)
MEAS_TOTAL = sum(MEAS.values())


def vo_secs(lid, frac=1.0):
    return LINE_MEAS[lid] * frac


def _old_vo_secs(lid, frac=1.0):
    l = VO[lid]
    w = words(l["text"])
    s = w / WPM * 60 + l["beats"] * BEAT
    if l["speaker"] == "ECHO":  # fragments are slowed / late in post: estimate, floor 1.6 s
        s = max(1.6, w / 110 * 60 + 0.6)
    return s * frac


BGS = [
    ("BG01", "Lantern diner interior (wide)", "L1 (pendant lamps; L4 for the dark street beyond the glass)",
     "A night busy (cold open, 2:00 exhale) · B late night, sparse, 12:5x · C quiet hour, frozen customers · "
     "D emptying, money on tables, half-eaten food · E morning, flat daylight, chairs up",
     "booth, counter, stools, jukebox, wall clock, pendant lamps, window wall (right)"),
    ("BG02", "Counter insert plate (generic close-up counter top)", "L1 / L3 per dressing",
     "A diner counter (coffee cup, recorder, radio behind) · B motel office desk (taped bell, laminated card, key) · "
     "C gas-station till (hand-lettered sign, change tray, tube-light flicker)",
     "one counter-top plate re-dressed for three locations; all inserts and hand shots"),
    ("BG03", "Diner window + hill and radio tower", "L4 outside / L1 reflection",
     "A night, tower red light (cold open, Act I) · B night 2, breath fog layer · "
     "C tower exterior, faded flashback (spring) · D tower exterior, night (Act III held silence)",
     "window frame fg, glass reflection fx, hill + tower far layer shared by all four"),
    ("BG04", "Highway and Wrenfield town line", "L3",
     "A highway in rain (arrival) · B car cabin overlay (dashboard, wipers) · C town-line sign in headlights · "
     "D town line 12:55 a.m., departing tail lights",
     "sign layer 'POP. 412' + hand-painted board shared by C and D"),
    ("BG05", "Motel room", "L4 + L2 (laptop / phone)",
     "A night 1, cheap lamp, laptop, headphones · B night 3, every light on, notes on bed · "
     "C bedside close (clock, phone on bed) · S screen-insert plates (waveform, dashboard, phone UI)",
     "screen plates are flat L2 graphics laid over a blurred room bg"),
    ("BG06", "Wrenfield main street", "L1 (diner glow) / L3 (street, forecourt) / DAY*",
     "A night, everything dark except the Lantern · B day, bright, townsfolk, bike · "
     "C gas-station forecourt end, one flickering tube light · D morning, Cal's hatchback at the kerb",
     "the gas station is the far end of main street: same far/bg, new mid"),
    ("BG07", "Town library", "DAY* (window light) / L1 desk lamp in booth",
     "A wide reading room · B cassette drawer (labels 1974/1981/1996/2009) · C listening booth with deck",
     ""),
    ("BG08", "Porch on Fenner Street", "DAY* (late afternoon)",
     "A wide porch, old woman shelling peas · B close, pea pod and hands",
     ""),
    ("BG09", "Radio booth (flashback, faded colour)", "L1 desaturated + red on-air light",
     "A man at the desk (silhouette) · B empty chair, mic light on · C mic close, tower through frosted window",
     "flashback grade: lifted, desaturated, grain fx layer"),
    ("BG10", "Ines's flat above the diner", "L4 + radio-dial glow; L5 once (door, ending)",
     "A wide, dark, small radio · B door to hallway · C window behind Ines (moth)",
     ""),
]

HERO = {
    "H01": "Coffee keeps pouring over the rim at 1:00 while everything else freezes",
    "H02": "Radio-tower red light: one slow blink (one clip, re-used at the end of Act I and in the Act III held silence)",
    "H03": "Ines turns her notepad to camera (blank page; text composited in post, re-used for COFFEE?/HABIT./NOT A WORD.)",
    "H04": "Ines tears the page off, folds it, pockets it",
    "H05": "Gas attendant counts change very slowly, smile frozen",
    "H06": "Every head in the diner turns toward Cal (the episode's first full-motion scare beat)",
    "H07": "Breath fog blooms on the outside of the window, then fades",
    "H08": "Phone buzzes on the bed (caller ID HOME), rings out, voicemail plays itself",
    "H09": "Notepad pages torn off one by one and handed over (blank pages; four texts composited)",
    "H10": "Tail lights shrink into the dark past the town-line sign",
    "H11": "Radio dial glows; Ines's hand reaches for it and stops",
    "H12": "A moth lands on the window behind Ines, lit by the radio dial",
}

# shot: (section, framing, bg-variant, description, layers[(file_stem, kind, depth)], move, strength,
#        light, vo[(id, frac)], pad, sfx, caption(text,key) or None, hero, extras{})
def L(*xs):
    return [dict(src=s, kind=k, depth=d) for s, k, d in xs]

DINER_A = L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01A_mid", "mid", 0.55), ("BG01_fx_lamps", "fx", 0.7))
SHOTS = []

def S(section, framing, bgv, desc, layers, move, strength, light, vo, pad, sfx, cap, hero=None, **ex):
    SHOTS.append(dict(section=section, framing=framing, bgv=bgv, desc=desc, layers=layers, move=move,
                      strength=strength, light=light, vo=vo, pad=pad, sfx=sfx, cap=cap, hero=hero, ex=ex))

CO, TI, A1, A2, N2, A3, EN = "Cold open", "Title", "Act I", "Act II", "Act II · second night", "Act III", "Ending"
clock = lambda v: L(("BG01_bg", "bg", 0.0), (f"BG01_clock_{v}", "mid", 0.6), ("BG01_fx_lamps", "fx", 0.8))

# ---------------- COLD OPEN
S(CO, "ECU", "BG01A", "Diner wall clock, second hand ticking 12:59:58 to 12:59:59. Warm Lamp light swings in.",
  clock("1259"), "push", 0.03, "L1", [], 2.0, "brand open_sub at 0.0 (-24 LUFS, under); clock tick x2; diner murmur",
  None, fade_in=0.4)
S(CO, "WS", "BG01A", "Booth and counter: coffee steam, waitress mid-pour, two truckers mid-laugh.",
  DINER_A + L(("BG01A_near_truckers", "near", 0.85), ("BG01_fx_steam", "fx", 0.9)), "drift", 0.02, "L1", [], 2.5,
  "laugh, cups, jukebox low, pour", None)
S(CO, "CU", "BG02A", "1:00. Every sound stops. Only the coffee keeps running over the rim onto the counter.",
  L(("BG02_bg", "bg", 0.0), ("BG02A_mid_cup", "mid", 0.6), ("BG02A_near_pot", "near", 0.9)), "push", 0.04, "L1",
  [("L001", 1)], 1.5, "HARD CUT of all diner sound at the clock landing; only pour + clock remain",
  ("In Wrenfield, nobody speaks between one and two in the morning.", "speaks"), "H01")
S(CO, "MS", "BG01C", "Frozen faces: truckers' mouths shut mid-laugh, waitress perfectly still. Coffee drips off the counter.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01C_mid", "mid", 0.55), ("BG01C_near_truckers", "near", 0.85)),
  "push", 0.04, "L1", [("L002", 1)], 0.5, "fridge hum, drip on lino, clock",
  ("Not to answer a phone. Not to call for help.", "help"))
S(CO, "WS", "BG03A", "Through the window: the radio tower on the hill blinks its red light once, slowly.",
  L(("BG03_bg", "bg", 0.0), ("BG03_far_tower", "far", 0.2), ("BG03A_mid_glass", "mid", 0.6), ("BG03_fg_frame", "fg", 1.0)),
  "push", 0.03, "L4", [("L003", 1)], 2.0, "low wind outside the glass; no sting",
  ("I went there to find out why. I should have just listened.", "listened"), "H02")
# ---------------- TITLE
S(TI, "card", "TITLE", "Title card from brand/templates/title_card_template.html: A MOTHWAKE STORY / The Quiet Hour.",
  L(("TITLE_card", "bg", 0.0)), "static", 0.0, "n/a", [], 3.0, "brand signature (1.65 s) at card start, -2 dB",
  None, hide_watermark=True, fade_in=0.3)
# ---------------- ACT I
S(A1, "WS", "BG04A", "Highway at night in rain. Cal's hatchback with a dented door.",
  L(("BG04_bg", "bg", 0.0), ("BG04A_far", "far", 0.3), ("BG04A_mid_car", "mid", 0.6), ("BG04_fx_rain", "fx", 0.95)),
  "pan_left", 0.03, "L3", [("L004", 0.4)], 0.5, "rain on tarmac, tyre hiss",
  ("I make a podcast about small towns with strange habits.", "podcast"))
S(A1, "MS", "BG04B", "Inside the car: Cal driving, dashboard glow, wipers, sodium light sliding over him.",
  L(("BG04A_far", "bg", 0.0), ("BG04B_mid_cal", "mid", 0.6), ("BG04B_fg_cabin", "fg", 1.0), ("BG04_fx_rain", "fx", 0.9)),
  "drift", 0.02, "L3", [("L004", 0.35)], 0.0, "wipers, rain on roof, indicator off",
  ("A festival nobody remembers starting. A grudge between two families.", "grudge"))
S(A1, "CU", "BG04B", "Cal in profile, half-smile, eyes on the road.",
  L(("BG04A_far", "bg", 0.0), ("BG04B_near_cal_cu", "near", 0.8), ("BG04B_fg_cabin", "fg", 1.0)),
  "push", 0.03, "L3", [("L004", 0.25)], 0.5, "rain, engine",
  ("People liked them because nothing bad ever happened at the end.", "bad"))
S(A1, "WS", "BG04C", "Town-line sign in the headlights: WRENFIELD. POP. 412.",
  L(("BG04_bg", "bg", 0.0), ("BG04C_far", "far", 0.3), ("BG04_mid_sign", "mid", 0.6), ("BG04_fx_rain", "fx", 0.95)),
  "push", 0.04, "L3", [], 2.0, "engine slows, rain", None)
S(A1, "insert", "BG04C", "Hand-painted board below the sign: VISITORS — PLEASE LEARN TO BE QUIET.",
  L(("BG04_bg", "bg", 0.0), ("BG04_near_board", "near", 0.7), ("BG04_fx_rain", "fx", 0.95)),
  "push", 0.05, "L3", [("L005", 1)], 0.5, "rain; a single wiper pass",
  ("Wrenfield's habit was already on the sign. That's rare.", "sign"))
S(A1, "MS", "BG02B", "Motel office desk. Bell with tape over the clapper. The older owner slides a key across.",
  L(("BG02_bg", "bg", 0.0), ("BG02B_mid_desk", "mid", 0.5), ("BG02B_near_owner", "near", 0.8)),
  "drift", 0.02, "L1", [("L006", 0.5)], 0.0, "desk-lamp buzz, key on wood",
  ("The motel owner didn't explain it.", "explain"))
S(A1, "insert", "BG02B", "His finger taps a laminated card twice: QUIET HOUR 1–2 A.M. THANK YOU FOR YOUR COOPERATION.",
  L(("BG02_bg", "bg", 0.0), ("BG02B_mid_card", "mid", 0.6), ("BG02B_near_finger", "near", 0.9)),
  "push", 0.04, "L1", [("L006", 0.5)], 0.5, "two taps on laminate (sync to 'tapped the card twice')",
  ("It was nine in the evening. He could have talked.", "talked"))
S(A1, "WS", "BG06C", "Gas-station forecourt at the end of main street under one flickering tube light.",
  L(("BG06_bg", "bg", 0.0), ("BG06_far", "far", 0.3), ("BG06C_mid_forecourt", "mid", 0.6), ("BG06C_fx_tube", "fx", 0.8)),
  "pan_right", 0.03, "L3", [("L007", 0.5)], 0.0, "tube-light buzz and tick, pump hum",
  ("The kid at the gas station was more relaxed about it.", "relaxed"), flicker=True)
S(A1, "MS", "BG02C", "The attendant (twenties) at the till. Sign above: WE CLOSE OUR MOUTHS AT ONE. THANK YOU.",
  L(("BG02_bg", "bg", 0.0), ("BG02C_mid_till", "mid", 0.5), ("BG02C_near_attendant", "near", 0.8)),
  "drift", 0.02, "L3", [("L007", 0.5)], 0.5, "tube buzz",
  ("Then I asked what happened to people who didn't.", "didn't"), flicker=True)
S(A1, "CU", "BG02C", "His smile stays exactly where it is. He counts out Cal's change very slowly.",
  L(("BG02_bg", "bg", 0.0), ("BG02C_mid_tray", "mid", 0.6), ("BG02C_near_hands", "near", 0.9)),
  "push", 0.05, "L3", [("L008", 1)], 1.0, "coins, one by one, too slow; tube buzz",
  ("You're not staying long, are you?", "long"), "H05", flicker=True)
S(A1, "WS", "BG06A", "Main street at night: everything shut except one diner, its windows the only warm light.",
  L(("BG06_bg", "bg", 0.0), ("BG06_far", "far", 0.3), ("BG06A_mid_lantern", "mid", 0.6), ("BG06_fx_dust", "fx", 0.9)),
  "push", 0.03, "L1", [("L009", 0.55)], 0.0, "distant dog, wind, neon hum",
  ("The only place open after midnight was a diner called the Lantern.", "Lantern"))
S(A1, "MS", "BG01B", "Ines behind the counter: fifties, steady eyes, notepad on a string around her neck.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01B_mid", "mid", 0.55), ("BG01B_near_ines", "near", 0.85)),
  "push", 0.03, "L1", [("L009", 0.45)], 0.5, "jukebox, cutlery",
  ("She didn't speak at all. Not just during the hour. Ever.", "Ever"))
S(A1, "CU", "BG01B", "Ines writes and turns the pad to camera: COFFEE?",
  L(("BG01_bg", "bg", 0.0), ("BG01B_near_ines_cu", "near", 0.7), ("BG01_fg_pad", "fg", 1.0)),
  "static", 0.0, "L1", [("L010", 0.6)], 0.0, "pencil scratch, pad flip",
  ("She wrote everything on a little pad she wore around her neck.", "pad"), "H03")
S(A1, "insert", "BG01B", "Notepad: HABIT.",
  L(("BG01_bg", "bg", 0.0), ("BG01_fg_pad", "fg", 1.0)), "push", 0.03, "L1", [("L010", 0.4)], 1.5, "pencil scratch",
  ("When I asked why the town went silent, she wrote one word.", "word"), "H03")
S(A1, "CU", "BG02A", "Her hands tear the page off, fold it in half, put it in her apron pocket.",
  L(("BG02_bg", "bg", 0.0), ("BG02A_mid_counter", "mid", 0.5), ("BG02A_near_hands", "near", 0.9)),
  "static", 0.0, "L1", [("L011", 1)], 0.5, "paper tear, fold",
  ("Like it was something that shouldn't be left lying around.", "lying"), "H04")
S(A1, "insert", "BG02A", "Cal's recorder on the counter, red light on; green level bar jumping with the jukebox.",
  L(("BG02_bg", "bg", 0.0), ("BG02A_mid_recorder", "mid", 0.6), ("BG02A_fx_led", "fx", 0.8)),
  "push", 0.04, "L1", [("L012", 1)], 0.5, "jukebox through the recorder (slightly compressed)",
  ("I stayed until one. I wanted to hear it for myself.", "hear"))
S(A1, "MS", "BG01B", "12:57. A man stops his story halfway and nods; a trucker pays in exact change.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01B_mid", "mid", 0.55), ("BG01B_near_customers", "near", 0.85)),
  "drift", 0.02, "L1", [("L013", 0.5)], 0.0, "coins on counter, chatter thinning",
  ("You could feel the whole room getting ready.", "ready"))
S(A1, "CU", "BG01B", "Two customers say goodbye to each other. Neither stands up.",
  L(("BG01_bg", "bg", 0.0), ("BG01B_near_goodbye", "near", 0.8), ("BG01_fx_lamps", "fx", 0.9)),
  "push", 0.03, "L1", [("L013", 0.5)], 0.5, "murmur fading",
  ("People said goodbye to each other at two minutes to one.", "goodbye"))
S(A1, "ECU", "BG01B", "Clock: 1:00.", clock("0100"), "push", 0.05, "L1", [], 2.0,
  "jukebox cuts with the second hand; clock tick, fridge hum only", None)
S(A1, "insert", "BG02A", "Recorder level drops to almost nothing.",
  L(("BG02_bg", "bg", 0.0), ("BG02A_mid_recorder", "mid", 0.6), ("BG02A_fx_led_low", "fx", 0.8)),
  "push", 0.04, "L1", [("L014", 0.45)], 1.0, "fridge hum, forty people breathing",
  ("How loud a room full of people being quiet is.", "quiet"))
S(A1, "WS", "BG01C", "The whole diner holding still. Breathing loops only (2% chest scale).",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01C_mid", "mid", 0.55), ("BG01C_near", "near", 0.85)),
  "push", 0.03, "L1", [("L014", 0.55)], 0.5, "breath, fridge, clock",
  ("It isn't calm. It's effort. Everybody holding something in.", "effort"))
S(A1, "CU", "BG01C", "Ines looks at Cal, writes slowly, turns the pad: NOT A WORD. PLEASE.",
  L(("BG01_bg", "bg", 0.0), ("BG01C_near_ines_cu", "near", 0.7), ("BG01_fg_pad", "fg", 1.0)),
  "static", 0.0, "L1", [], 3.5, "pencil only", None, "H03")
S(A1, "WS", "BG03A", "Through the window the tower light blinks. Then again. Steady, like breathing.",
  L(("BG03_bg", "bg", 0.0), ("BG03_far_tower", "far", 0.2), ("BG03A_mid_glass", "mid", 0.6), ("BG03_fg_frame", "fg", 1.0)),
  "push", 0.02, "L4", [], 4.0, "wind; no music", None, "H02")
S(A1, "WS", "BG01A", "2:00. Everyone exhales at once; the room goes back to normal.",
  DINER_A + L(("BG01A_near_truckers", "near", 0.85)), "drift", 0.02, "L1", [("L015", 0.55)], 0.5,
  "collective exhale, chatter and jukebox return together",
  ("At two o'clock, everyone exhaled at once.", "exhaled"))
S(A1, "MS", "BG01A", "Cal at the counter, recorder in hand, not saying a word.",
  L(("BG01_bg", "bg", 0.0), ("BG01A_mid", "mid", 0.55), ("BG01A_near_cal", "near", 0.85)),
  "push", 0.03, "L1", [("L015", 0.45)], 0.5, "room tone",
  ("I didn't say a word that first night.", "word"))
# ---------------- ACT II
S(A2, "WS", "BG05A", "Motel room: cheap lamp, laptop, Cal in headphones playing back the night.",
  L(("BG05_bg", "bg", 0.0), ("BG05A_mid", "mid", 0.5), ("BG05A_near_cal", "near", 0.8), ("BG05_fx_screen", "fx", 0.9)),
  "push", 0.03, "L4", [("L016", 0.5)], 0.5, "motel AC rattle; headphone bleed of diner chatter",
  ("Back at the motel I went through the recording.", "recording"))
S(A2, "insert", "BG05S", "Laptop screen: busy waveform, then flat at 1:00.",
  L(("BG05_bg_blur", "bg", 0.0), ("BG05S_mid_waveform_flat", "mid", 0.6)), "pan_left", 0.04, "L2",
  [("L016", 0.5)], 0.0, "playback: chatter, cups, jukebox, then nothing",
  ("One o'clock: nothing. Just the fridge and forty people breathing.", "nothing"))
S(A2, "ECU", "BG05S", "Flat line. At 1:37, a tiny blip.",
  L(("BG05_bg_blur", "bg", 0.0), ("BG05S_mid_waveform_blip", "mid", 0.6)), "push", 0.06, "L2",
  [("L017", 1)], 0.5, "fridge hum (playback)", ("Except at one thirty-seven. Something very small.", "small"))
S(A2, "CU", "BG05A", "Cal's face in screen light as he boosts the gain.",
  L(("BG05_bg", "bg", 0.0), ("BG05A_near_cal_cu", "near", 0.8), ("BG05_fx_screen", "fx", 0.9)), "push", 0.05, "L2",
  [("L018", 1)], 1.5, "1.0 s silence first; then a breath and a mouth shape (ECHO processing)",
  ("…ffee…", "…ffee…"))
S(A2, "MS", "BG05A", "Cal very still, staring at the screen.",
  L(("BG05_bg", "bg", 0.0), ("BG05A_mid", "mid", 0.5), ("BG05A_near_cal", "near", 0.8)), "static", 0.0, "L2",
  [("L019", 1)], 0.5, "AC rattle", ("It sounded like someone practising the word coffee.", "coffee"))
S(A2, "WS", "BG06B", "Day. Main street bright and friendly; people talk, laugh, wave; a kid rings a bike bell.",
  L(("BG06_bg_day", "bg", 0.0), ("BG06_far", "far", 0.3), ("BG06B_mid", "mid", 0.6), ("BG06B_near_kid", "near", 0.9)),
  "pan_right", 0.03, "DAY*", [("L020", 0.5)], 0.0, "bike bell, birds, overlapping chatter (loud contrast)",
  ("In daylight, Wrenfield was the friendliest town I've ever been to.", "friendliest"))
S(A2, "MS", "BG06B", "Townsfolk talking a little too much, a little too fast.",
  L(("BG06_bg_day", "bg", 0.0), ("BG06B_mid", "mid", 0.5), ("BG06B_near_townsfolk", "near", 0.85)),
  "drift", 0.02, "DAY*", [("L020", 0.5)], 0.5, "chatter",
  ("As if they were getting it all out of their system.", "system"))
S(A2, "WS", "BG07A", "Town library reading room, dust in window light.",
  L(("BG07_bg", "bg", 0.0), ("BG07A_mid", "mid", 0.5), ("BG07_fx_dust", "fx", 0.9)), "push", 0.03, "DAY*",
  [("L021", 0.45)], 0.5, "clock, page turn", ("The library kept tapes. Interviews with visitors.", "tapes"))
S(A2, "insert", "BG07B", "A drawer of cassette tapes labelled by year: 1974, 1981, 1996, 2009.",
  L(("BG07_bg", "bg", 0.0), ("BG07B_mid_drawer", "mid", 0.6)), "pan_left", 0.03, "DAY*",
  [("L021", 0.55)], 0.5, "drawer slide, cassettes clack",
  ("A stranger who'd come to ask about the quiet hour.", "stranger"))
S(A2, "MS", "BG07C", "Listening booth. Tape 1974 in the deck. A nervous man laughing on tape.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_mid_booth", "mid", 0.5), ("BG07C_near_cal", "near", 0.85)), "push", 0.03, "L1",
  [("L022", 1)], 0.5, "tape hiss, deck clunk", ("So what happens if I talk? Hello? Hello?", "Hello"))
S(A2, "CU", "BG07C", "Cassette reels turning in the deck.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_mid_deck", "mid", 0.7)), "push", 0.04, "L1", [("L023", 0.5)], 0.0,
  "tape hiss", ("Each tape ended the same way. The visitor talked during the hour.", "talked"))
S(A2, "MS", "BG07C", "Cal listening, headphones pressed to his ears.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_mid_booth", "mid", 0.5), ("BG07C_near_cal", "near", 0.85)), "drift", 0.02, "L1",
  [("L023", 0.5)], 0.5, "tape hiss", ("Afterwards, the historian went outside and recorded the silence.", "silence"))
S(A2, "insert", "BG07C", "Tape label 1981 in the deck. Wind on the tape.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_mid_tape1981", "mid", 0.7)), "push", 0.04, "L1", [("L024", 1)], 1.0,
  "outdoor wind on tape, then the voice", ("…hello…", "…hello…"))
S(A2, "insert", "BG07C", "Tape label 1996.", L(("BG07_bg", "bg", 0.0), ("BG07C_mid_tape1996", "mid", 0.7)),
  "push", 0.04, "L1", [("L025", 1)], 0.5, "tape hiss, wind", ("…what happens if I…", "happens"))
S(A2, "insert", "BG07C", "Tape label 2009. Clearer, nearly a sentence.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_mid_tape2009", "mid", 0.7)), "push", 0.05, "L1", [("L026", 1)], 1.0,
  "less hiss each year", ("…is anybody… out there…", "anybody…"))
S(A2, "CU", "BG07C", "Cal takes the headphones off slowly.",
  L(("BG07_bg", "bg", 0.0), ("BG07C_near_cal_cu", "near", 0.8)), "push", 0.04, "L1", [("L027", 0.5)], 0.5,
  "room tone", ("It wasn't just repeating them. It was keeping them.", "keeping"))
S(A2, "WS", "BG07B", "The drawer of tapes, rows of years.",
  L(("BG07_bg", "bg", 0.0), ("BG07B_mid_drawer", "mid", 0.6), ("BG07_fx_dust", "fx", 0.9)), "push", 0.04, "DAY*",
  [("L027", 0.5)], 0.5, "low room tone", ("Fifty years of tourists, teaching it one sentence at a time.", "teaching"))
S(A2, "WS", "BG08A", "Afternoon porch on Fenner Street. An old woman shelling peas eyes Cal's recorder.",
  L(("BG08_bg", "bg", 0.0), ("BG08A_mid_porch", "mid", 0.5), ("BG08A_near_woman", "near", 0.8)), "drift", 0.02,
  "DAY*", [("L028", 0.5)], 0.0, "peas into a bowl, screen door, wind chime",
  ("I tried to get someone to say it on the record.", "record"))
S(A2, "MS", "BG08A", "Cal clicks the recorder off and shows her. She leans in close.",
  L(("BG08_bg", "bg", 0.0), ("BG08A_mid_porch", "mid", 0.5), ("BG08A_near_both", "near", 0.85)), "push", 0.03,
  "DAY*", [("L028", 0.5)], 0.5, "recorder click", ("As long as I turned off the recorder first.", "recorder"))
S(A2, "CU", "BG08A", "Her face, close, lowering her voice.",
  L(("BG08_bg", "bg", 0.0), ("BG08A_near_woman_cu", "near", 0.8)), "push", 0.03, "DAY*", [("L029", 0.35)], 0.0,
  "wind chime fades", ("The town still had a night-time radio show.", "radio"))
S(A2, "WS", "BG09A", "Flashback (faded colour): tiny radio booth, a man reading the news (silhouette).",
  L(("BG09_bg", "bg", 0.0), ("BG09A_mid_man", "mid", 0.6), ("BG09_fx_grain", "fx", 1.0)), "drift", 0.02, "L1",
  [("L029", 0.4)], 0.0, "old AM hiss, faint weather report bed (original, no voice)",
  ("Requests, weather, a man reading the news.", "news"), fade_in=0.5)
S(A2, "MS", "BG09B", "Flashback: the chair empty, microphone ON light still lit.",
  L(("BG09_bg", "bg", 0.0), ("BG09B_mid_empty", "mid", 0.6), ("BG09B_fx_onair", "fx", 0.8), ("BG09_fx_grain", "fx", 1.0)),
  "push", 0.04, "L1", [("L029", 0.25)], 0.5, "AM hiss continues",
  ("The station kept broadcasting after the man went home.", "home"), flicker=True)
S(A2, "CU", "BG09C", "Flashback: mic close; through the frosted window the tower light blinks.",
  L(("BG09_bg", "bg", 0.0), ("BG03_far_tower", "far", 0.2), ("BG09C_mid_mic", "mid", 0.7), ("BG09_fx_grain", "fx", 1.0)),
  "push", 0.04, "L1", [("L030", 0.45)], 0.0, "hiss with fragments of syllables (no words)",
  ("Nobody was in the booth. But something kept talking.", "talking"), flicker=True)
S(A2, "WS", "BG03C", "Flashback: the tower on the hill in spring; the transmitter hut gutted.",
  L(("BG03C_bg_spring", "bg", 0.0), ("BG03_far_tower", "far", 0.3), ("BG09_fx_grain", "fx", 1.0)), "push", 0.03,
  "DAY*", [("L030", 0.55)], 0.5, "birds, wind; AM hiss cuts out",
  ("They tore the transmitter out in the spring. The tower's still there.", "transmitter"))
S(A2, "CU", "BG08B", "Back on the porch: she splits a pea pod with her thumbnail.",
  L(("BG08_bg", "bg", 0.0), ("BG08B_near_hands", "near", 0.8)), "static", 0.0, "DAY*", [("L031", 1)], 0.5,
  "pod snap (crisp, close)", ("Honey, it's always been out there.", "always"))
S(A2, "MS", "BG06A", "Cal in his parked car on main street, recorder in his lap, lit by the dashboard.",
  L(("BG06_bg", "bg", 0.0), ("BG06A_mid_lantern", "mid", 0.4), ("BG04B_mid_cal_parked", "near", 0.8), ("BG04B_fg_cabin", "fg", 1.0)),
  "drift", 0.02, "L3", [("L032", 0.5)], 0.0, "engine ticking as it cools",
  ("I should have left then. But I'm a podcaster.", "left"))
S(A2, "CU", "BG06A", "Cal's face, decided.",
  L(("BG06_bg", "bg", 0.0), ("BG04B_near_cal_cu", "near", 0.8), ("BG04B_fg_cabin", "fg", 1.0)), "push", 0.04, "L3",
  [("L032", 0.5)], 0.5, "engine tick", ("I had the best story of my life sitting in a drawer.", "story"))
# ---------------- SECOND NIGHT
S(N2, "MS", "BG01B", "12:58. Ines sees Cal's recorder and shakes her head: a small, frightened no.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01B_mid", "mid", 0.55), ("BG01B_near_ines_no", "near", 0.85)),
  "push", 0.03, "L1", [("L033", 1)], 2.0, "chatter thinning, clock", ("The second night, I talked.", "talked"))
S(N2, "ECU", "BG01C", "Clock: 1:00 (re-use).", clock("0100"), "push", 0.05, "L1", [], 1.5,
  "all sound cuts; fridge, clock", None)
S(N2, "CU", "BG02A", "Cal leans close to his recorder and speaks.",
  L(("BG02_bg", "bg", 0.0), ("BG02A_mid_recorder", "mid", 0.6), ("BG02A_near_cal_cu", "near", 0.9)), "push", 0.05,
  "L1", [("L034", 1)], 0.5, "Cal's voice dry and close, no reverb (it must feel too loud)",
  ("It's one o'clock in Wrenfield, and I'm going to say something.", "something"))
S(N2, "WS", "BG01C", "Every head in the diner turns. Nobody speaks.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01C_mid_turn", "mid", 0.55), ("BG01C_near_turn", "near", 0.85)),
  "static", 0.0, "L1", [], 2.5, "chairs creak in unison; nothing else", None, "H06")
S(N2, "MS", "BG01C", "A woman covers her child's ears.",
  L(("BG01_bg", "bg", 0.0), ("BG01C_near_mother", "near", 0.8)), "push", 0.03, "L1", [], 2.0, "fridge hum", None)
S(N2, "CU", "BG03B", "Outside the glass, a faint fog of breath appears, as if someone stands very close.",
  L(("BG03_bg", "bg", 0.0), ("BG03_far_tower", "far", 0.2), ("BG03A_mid_glass", "mid", 0.6), ("BG03B_fx_fog", "fx", 0.8),
    ("BG03_fg_frame", "fg", 1.0)), "push", 0.04, "L4", [("L035", 1)], 2.0,
  "1.0 s total silence, then ECHO (Cal, flat, late, through glass)", ("…it's one o'clock… in…", "one"), "H07")
S(N2, "CU", "BG01C", "Cal frozen. Behind him, the fog on the glass slowly fades.",
  L(("BG01_bg", "bg", 0.0), ("BG03B_fx_fog", "far", 0.3), ("BG01C_near_cal_cu", "near", 0.85)), "push", 0.03,
  "L1", [("L036", 0.45)], 0.5, "his breathing", ("It used my voice. Not well.", "voice"))
S(N2, "insert", "BG01C", "Ines writes, hands shaking, doesn't turn the pad. She closes her eyes.",
  L(("BG01_bg", "bg", 0.0), ("BG01C_near_ines_eyes", "near", 0.7), ("BG01_fg_pad", "fg", 1.0)), "static", 0.0, "L1",
  [("L036", 0.55)], 1.5, "pencil shaking", ("Like someone wearing a coat that doesn't fit yet.", "coat"))
S(N2, "WS", "BG01D", "2:00. Money left on tables, food unfinished; people leave without a word.",
  L(("BG01_bg", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01D_mid", "mid", 0.55), ("BG01D_near_leaving", "near", 0.85)),
  "drift", 0.02, "L1", [("L037", 0.4)], 0.5, "coats, door bell, nobody talks",
  ("At two o'clock, nobody said goodbye. They just left.", "left"))
S(N2, "MS", "BG01D", "Ines locks the door behind the last of them.",
  L(("BG01_bg", "bg", 0.0), ("BG01D_mid", "mid", 0.55), ("BG01D_near_ines_door", "near", 0.85)), "push", 0.03, "L1",
  [("L037", 0.25)], 0.0, "lock turning", ("Ines locked the door behind the last of them.", "locked"))
S(N2, "MS", "BG01D", "She points: at Cal, at the door, at the road out of town.",
  L(("BG01_bg", "bg", 0.0), ("BG01D_mid", "mid", 0.55), ("BG01D_near_ines_point", "near", 0.85)), "static", 0.0,
  "L1", [("L037", 0.35)], 1.0, "fridge hum", ("It was the clearest sentence anyone said to me in Wrenfield.", "clearest"))
# ---------------- ACT III
S(A3, "WS", "BG05B", "Night three. Every light on. Notes, dates, a hand-drawn timeline all over the bed. Cal hasn't slept.",
  L(("BG05_bg", "bg", 0.0), ("BG05B_mid_notes", "mid", 0.5), ("BG05B_near_cal", "near", 0.85)), "push", 0.03, "L1",
  [("L038", 1)], 0.5, "AC rattle, lamp buzz", ("I stayed in my room with every light on.", "light"))
S(A3, "insert", "BG05C", "Bedside clock: 1:12.",
  L(("BG05C_bg_bedside", "bg", 0.0), ("BG05C_mid_clock", "mid", 0.6)), "push", 0.04, "L1", [], 2.0,
  "clock flip", None)
S(A3, "MS", "BG05B", "Cal turns toward the wall. Through it, faint and conversational, his own voice.",
  L(("BG05_bg", "bg", 0.0), ("BG05B_mid_wall", "mid", 0.5), ("BG05B_near_cal_turn", "near", 0.85)), "push", 0.05,
  "L1", [("L039", 1)], 1.0, "ECHO muffled through drywall (low-pass)",
  ("…I make a podcast about small towns… with strange habits…", "podcast"))
S(A3, "CU", "BG05B", "Cal's face: recognition.",
  L(("BG05_bg", "bg", 0.0), ("BG05B_near_cal_cu", "near", 0.85)), "push", 0.04, "L1", [("L040", 0.5)], 0.5,
  "room tone", ("That was my intro. Word for word.", "intro"))
S(A3, "MS", "BG05B", "Cal on the bed among the notes, hugging his knees.",
  L(("BG05_bg", "bg", 0.0), ("BG05B_mid_notes", "mid", 0.5), ("BG05B_near_cal", "near", 0.85)), "drift", 0.02, "L1",
  [("L040", 0.5)], 0.0, "room tone", ("In the car. In the motel. Every time I talked to myself.", "myself"))
S(A3, "insert", "BG05C", "1:24. Phone buzzes on the bed. Caller ID: HOME. It rings out.",
  L(("BG05C_bg_bedside", "bg", 0.0), ("BG05C_mid_phone_home", "mid", 0.6), ("BG05_fx_screen", "fx", 0.8)),
  "push", 0.04, "L2", [], 4.0, "vibration on the mattress x3, then stop", None, "H08")
S(A3, "insert", "BG05C", "A voicemail notification. He doesn't touch it. It plays on speaker by itself.",
  L(("BG05C_bg_bedside", "bg", 0.0), ("BG05C_mid_phone_vm", "mid", 0.6), ("BG05_fx_screen", "fx", 0.8)),
  "push", 0.05, "L2", [("L041", 1)], 0.5, "phone-speaker EQ on ECHO (almost natural)",
  ("Pick up. I want to tell you about the town.", "town"), "H08")
S(A3, "CU", "BG05B", "Cal staring at the phone.",
  L(("BG05_bg", "bg", 0.0), ("BG05B_near_cal_cu", "near", 0.85), ("BG05_fx_screen", "fx", 0.9)), "push", 0.03, "L2",
  [("L042", 1)], 0.5, "room tone", ("The only person who calls me from home is me.", "home"))
S(A3, "insert", "BG05S", "Laptop: podcast dashboard. A draft he never made: WRENFIELD — Part 1. Length 41 minutes.",
  L(("BG05_bg_blur", "bg", 0.0), ("BG05S_mid_dashboard", "mid", 0.6)), "push", 0.05, "L2", [("L043", 1)], 1.5,
  "laptop fan; trackpad click", ("The one place where a voice can go on talking.", "talking"))
S(A3, "WS", "BG01E", "Morning at the Lantern. Ines writes fast, for the first time.",
  L(("BG01_bg_day", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01E_mid", "mid", 0.55), ("BG01E_near_ines", "near", 0.85)),
  "push", 0.03, "DAY*", [], 1.5, "pencil racing, coffee machine", None)
for txt, p in (("IT CAN'T FINISH IF WE DON'T TEACH IT.", 3.0), ("EVERY VISITOR GAVE IT WORDS.", 2.5),
               ("YOU GAVE IT MORE THAN ANYONE.", 2.5), ("IT ONLY NEEDS THE LAST ONES.", 3.0)):
    S(A3, "insert", "BG02A", f"Notepad page torn off and handed to Cal: {txt}",
      L(("BG02_bg_day", "bg", 0.0), ("BG02A_mid_counter", "mid", 0.5), ("BG01_fg_pad", "fg", 1.0)), "push", 0.02,
      "DAY*", [], p, "page tear; page slides across the counter", None, "H09")
S(A3, "MS", "BG01E", "Ines looks at the radio behind the counter.",
  L(("BG01_bg_day", "bg", 0.0), ("BG01E_mid", "mid", 0.55), ("BG01E_near_ines_look", "near", 0.85)), "push", 0.03,
  "DAY*", [("L044", 0.5)], 0.0, "room tone drops out", ("I asked her what happens when it finishes.", "finishes"))
S(A3, "CU", "BG02A", "The old radio behind the counter, dial dark.",
  L(("BG02_bg_day", "bg", 0.0), ("BG02A_mid_radio", "mid", 0.7)), "push", 0.05, "DAY*", [("L044", 0.5)], 0.5,
  "faint electrical hum from the radio (no signal)", ("The way you look at a door you're not allowed to open.", "door"))
S(A3, "WS", "BG01E", "Cal and Ines small in the wide frame, the radio between them.",
  L(("BG01_bg_day", "bg", 0.0), ("BG01_far", "far", 0.25), ("BG01E_mid", "mid", 0.55), ("BG01E_near_both", "near", 0.85)),
  "drift", 0.02, "DAY*", [("L045", 1)], 0.5, "room tone", ("The silence was never a superstition. It was a wall.", "wall"))
S(A3, "MS", "BG06D", "At his car: Cal puts the recorder in the glovebox and locks it.",
  L(("BG06_bg_day", "bg", 0.0), ("BG06D_mid_car", "mid", 0.5), ("BG04B_fg_cabin", "fg", 1.0)), "push", 0.03,
  "DAY*", [("L046", 0.35)], 0.0, "glovebox click, key", ("So I decided to leave without saying another word.", "leave"))
S(A3, "insert", "BG05S", "Laptop: he deletes the draft. 'Are you sure?' He clicks yes.",
  L(("BG05_bg_blur", "bg", 0.0), ("BG05S_mid_delete", "mid", 0.6)), "static", 0.0, "L2", [("L046", 0.35)], 0.5,
  "trackpad click", ("I deleted the episode. I'd make something else.", "deleted"))
S(A3, "CU", "BG06D", "Cal behind the wheel, jaw set.",
  L(("BG06_bg_day", "bg", 0.0), ("BG04B_near_cal_cu", "near", 0.8), ("BG04B_fg_cabin", "fg", 1.0)), "push", 0.03,
  "DAY*", [("L046", 0.3)], 0.5, "engine starts", ("Something where nothing bad happens at the end.", "nothing"))
S(A3, "WS", "BG04D", "The town line at 12:55 a.m. The sign. The car's tail lights shrink into the dark.",
  L(("BG04_bg", "bg", 0.0), ("BG04D_far", "far", 0.3), ("BG04_mid_sign", "mid", 0.6), ("BG04D_fx_taillights", "fx", 0.8)),
  "static", 0.0, "L3", [], 3.5, "engine recedes to nothing", None, "H10")
S(A3, "WS", "BG03D", "Held silence, four seconds. On the hill, the tower light blinks.",
  L(("BG03D_bg_night", "bg", 0.0), ("BG03_far_tower", "far", 0.3)), "static", 0.0, "L4", [], 4.0,
  "NOTHING. True digital silence for 4.0 s (QC: confirm intentional)", None, "H02")
# ---------------- ENDING
S(EN, "WS", "BG10A", "Ines's flat above the diner, 1:30 a.m. She sits in the dark beside a small radio.",
  L(("BG10_bg", "bg", 0.0), ("BG10A_mid", "mid", 0.5), ("BG10A_near_ines", "near", 0.85)), "push", 0.02, "L4", [],
  2.0, "radio crackle builds", None, hide_watermark=True, fade_in=0.5)
S(EN, "CU", "BG10A", "The radio dial glows. A podcast intro: Cal's voice, fluent, perfect.",
  L(("BG10_bg", "bg", 0.0), ("BG10A_mid_radio", "mid", 0.7), ("BG10_fx_dial", "fx", 0.9)), "push", 0.04, "L4",
  [("L047", 0.45)], 0.5, "ECHO as Cal: full-range, warm, NO processing (it has learned)",
  ("I make a podcast about small towns with strange habits.", "podcast"), "H11", hide_watermark=True)
S(EN, "MS", "BG10A", "Ines listening, her face lit only by the dial; Lamp highlight in her eyes.",
  L(("BG10_bg", "bg", 0.0), ("BG10A_near_ines_lit", "near", 0.85), ("BG10_fx_dial", "fx", 0.9)), "push", 0.03, "L4",
  [("L047", 0.25)], 0.0, "radio", ("This week: a town called Wrenfield. I'm here now.", "here"), hide_watermark=True)
S(EN, "CU", "BG10A", "Ines reaches for the dial. Her hand stops.",
  L(("BG10_bg", "bg", 0.0), ("BG10A_mid_radio", "mid", 0.7), ("BG10A_near_hand", "near", 0.9), ("BG10_fx_dial", "fx", 0.95)),
  "static", 0.0, "L4", [("L047", 0.3)], 1.0, "radio; the same voice, very faintly, from the hallway (offset 0.3 s)",
  ("And I'm going to talk for as long as you'll let me.", "talk"), "H11", hide_watermark=True)
S(EN, "MS", "BG10B", "Hold on the door. Warm light under it, from the hallway: the wrong direction.",
  L(("BG10_bg", "bg", 0.0), ("BG10B_mid_door", "mid", 0.6), ("BG10B_fx_underdoor", "fx", 0.8)), "push", 0.03, "L5",
  [], 3.0, "hallway voice continues, unintelligible", None, hide_watermark=True)
S(EN, "CU", "BG10C", "A moth lands on the window behind her, lit by the radio dial.",
  L(("BG10C_bg_window", "bg", 0.0), ("BG10C_mid_glass", "mid", 0.5), ("BG10C_near_moth", "near", 0.8), ("BG10_fx_dial", "fx", 0.9)),
  "push", 0.03, "L4", [], 4.0, "a single soft wing flutter (motif: something is noticing you)", None, "H12",
  hide_watermark=True)
S(EN, "black", "-", "Cut to black. Then brand outro (exports.outro) and the YouTube end screen.",
  L(("BLACK", "bg", 0.0)), "static", 0.0, "n/a", [], 1.5, "voice cuts with the picture", None, hide_watermark=True)


def r05(x):
    return max(1.5, round(x * 2) / 2)


rows, out = [], []
for i, s in enumerate(SHOTS, 1):
    sid = f"S{i:03d}"
    dur = r05(sum(vo_secs(l, f) for l, f in s["vo"]) + s["pad"])
    vo_txt = ", ".join(l if f == 1 else f"{l} (~{int(f*100)}%)" for l, f in s["vo"]) or "— (visual only)"
    sh = {"id": sid, "section": s["section"], "framing": s["framing"], "background": s["bgv"],
          "layers": [{"src": f"art/{x['src']}.png", "depth": x["depth"]} for x in s["layers"]],
          "duration": dur, "move": s["move"], "strength": s["strength"], "lighting": s["light"],
          "vo": [l for l, _ in s["vo"]]}
    if s["hero"]:
        sh["hero_clip"] = s["hero"]
    if s["ex"].get("flicker"):
        sh["flicker"] = True
    if s["ex"].get("fade_in"):
        sh["fade_in"] = s["ex"]["fade_in"]
    if s["ex"].get("hide_watermark"):
        sh["hide_watermark"] = True
    if s["cap"]:
        t, k = s["cap"]
        assert words(t) <= 12, (sid, t)
        bad = k.lower() not in [w.strip('.,!?').lower() for w in t.split()]
        print('KEYMISS', sid, k, t) if bad else None
        sh["caption"] = {"text": t, "key": k, "y": 0.80}
        if s["vo"] and s["pad"] >= 1.0:
            sh["caption"]["from"] = round(min(s["pad"] - 0.5, 1.0), 1)
    out.append(sh)
    rows.append((sid, s, dur, vo_txt))

total = sum(x["duration"] for x in out)
heroes_used = sorted({x.get("hero_clip") for x in out if x.get("hero_clip")})
assert len(heroes_used) <= 12
bgs_used = sorted({x["background"][:4] for x in out if x["background"].startswith("BG")})

(EP / "shots_draft.json").write_text(json.dumps(
    {"episode": "EP001", "status": "draft — storyboard v1, not yet reviewed",
     "note": "Layer PNGs are placeholders (art/*.png do not exist yet). Shot durations = measured length of the processed "
             "narration file for the block (ffprobe, 2026-11-19), split across lines and shots by word share (estimate), "
             "plus visual pads; re-time against real line onsets before assembly. Extra keys "
             "(id, section, framing, background, lighting, vo, hero_clip) are ignored by assemble.py.",
     "estimated_total_seconds": total, "shots": out}, indent=2, ensure_ascii=False) + "\n")

# section totals
sec = {}
for sid, s, d, _ in rows:
    sec[s["section"]] = sec.get(s["section"], 0) + d
vo_total = MEAS_TOTAL
est_total = sum(est_secs(l) for l in VO)

md = []
A = md.append
A("# EP001 — The Quiet Hour · Storyboard v1 (draft)\n")
A("**Source:** `episodes/EP001/script.md` (v3) + `episodes/EP001/vo.json` · **Format:** long-form 16:9, 1920×1080 · "
  "**Owner of this file:** Storyboard Designer · **Date:** 2026-11-19 · **Status:** draft, not reviewed\n")
A("Companion file: `episodes/EP001/shots_draft.json` (the `shots` array for `scripts/production/assemble.py`). "
  "No media was generated and no paid service was used.\n")
A("## Timing summary (all **estimates**)\n")
A("| Item | Value | Basis |\n|---|---|---|")
A(f"| Narration words | 1,089 | **measured**: `scripts/production/script_stats.py`, 2026-11-19 |")
A(f"| Narration, recorded | {vo_total:.1f} s ({vo_total/60:.2f} min) | **measured**: ffprobe on the 15 files in `episodes/EP001/audio/processed/`, 2026-11-19 (≈ {1089/(vo_total/60):.0f} wpm incl. pauses) |")
A(f"| Narration, planning estimate | {est_total:.0f} s | estimate at 145 wpm + 0.8 s/beat; superseded by the measured files |")
A(f"| Visual-only pads, silences, cards | {total - vo_total:.0f} s | estimate: per-shot pads below |")
A(f"| **Picture total (shots)** | **{total:.1f} s ≈ {int(total//60)}:{int(total%60):02d}** | sum of shot durations (estimate built on measured VO) |")
A("| + brand outro | 3.2 s | brand/video/mothwake_outro_1920x1080.mp4 (exports.outro) |")
A("| + end screen | 10–20 s | YouTube end-screen element, see issues |")
A(f"| Shots | {len(out)} | |")
A(f"| Hero clips (Google Flow, manual) | {len(heroes_used)} unique, used in {sum(1 for x in out if x.get('hero_clip'))} shots | budget ≤ 12 |")
A(f"| Unique backgrounds | {len(bgs_used)} (+ title card, black) | budget ≤ 10 |\n")
A("| Section | Script range | Estimated length |\n|---|---|---|")
ranges = {CO: "0:00–0:30", TI: "0:30–0:36", A1: "0:36–3:50", A2: "3:50–7:30", N2: "(inside Act II)", A3: "7:30–10:00", EN: "10:00–10:50"}
t0 = 0
for k in (CO, TI, A1, A2, N2, A3, EN):
    A(f"| {k} | {ranges[k]} | {sec[k]:.1f} s (starts ≈ {int(t0//60)}:{int(t0%60):02d}) |")
    t0 += sec[k]
A("")
A("## Conventions\n")
A("- **Framing:** WS wide · MS medium · CU close-up · ECU extreme close-up · insert (prop/hand detail).")
A("- **Layers:** `kind@depth`, depth 0 = farthest (static), 1 = nearest (moves most). Files are `art/<bg_id>_<layer>.png` "
  "placeholders; a variant letter in the id (e.g. `BG01C_mid`) means a re-dressed layer on a shared plate (`BG01_bg`).")
A("- **Move:** `push` / `drift` / `pan_left` / `pan_right` / `static`; strength is the assembler value (0.02 = barely, 0.06 = strong dread push). "
  "Keep to the Environment Bible recipe: ≤ 4% scale on drifts.")
A("- **Lighting:** Environment Bible presets L1–L5. `DAY*` = daylight scene; the bible has **no daylight preset** (see issues). "
  "L5 Reveal is used **once**: S" + next(r[0][1:] for r in rows if r[1]["light"] == "L5") + ".")
A("- **Captions:** long-form lower third (y = 0.80), Inter SemiBold 46 px, Bone with key word in Lamp, ≤ 12 words, text taken from the narration. "
  "No caption on visual-only shots; on-screen notepad text is art, not caption.")
A("- **Watermark:** hidden on title card and the whole ending (S" + next(r[0][1:] for r in rows if r[1]["section"] == EN) + " onward).")
A("- **Hero clip:** a manual Google Flow generation (no API, owner runs it). Everything else is a layered parallax still (free).\n")

A("## Background inventory (10 unique)\n")
A("| ID | Background | Lighting | Dressing variants | Notes | Shots |\n|---|---|---|---|---|---|")
for bid, name, light, var, note in BGS:
    used = [r[0] for r in rows if r[1]["bgv"].startswith(bid)]
    A(f"| {bid} | {name} | {light} | {var} | {note or '—'} | {len(used)} |")
A("\nShared overlay assets (not backgrounds): `BG04B_fg_cabin` (car cabin, used on highway, main street night and day), "
  "`BG01_fg_pad` (Ines's notepad, blank, text composited), `BG03_far_tower` (hill + tower, also seen through the radio-booth window), "
  "`BG01_clock_*` (diner clock faces 12:59 / 1:00), `BG04_fx_rain`, `BG06_fx_dust`, `BG09_fx_grain`.\n")
A("Every location is built once in 4–6 layers per the Environment Bible; three locations (diner counter, motel office, gas-station till) "
  "share one counter-top plate (BG02), and the gas station is the far end of main street (BG06C). Each background has ≥ 3 dressing "
  "variants except BG07–BG10 (2–3; they appear in one sequence each).\n")

A("## Hero clips (12, Google Flow, manual)\n")
A("| Hero | Moment | Shots | Why it earns motion |\n|---|---|---|---|")
why = {"H01": "the hook image; the one thing still moving at 1:00", "H02": "the recurring 'something is awake' signal; one clip, three uses",
       "H03": "Ines's only voice; one clip, three pages", "H04": "establishes that words are dangerous objects",
       "H05": "first human wrongness in town", "H06": "first full-motion scare beat (bible: full motion saved for the scare)",
       "H07": "the Echo's first physical trace", "H08": "the Echo reaches into Cal's own life",
       "H09": "Ines finally 'speaks'; the rule explained", "H10": "Cal's escape, emotionally false relief",
       "H11": "the twist lands on the radio", "H12": "brand easter egg and final frame"}
for h, d in HERO.items():
    used = [r[0] for r in rows if r[1]["hero"] == h]
    A(f"| {h} | {d} | {', '.join(used)} | {why[h]} |")
A("\nEach hero clip must also exist as a layered still fallback (the layers listed per shot), so the episode renders end-to-end before any "
  "Flow clip exists. Character references for Flow must come only from approved character sheets (CHARACTER_BIBLE: ≤ 3 ingredients each). "
  "Notepad, sign and screen **text is never generated**: generate blank surfaces and composite text in post.\n")

A("## Shot list\n")
cur = None
for sid, s, d, vo_txt in rows:
    if s["section"] != cur:
        cur = s["section"]
        A(f"\n### {cur}\n")
        A("| Shot | Dur (s) | Framing | BG | Description | Layers (kind@depth) | Move | Light | VO | SFX | Caption key | Type |")
        A("|---|---|---|---|---|---|---|---|---|---|---|---|")
    lay = ", ".join(f"{x['src']} {x['kind']}@{x['depth']}" for x in s["layers"])
    mv = s["move"] if s["move"] == "static" else f"{s['move']} {s['strength']}"
    if s["ex"].get("flicker"):
        mv += " · flicker"
    cap = f"**{s['cap'][1]}** — “{s['cap'][0]}”" if s["cap"] else "—"
    typ = f"**HERO {s['hero']}**" if s["hero"] else "parallax still"
    if s["ex"].get("hide_watermark"):
        typ += " · no watermark"
    A(f"| {sid} | {d} | {s['framing']} | {s['bgv']} | {s['desc']} | {lay} | {mv} | {s['light']} | {vo_txt} | {s['sfx']} | {cap} | {typ} |")


A("\n## Issues and script notes (for Storywriter / Creative Director; this file does not change the script)\n")
for n, t in enumerate([
  "**Hook timing vs Video Branding Guide.** The guide wants the hook line within 1.5 s. The script opens on a clock and a busy diner before the 1:00 cut, so L001 starts at ≈ 4.5 s + 1.5 s pad (≈ 6 s). Storyboard compresses the pre-roll to 4.5 s; going lower kills the 'sound stops' gag. Decide: accept ≈ 6 s, or put a 1-line hook caption/ECHO whisper over S001.",
  "**Title card length.** Script reserves 0:30–0:36 (6 s); the branding guide caps title cards at 2–3 s. Storyboard uses 3.0 s.",
  f"**Runtime is short of the ~9.5 min target.** The recorded narration measures {vo_total:.0f} s (≈ {1089/(vo_total/60):.0f} wpm incl. pauses; the plan assumed 145 wpm ≈ {est_total:.0f} s). With every visual beat in the script the picture is ≈ {int(total//60)}:{int(total%60):02d} (+3.2 s outro + end screen ≈ 8:40–8:50 delivered). Reaching 9:30 would need ≈ {570-total:.0f} s more: options are (a) re-time the processed VO with small inter-sentence gaps (free, ffmpeg, Voice and Sound agent), (b) longer visual holds in the quiet-hour sequences (risk: drag), (c) a script addition (Storywriter). Padding was **not** added here. The script's section timecodes (Act I to 3:50, Ending at 10:00) are also optimistic: Act I now ends ≈ 2:40.",
  "**Shot timing inside long narration files is estimated.** N02_act1 (112.5 s) and N03_act2 (123.9 s) are single files; shot cuts were placed by word share. Before assembly, re-time cuts to real line onsets (e.g. silence detection on the processed WAVs).",
  f"**Act II is the longest stretch (≈ {(sec[A2]+sec[N2])/60:.1f} min incl. the second night; {sec[A2]:.0f} s before the second night) and is mostly exposition** (library tapes + porch + radio flashback with no threat on screen). Retention risk in the 3:30–5:15 window. Option: trim L029/L030 (radio backstory) by a sentence each, or move one tape (1996) out.",
  "**'I want that on the record' (L015) is unclear in a cut.** It reads as a podcast aside; fine, but it is the only line that addresses an audience inside the story before the twist. Keep it consistent with the ending reveal (good set-up) — just confirm it is intentional.",
  "**Act III notepad scene has no narration for ≈ 12.5 s** (four pages, S080–S083). Pages must be readable (≈ 2.5–3 s each); this is deliberate, but it is the longest visual-only stretch after the cold open. Confirm it is wanted, or let NARR read one page.",
  "**Geography gap:** 'the radio behind the counter' (L044) is first seen in Act III. It should be planted earlier: storyboard dresses it into BG02A from Act I (S022/S026 background) so the ending pays off.",
  "**Ines's flat (Ending)** has no set-up line; the audience must infer 'above the diner'. Suggest an establishing exterior beat (re-use BG06A with a lit upstairs window) if a 2–3 s shot can be afforded.",
  "**The tower light is never explained in Act I** (blinks in S005/S029) and the radio-station backstory lands in Act II. Good mystery set-up; no change, noted for QC so the blinks are not removed as 'decoration'.",
  "**Held 4 s silence (S091) and the 1:00 hard cuts** are true silence. QC tools that flag dropouts must whitelist these timestamps.",
  "**Day scenes have no Environment Bible lighting preset** (main street day, library, porch, diner morning; marked DAY*). Environment Bible owner should add one (suggest: overcast Bone key, Ash-Violet shadow, lowered saturation) so the town is 'friendly but wrong'.",
  "**Assembler gaps (scripts/production/assemble.py):** (a) no video layers, so hero clips cannot be placed yet; each hero shot carries a still-layer fallback. (b) `static` is not a named move; it works because unknown moves fall through to no motion. (c) Caption key matching strips only `.,!?`, so keys next to '…' or apostrophes must be written exactly (e.g. key `…ffee…`). (d) The YouTube end screen (10–20 s) must follow the outro; the assembler appends the outro last, so the end-screen plate needs a separate step.",
  "**No `episodes/EP001/manifest.json` exists yet**, so the shots could not be written into the manifest or `pipeline.storyboard.status` set; they are in `shots_draft.json` for the owner of the manifest to merge.",
  "**Character sheets for Cal, Ines, the motel owner, the attendant and the old woman do not exist yet** (CHARACTER_BIBLE requires approved sheets before any Flow generation). Hero clips H03–H06, H08, H09, H11 are blocked on them.",
  "**Originality:** storyboard keeps the radio station to three short flashback shots (S052–S054) and no DJ character, as the script notes require (distance from *Pontypool*).",
], 1):
    A(f"{n}. {t}")

(EP / "storyboard.md").write_text("\n".join(md) + "\n")
print(f"shots={len(out)} total={total:.1f}s ({total/60:.2f} min) vo_est={vo_total:.0f}s heroes={heroes_used} bgs={bgs_used}")
for k, v in sec.items():
    print(f"  {k}: {v:.1f}")
