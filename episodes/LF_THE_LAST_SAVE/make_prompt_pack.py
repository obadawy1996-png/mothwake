"""Builds FLOW_PROMPT_PACK.md: 40 copy-paste Flow prompts for THE LAST SAVE (owner-run, 16:9)."""
from pathlib import Path

P = ("MOTHWAKE style. Dark 2D hand-drawn animation, flat cel shading with only two tones per surface (base and shadow) "
     "and one soft warm rim light from the single light source in the scene. Strictly limited palette: near-black obsidian, "
     "charcoal, muted ash violet, dull old gold, bone white, and one warm lamp-yellow light. Cool ash-violet darkness surrounds "
     "one warm pool of light. Painted flat backgrounds with no outlines and soft simplified edges away from the focal point; "
     "characters drawn with a thin dark charcoal line. Small warm lamp-coloured highlights in every eye. Quiet, still, "
     "atmospheric night. Restrained motion, slow camera. 16:9 widescreen cinematic frame, rule-of-thirds composition. ")
A = (" Audio: quiet room tone only, no speech, no voices, no music. Avoid: photorealism, 3D render, CGI, glossy plastic look, "
     "anime, chibi, bright or saturated colours, neon, multiple coloured light sources, heavy lens flare, blood, gore, wounds, "
     "corpses, monsters with faces, teeth or claws, text, letters, numbers, words, captions, subtitles, signage lettering, "
     "logos, brand names, watermarks, readable screens, game interface, extra fingers, distorted hands, people speaking or "
     "moving their lips, camera shake, fast cuts.")
J = "Jun, a lanky 15-year-old boy with the hood of a dark charcoal hoodie up, lime-green hoodie cords, short black hair"
I = "Ivy, a woman of 27 with a tired kind face, dark brown hair in a low loose bun, a long rust-red knitted scarf, a charcoal jumper"
T = "shown on a TV screen in a soft flat painted daylight style, washed out like an old TV picture"
BOY, WOM, LNG = "Character turnaround sheet of boy", "Woman character turnaround sheet", "Apartment living room at night"
COR, SEA, APT = "Empty corridor at night", "Seaside town illustration", "Apartment block glowing at night"
PRK, MTH, BED, TAL = "Car park behind apartment building", "Moth resting on window frame", "Empty bedroom at night", "Tall figure standing in doorway"

S = [
 ("01", "Lite", [LNG, COR], f"A dark, cluttered living room at night lit only by a large TV. On the TV screen, {T}: the inside of an apartment hallway with one closed wooden door and a warm light under it, perfectly still. The room is empty; a game controller lies on the sofa. Camera very slow push-in toward the screen."),
 ("02", "Lite", [SEA], "A wide establishing view, soft flat painted daylight style washed out like an old TV picture: a sunny seaside town with a curving coastal road, palm trees, pastel houses, a pier and a calm sea under a hazy sun. A small plain grey apartment block stands far off at the edge of town. Slow lateral pan. No people, no cars."),
 ("03", "Lite", [SEA], "Soft flat painted daylight style washed out like an old TV picture: the camera glides forward along an empty sunny coastal road lined with palm trees past pastel houses and a beach, like a game character driving. No people, no cars."),
 ("04", "Lite", [COR, SEA], "Soft flat painted style washed out like an old TV picture: a game version of an old apartment hallway at night, one closed wooden door at the end with a warm line of light under it. Camera slowly pushes toward the door. No people."),
 ("05", "Lite", [APT, PRK], "Wide exterior at night: an old grey brick apartment block above a small wet car park, a dead streetlamp, all windows dark except one warm lit window on the third floor. Mist. Camera locked off, slow push-in."),
 ("06", "Lite", [BOY, LNG], f"Wide shot of a cluttered living room at midnight lit only by a large warm TV. {J}, sits alone on the worn sofa holding a controller, small in the frame, the glow flickering over him. Nobody else in the frame. Camera locked off."),
 ("07", "Lite", [WOM, BED], f"A dark bedroom at night. {I}, lies awake in bed on her side, eyes open, listening to the wall beside her bed, where faint flickering TV light leaks through a gap near the skirting board. Camera locked off."),
 ("08", "Lite", [BOY, COR], f"A dim old apartment stairwell at night with one warm light on the landing. {J}, alone, runs up the stairs two at a time, excited, holding a small plain paper shopping bag. Nobody else. Camera low, locked off."),
 ("09", "Lite", [SEA, LNG], f"Close on a glowing TV in a dark room. On screen, {T}: a sunny postcard view of a seaside town with palm trees; the camera slowly pushes into the corner of the picture where one plain grey apartment block stands."),
 ("10", "Fast", [SEA, TAL], "Key moment. Soft flat painted daylight style washed out like an old TV picture: one lit third-floor window in a grey brick apartment block among palm trees. Inside the warm window a tall, thin, featureless dark silhouette stands perfectly still, facing out. The image flickers like a TV glitch; it is still there. Camera locked off."),
 ("11", "Lite", [BOY, LNG], f"Medium close shot in a dark living room: {J}, alone, leans toward the glowing TV, controller in hand, eyes searching, warm light flickering across his face. Camera locked off."),
 ("12", "Lite", [SEA, LNG], f"Close on a glowing TV in a dark room. On screen, {T}, but at night: a plain white car with nobody inside drives slowly along a coastal road lined with palms and stops, engine idling, empty driver seat."),
 ("13", "Lite", [WOM, PRK], f"Inside a dark flat at night: {I}, stands at her window in pyjamas, one hand on the cold glass, looking down at the car park below with worry. Seen from behind her shoulder. Camera locked off."),
 ("14", "Lite", [PRK, APT], "High angle down at a small wet car park behind an old apartment block at night, a tall dead unlit streetlamp, puddles, mist, one empty bay below the lamp. No people. Slow tilt down."),
 ("15", "Fast", [PRK], "Key moment. Wide shot of a small wet car park at night under a tall dead streetlamp. A plain white car idles in the bay below it, headlights on, exhaust curling, interior light glowing, driver seat empty, nobody anywhere. Mist drifts. Camera locked off, slow push-in."),
 ("16", "Lite", [PRK], "Grey dawn over a small wet car park behind an old apartment block. Under the dead streetlamp, an empty parking bay; in it a perfectly dry rectangle the exact shape of a car on otherwise wet tarmac. No people. Camera slowly tilts down."),
 ("17", "Lite", [BOY, LNG], f"A dark living room at night lit by the TV: {J}, alone, sits on the floor against the sofa writing carefully in a small notepad, glancing up at the screen between lines. The page shows only scribbled lines. Camera locked off."),
 ("18", "Lite", [LNG], "Extreme close-up of a small notepad on a sofa cushion at night, warm TV glow, a pencil beside it, the page filled with neat scribbled lines that cannot be read. Camera slow push-in."),
 ("19", "Lite", [BOY, LNG], f"Medium shot in a dark living room: {J}, alone on the sofa, fights sleep, eyelids drooping, jerking awake once, the controller slowly slipping from his fingers. Camera locked off."),
 ("20", "Lite", [SEA, LNG], f"Close on a glowing TV. On screen, {T}: in a sunny pastel street small faceless townspeople walk slowly, never running; one presses a light switch on a wall once and walks on."),
 ("21", "Lite", [SEA], "Soft flat painted style washed out like an old TV picture: a pastel street at dusk with small faceless townspeople. The streetlights all go out at once and every townsperson freezes perfectly still mid-step. Camera locked off."),
 ("22", "Fast", [SEA, LNG], f"Key moment. Close on a glowing TV in a dark room. On screen, {T}: a street full of small faceless townspeople standing still; one by one they slowly turn their blank heads to face out of the screen, toward the viewer. Camera slow push-in."),
 ("23", "Lite", [SEA, LNG], f"Close on a glowing TV in a dark room. On screen, {T}: the front door of a little pastel house at dusk, a small faceless figure waiting on the step, and two blank glowing rounded panels side by side, gold and grey, waiting for a choice."),
 ("24", "Lite", [BOY, LNG], f"Close shot in a dark room lit by TV glow: the hands of {J} on a game controller, his thumb hovering over one button, trembling, not pressing. Camera locked off."),
 ("25", "Lite", [LNG, COR], "Inside a dark apartment at night: the plain wooden front door, chained, a warm line of hallway light under it, a tiny glowing peephole. The door shudders as someone knocks three slow times, pauses, then three more. No people visible. Camera locked off."),
 ("26", "Lite", [WOM, COR], f"A dim apartment landing at night with one warm ceiling light. {I}, stands alone by her own door in pyjamas, frozen, staring down the hall toward a neighbour's closed door. Camera locked off."),
 ("27", "Lite", [COR], "Low close shot along an apartment hallway floor at night: the warm line of light under a closed door, and in it the shadow of two feet standing still on the other side. Nobody is visible. Camera locked off at floor level."),
 ("28", "Lite", [BOY, LNG], f"Wide shot of a dark apartment: {J}, alone, stands frozen between the glowing TV and the closed front door, controller in his hand. Behind him the window slowly turns from black to grey dawn. Camera locked off."),
 ("29", "Fast", [SEA, LNG], f"Key moment. Close on a glowing TV. On screen, {T}: a sunny coastal road at sunset; the sun sinks fast, and the tall palm trees along the road slowly straighten and harden into tall dark streetlamps, one after another. Camera locked off."),
 ("30", "Lite", [SEA], "Soft flat painted daylight style washed out like an old TV picture: an empty sunny coastal road past the last houses and the pier toward the edge of the world, where the scenery simply stops and fades into a flat pale grey void. The camera glides forward. No people."),
 ("31", "Lite", [SEA, APT], "Soft flat painted style: at the edge of a sunny game world fading into grey void stands one plain grey brick apartment block alone; the sky darkens to night as the camera approaches; one warm window on the third floor. No people. Slow push-in."),
 ("32", "Lite", [SEA, MTH], "Close shot, soft flat painted style: a warm-lit third-floor window in a grey brick wall at dusk; a small moth with old-gold wings and eye-spots rests on the ledge, wings slowly opening and closing. No people. Gentle push-in."),
 ("33", "Fast", [BOY, LNG, MTH], f"Key moment. Wide shot of a dark living room lit only by a large glowing TV. A real moth with old-gold wings flutters out of the dark and lands on the bright screen. In the foreground {J}, alone on the sofa, slowly leans back, controller lowering, staring at it. Camera locked off."),
 ("34", "Lite", [BOY, LNG], f"Pale grey morning light in a cluttered living room. {J}, alone, lies deeply asleep on the sofa, peaceful, the controller still held loosely in both hands, the TV still glowing softly. Camera slow push-in."),
 ("35", "Lite", [LNG], "Extreme close-up in a dim room: the small standby light on a games console glowing steadily, a cable, the soft glow of a TV reflected on the cabinet. No people. Camera locked off."),
 ("36", "Lite", [WOM, LNG], f"A dim living room in pale morning light. {I}, alone, sits cross-legged on the floor in front of the glowing TV holding a game controller, hesitates, then presses one button. Camera locked off."),
 ("37", "Lite", [COR, LNG], f"Close on a glowing TV in a dim room. On screen, {T}: a game version of an old apartment hallway with a warm ceiling light and a closed wooden door. Camera slow push-in."),
 ("38", "Lite", [COR, SEA], "Soft flat painted style washed out like an old TV picture: in an apartment hallway, a small game character in a dark hoodie with lime-green cords stands with his back to us in front of a closed door, perfectly still, waiting. Camera locked off."),
 ("39", "Fast", [COR, APT], "Key moment. Inside a dark flat at night: a plain wooden front door, a warm line of hallway light under it. It shudders with three slow knocks, a pause, then three more, and a shadow of two feet appears in the line of light. No people visible. Camera locked off, slow push-in."),
 ("40", "Lite", [WOM, LNG], f"Close-up in a dim room lit by TV glow: {I}, holding a game controller, slowly turns her head from the screen toward the front door off-screen, her face caught between fear and decision. Camera locked off."),
]

out = ["# THE LAST SAVE: Flow prompt pack (run by the owner, 16:9)", "",
       "Settings: Video · Ingredients · **16:9** · x1 · Veo 3.1 Lite (Fast where marked). Add the listed ingredients from the picker, paste the prompt, press Generate once.",
       f"Total: {len(S)} clips = {sum(10 if m == 'Lite' else 20 for _, m, _, _ in S)} credits. Download them all and tell me; I identify each clip by its frames, then edit and finish the film.", ""]
for n, m, ing, txt in S:
    out += [f"## {n} · {m} · ingredients: {' + '.join(ing)}", "```", P + txt + A, "```", ""]
Path(__file__).with_name("FLOW_PROMPT_PACK.md").write_text("\n".join(out), encoding="utf-8")
print(len(S), "prompts written")
