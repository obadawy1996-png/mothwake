"""FIVE MOTHS: builds the owner-run Flow pack (5 refs + 36 clips) as Markdown and a local copy-button page."""
import html, json
from pathlib import Path

HERE = Path(__file__).parent
STYLE = ("MOTHWAKE style. Dark 2D hand-drawn animation, flat cel shading with only two tones per surface (base and shadow) "
         "and one soft warm rim light from the single light source in the scene. Strictly limited palette: near-black obsidian, "
         "charcoal, muted ash violet, dull old gold, bone white, and one warm lamp-yellow light. Cool ash-violet darkness surrounds "
         "one warm pool of light. Painted flat backgrounds with no outlines and soft simplified edges away from the focal point; "
         "characters drawn with a thin dark charcoal line. Small warm lamp-coloured highlights in every eye. Quiet, still, "
         "atmospheric night. Restrained motion, slow camera. 16:9 widescreen cinematic frame, rule-of-thirds composition. ")
AVOID = (" Audio: quiet room tone only, no speech, no voices, no music. Avoid: photorealism, 3D render, CGI, glossy plastic look, "
         "anime, chibi, bright or saturated colours, neon, multiple coloured light sources, heavy lens flare, blood, gore, "
         "weapons, wounds, corpses, monsters with faces, teeth or claws, text, letters, numbers, words, captions, subtitles, "
         "signage lettering, logos, brand names, watermarks, readable screens, extra fingers, distorted hands, people speaking "
         "or moving their lips, camera shake, fast cuts.")
REF_AVOID = (" Avoid: photorealism, 3D render, CGI, anime, chibi, bright or saturated colours, neon, text, letters, numbers, "
             "words, signage lettering, logos, watermarks, extra fingers, distorted hands.")
RAE = "Rae, a woman of 31 with cropped dark hair, a mustard bomber jacket and fingerless gloves, quiet tired eyes"
DEZ = "Dez, a man of 33 in a loose grey suit jacket over a white T-shirt, a gold ring, an easy grin"
IVY = ("Ivy, a woman of 27 with a tired kind face, dark brown hair in a low loose bun, a long rust-red knitted scarf "
       "over a plain grey petrol-station tabard")
RES = "silent ordinary residents in dressing gowns and slippers, faces in soft shadow"

REFS = [
 ("R1", "REF-RAE", f"Character turnaround sheet on a plain dark charcoal background: {RAE}, shown four times at the same scale: front, three-quarter, side and back view, standing, mouth closed. No labels."),
 ("R2", "REF-DEZ", f"Character turnaround sheet on a plain dark charcoal background: {DEZ}, shown four times at the same scale: front, three-quarter, side and back view, standing, mouth closed. No labels."),
 ("R3", "REF-COAST-ROAD", "Environment reference, no people: a palm-lined two-lane coast road at night beside a dark calm sea in a sleepy seaside town; tall streetlamps, a few unlit; low pastel bungalows with dark windows; a long low bridge over the water in the distance; one warm light far ahead. Cool ash-violet darkness."),
 ("R4", "REF-PETROL-STATION", "Environment reference, no people: a small all-night petrol station on a coast road at night. One warm canopy light over two pumps, a small shop with a counter, a tea urn and a chocolate rack visible through the big window, palm trees, the dark sea behind. Everything else in cool ash-violet darkness."),
 ("R5", "REF-MOTEL-CAR", "Environment reference, no people: a low roadside motel at night with a row of identical doors and one warm lamp; parked in front, a plain white estate car with its driver door open and keys in the ignition. Palms, mist, dark sky."),
]
# (n, chapter, model, ingredients, prompt)
S = [
 (1, "Cold open", "Lite", "R4 + R5", "Wide shot of a small all-night petrol station on a dark coast road. Under the one warm canopy light a plain white estate car idles at the second pump, headlights on, exhaust curling. Nobody inside it, nobody anywhere. Very slow push-in."),
 (2, "Cold open", "Lite", "R5 + moth ref", "Close shot of the windscreen of an idling white estate car at night under a warm canopy light: four small moths with old-gold wings sit perfectly still on the glass while the car body trembles gently with the engine. Camera locked off."),
 (3, "Cold open", "Lite", "Ivy ref + R4", f"Inside a small petrol station shop at night: {IVY}, stands alone behind the counter, looking out through the big window at a car waiting at the pumps, still and wary. Warm counter light. Camera locked off."),
 (4, "I One last job", "Lite", "R3", "Wide night shot of a low beach casino by a dark sea, palm trees swaying slowly, all dark except one warm office window on the side facing the water. No people. Slow push-in."),
 (5, "I One last job", "Lite", "R1 + R2", f"A dark back corridor at night: {RAE}, and {DEZ}, move quietly side by side toward a door at the end, Dez grinning, Rae watchful. One warm light far ahead. Camera tracking slowly behind them."),
 (6, "I One last job", "Lite", "R3", "A dark office at night with a window onto a moonlit sea. The heavy door of a small wall safe swings slowly open by itself, a little warm light spilling out. Waves glitter outside. No people. Camera locked off."),
 (7, "I One last job", "Lite", "R2", f"Close shot in a dark office: {DEZ}, grinning, quickly fills a plain canvas bag with bundles of paper from an open safe, then zips it shut. Camera locked off."),
 (8, "I One last job", "Lite", "R3", "A plain dark car speeds along a palm-lined coast road at night beside the sea, its headlights sweeping the trunks of the palms, streetlamps passing overhead. Camera tracking alongside."),
 (9, "I One last job", "Fast", "R1 + moth ref", f"Key moment. From inside a moving car at night: {RAE}, drives with both hands on the wheel, staring ahead in disbelief. On the outside of the windscreen, right in front of her eyes, a small moth with old-gold wings sits perfectly still while the night wind and streetlamps rush past around it. Camera locked off inside the car."),
 (10, "II Two", "Lite", "R5 + R1 + R2", f"A low roadside motel at night. {RAE}, and {DEZ}, walk quickly away from a dark car to a plain white estate car with its door open, Dez carrying a canvas bag. One warm motel lamp. Camera locked off."),
 (11, "II Two", "Lite", "R1 + R2 + R5", f"Inside a white estate car driving at night, seen from the back seat: {RAE}, at the wheel and {DEZ}, in the passenger seat, windows up, dashboard glowing warm, the dark coast road ahead. Camera locked off."),
 (12, "II Two", "Lite", "moth ref + R5", "Extreme close shot of a car windscreen at night from inside: one small old-gold moth sits on the inside of the glass, and directly opposite it on the outside, another identical moth, both perfectly still, the dark road rushing past behind them. Camera locked off."),
 (13, "II Two", "Lite", "R1 + R2", f"Close shot of a car dashboard at night: the hand of {DEZ} turns on the small glowing radio, then the gloved hand of {RAE} reaches in and switches it off. The radio's warm dial light stays on. Camera locked off."),
 (14, "II Two", "Fast", "R5", "Key moment. Extreme close shot of an old car radio at night: it has been switched off, yet its warm dial light keeps glowing and the tuning needle slowly drifts on its own across the dial. No hands, no people. Camera slow push-in."),
 (15, "III Rules", "Lite", "Ivy ref + R4", f"Inside a small petrol station shop at night: {IVY}, alone, fills a tea urn at the counter and glances at the dark window, calm, as if she has seen this night before. Warm counter light. Camera locked off."),
 (16, "III Rules", "Lite", "R3", "A palm-lined coast road at night lit by a long line of tall warm streetlamps receding into the distance beside the dark sea. Empty, still. Camera slowly drifting forward."),
 (17, "III Rules", "Lite", "R3", "A long low bridge over black water at three in the morning. A single car crosses it slowly, its headlights the only moving light, mist on the water. Wide shot, camera locked off."),
 (18, "III Rules", "Fast", "R3", "Key moment. Seen from behind a car driving away along a coast road at night: the tall streetlamps behind it go out one by one, in order, following the car, until only darkness is left behind it. Camera tracking from behind."),
 (19, "III Rules", "Lite", "moth ref + R5", "Close shot of a car windscreen from inside at night: three small old-gold moths now sit perfectly still on the glass, dark road beyond. Camera locked off, slow push-in."),
 (20, "IV The town wakes", "Lite", "R3", "A quiet street of low pastel bungalows and palms at half past three in the morning, all dark. A car's headlights pass, and as it goes by, the house windows light up warm one after another in a wave following it. Wide shot, camera locked off."),
 (21, "IV The town wakes", "Lite", "R3", f"Several lit bungalow windows at night, and in each window stands one of the {RES}, perfectly still, watching the road. Slow lateral pan."),
 (22, "IV The town wakes", "Lite", "R1", f"Close shot through a car side window at night: {RAE}, driving, turns her head slowly to look at the lit windows passing outside, her face pale with dread in the warm flicker. Camera locked off."),
 (23, "IV The town wakes", "Fast", "R3", f"Key moment. A small bus stop on a dark palm-lined road at night under one streetlamp. An old man, one of the {RES}, stands there alone and slowly raises one hand in a kind neighbourly wave as headlights sweep past him. Camera locked off."),
 (24, "IV The town wakes", "Lite", "moth ref + R4", "From inside a car at night: four small old-gold moths sit on the windscreen, and ahead on the dark coast road a small petrol station glows warm under its canopy, getting closer. Camera slowly pushing forward."),
 (25, "V Pump two", "Lite", "R4 + R5", "A plain white estate car slowly pulls in under the warm canopy light of a small petrol station at night and stops at the second pump, engine running. No people visible. Camera locked off."),
 (26, "V Pump two", "Lite", "R1 + R4", f"{RAE}, gets out of a white estate car at a petrol pump at night and walks alone toward the warm shop door, hands in her jacket pockets, small moths clinging to her sleeve. Camera locked off."),
 (27, "V Pump two", "Lite", "Ivy ref + R4", f"Inside a small petrol station shop at night: {IVY}, alone behind the counter, quietly pours hot water from a tea urn into a paper cup and slides it across the counter, kind and calm. Warm light. Camera locked off."),
 (28, "V Pump two", "Lite", "R1 + R4", f"Inside a small petrol station shop at night: {RAE}, stands alone at the counter staring down at three small old-gold moths resting on her jacket sleeve, exhausted, a paper cup of tea in front of her. Camera locked off."),
 (29, "V Pump two", "Lite", "R1", f"Close shot: the gloved hand of {RAE} hovers over the open purse in her jacket pocket, hesitating, about to take it out. Warm shop light. Camera locked off."),
 (30, "V Pump two", "Lite", "R2 + R5", f"Outside a petrol station at night: {DEZ}, sits alone in the passenger seat of a white estate car, impatient, leaning across to press the horn hard, the canvas bag on his lap. Camera locked off."),
 (31, "V Pump two", "Fast", "R1 + R4", f"Key moment. Inside a petrol station shop at night: {RAE}, takes a chocolate bar from a rack, slips it into her pocket without paying and walks to the door; as she pushes it open, a fifth small old-gold moth lands softly on the back of her hand. Camera locked off."),
 (32, "VI The last pull-in", "Lite", "Ivy ref + R4", f"Inside a small petrol station shop at night: {IVY}, alone behind the counter, slowly looks up from her tea toward the window, where a white car still waits at the pump outside. Camera locked off, slow push-in."),
 (33, "VI The last pull-in", "Lite", "R4 + R5", "A plain white estate car idles alone at the second pump of a petrol station at night, headlights on, its radio light glowing inside, doors closed, nobody in it. Camera slowly circling."),
 (34, "VI The last pull-in", "Lite", "R5 + moth ref", "Close shot inside an empty idling car at night: on each of the two empty front seats sits one small moth with old-gold wings, perfectly still, the dashboard glowing warm. Camera locked off."),
 (35, "VI The last pull-in", "Fast", "R5", f"Key moment. A car rear-view mirror at night, filling the frame: reflected in it, the back seat is full of {RES}, sitting very straight and calm with hands in their laps, and an empty space for two in the middle. Camera slow push-in on the mirror."),
 (36, "VI The last pull-in", "Lite", "R3 + R4", "Final wide shot: a small petrol station glowing alone on a dark palm-lined coast road beside the sea at night, a white car still idling at the second pump. The camera slowly pulls back and up until the station is a tiny warm light in the dark."),
]

def ref_prompt(p):
    return ("MOTHWAKE style. Dark 2D hand-drawn animation, flat cel shading, limited palette of near-black obsidian, charcoal, "
            "muted ash violet, dull old gold, bone white and one warm lamp-yellow light; thin dark charcoal line on characters. "
            "16:9 frame. " + p + REF_AVOID)

total = sum(10 if m == "Lite" else 20 for *_, m, _, _ in [(a, b, c, d, e) for a, b, c, d, e in S])
md = ["# FIVE MOTHS: Flow pack (run by the owner)", "",
      "**Step 1, references (Image mode · Nano Banana · 16:9 · x1, 0 credits).** Generate R1–R5, then use them as ingredients below. Also use the existing *Woman character turnaround sheet* (Ivy) and *Moth resting on window frame*.",
      f"**Step 2, clips (Video · Ingredients · 16:9 · x1).** Lite 10 / Fast 20 credits → {len(S)} clips = **{total} credits**. Click Generate once per clip.",
      "**Step 3.** Leave everything in Downloads and tell me. I identify each clip by its frames, then edit, mix, subtitle and QC the film.", ""]
for code, name, p in REFS:
    md += [f"## {code} · {name} (image)", "```", ref_prompt(p), "```", ""]
for n, ch, m, ing, p in S:
    md += [f"## {n:02d} · {ch} · {m} · ingredients: {ing}", "```", STYLE + p + AVOID, "```", ""]
(HERE / "FLOW_PROMPT_PACK.md").write_text("\n".join(md), encoding="utf-8")

items = [{"id": c, "title": f"{c} · {nm} · image · 0 credits", "ing": "none", "text": ref_prompt(p)} for c, nm, p in REFS]
items += [{"id": f"{n:02d}", "title": f"{n:02d} · {ch} · {m} ({10 if m == 'Lite' else 20})", "ing": ing,
           "text": STYLE + p + AVOID} for n, ch, m, ing, p in S]
page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Five Moths Flow Run</title><style>
:root{--bg:#090A0D;--card:#25232B;--muted:#77717D;--gold:#B89A68;--text:#E7E2D8}
body{margin:0;background:var(--bg);color:var(--text);font:15px/1.5 system-ui,sans-serif}
header{position:sticky;top:0;background:var(--bg);padding:14px 16px;border-bottom:1px solid #333;z-index:2}
h1{margin:0;font-size:18px;color:var(--gold)} #prog{color:var(--muted);font-size:13px}
main{max-width:860px;margin:0 auto;padding:12px 16px 60px}
.c{background:var(--card);border-radius:10px;padding:12px 14px;margin:10px 0}.c.done{opacity:.45}
.t{font-weight:600}.i{color:var(--muted);font-size:13px;margin:2px 0 8px}
pre{white-space:pre-wrap;font-size:12px;color:#cfc8bb;max-height:4.5em;overflow:hidden;margin:0 0 8px}
button{background:var(--gold);color:#090A0D;border:0;border-radius:6px;padding:7px 14px;font-weight:600;cursor:pointer}
label{margin-left:12px;color:var(--muted);font-size:13px}</style></head><body>
<header><h1>FIVE MOTHS · Flow run</h1><div id="prog"></div></header><main id="list"></main>
<script>
const ITEMS=__ITEMS__;let done={};try{done=JSON.parse(localStorage.getItem('fm_done')||'{}')}catch(e){}
function save(){try{localStorage.setItem('fm_done',JSON.stringify(done))}catch(e){}}
function prog(){const n=ITEMS.filter(x=>done[x.id]).length;document.getElementById('prog').textContent=n+' of '+ITEMS.length+' done · 5 refs first, then 36 clips (16:9, x1, click Generate once)'}
const L=document.getElementById('list');
ITEMS.forEach(x=>{const d=document.createElement('div');d.className='c'+(done[x.id]?' done':'');
d.innerHTML='<div class="t"></div><div class="i"></div><pre></pre><button>Copy prompt</button><label><input type="checkbox"> done</label>';
d.querySelector('.t').textContent=x.title;d.querySelector('.i').textContent='Ingredients: '+x.ing;d.querySelector('pre').textContent=x.text;
const b=d.querySelector('button'),cb=d.querySelector('input');cb.checked=!!done[x.id];
b.onclick=async()=>{try{await navigator.clipboard.writeText(x.text)}catch(e){const t=document.createElement('textarea');t.value=x.text;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove()}b.textContent='Copied ✓';setTimeout(()=>b.textContent='Copy prompt',1500)};
cb.onchange=()=>{done[x.id]=cb.checked;d.classList.toggle('done',cb.checked);save();prog()};L.appendChild(d)});prog();
</script></body></html>""".replace("__ITEMS__", json.dumps(items))
(HERE / "FIVE_MOTHS_FLOW_RUN.html").write_text(page, encoding="utf-8")
print(len(REFS), "refs,", len(S), "clips,", total, "credits")
