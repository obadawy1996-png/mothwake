# PILOT_01 — narration and voice shortlist

**Status:** 2026-11-20. Fix 3: voices are chosen by the owner **before** any narration is generated. Nothing has been generated or spent.
**Estimate:** about 930 ElevenLabs credits for all three Shorts (plan figure; about 1 credit per character on EP001).

## Who speaks
| Short | Ivy (first-person narrator) | Theo (child, 7) |
|---|---|---|
| SH012 Rain Sounds | All lines (37 words) | — |
| SH019 Theo's Nightlight Rules | Narration | The three rules and "Now they'll look at you." (whispered) |
| SH025 Part 1 | All lines | — |

## Ivy: shortlist (ElevenLabs library, listen to the previews)
| Option | Voice | Why | Preview |
|---|---|---|---|
| A (recommended) | **Ana-Rita2** `wJqPPQ618aTW29mptyoc` | Young British, soft and expressive, built for book narration. It fits the Vesper Court setting. | https://storage.googleapis.com/eleven-public-prod/JSdwiNguB8ejxX5k1f64Z6aLdP73/voices/wJqPPQ618aTW29mptyoc/7f5d3985-6999-49c4-8c53-e0f43ef5a334.mp3 |
| B | **Ophelia Rose** `FA6HhUjVbervLw2rNl8M` | Calm, soothing British. Quieter, more "bedtime". | https://storage.googleapis.com/eleven-public-prod/custom/voices/FA6HhUjVbervLw2rNl8M/7S9eyCKsvFIEyj8B5qmI.mp3 |
| C | **JANE DOE** `SaqYcK3ZpDKBAImA8AdW` | Young warm American, intimate story voice, if an American narrator suits the US audience better. | (preview in the ElevenLabs library) |

## Theo: the library has almost no natural child voices
The only match is **Teddy Twinkle** `XjGYkUkzth8BPs29fmcV`, a cheerful cartoon boy. That's too bright for a whispered horror line.
**Recommendation:** design Theo with ElevenLabs Voice Design, using this description: *"A quiet, serious seven-year-old British boy, small and breathy voice, speaks slowly and carefully as if telling a secret, no cartoon exaggeration."* Voice Design makes previews to pick from. Its credit cost is shown before it runs, and it needs the owner's OK.

## Lines (pilot versions)
**SH012:** "I sleep to rain sounds. Last night I paused them." · "I paused it." · "The rain outside stopped." · "Play. Rain. Pause. Nothing." · "Only my window was wet." · "This time the tapping didn't stop." · "It was never a recording."
**SH019:** IVY "Theo has three rules about his nightlight." · THEO "One: it stays on." · THEO "Two: if it flickers, look at me. Not it." · THEO "Three: if it goes out, never turn on the big light." · IVY "I'm the grown-up. I turned it on." · IVY "They were all facing the nightlight. Like moths." · IVY "It wasn't for Theo. It kept them looking at it." · THEO (whisper) "Now they'll look at you."
**SH025 Part 1:** "Normal evening. Bike, keys, shopping." · "Two doors say nine. Only one is mine." · "Which do I open? Decide now."

**Open point:** SH019 calls Theo "my little brother" in the test title, but the Asset Kit says he is Ivy's nephew. The lines above work for both. Pick one before the title is final.

## Generated 2026-11-20 (owner chose Ivy = Ana-Rita2)
ElevenLabs flow `kdSu925On1uAvgqQLTO7` "MOTHWAKE PILOT_01 narration", model eleven_v4, **1 take each** to stay inside the approved ~930 budget (the default 2 takes would have cost about 1,500).
| Node | Short | Lines | Credits (measured, ElevenLabs result) |
|---|---|---|---|
| IfkrDVYGAMu1SWlkFQsz | SH012 | all Ivy lines | 313 |
| cDyzYHmh4Jof3c4kpxdy | SH019 | Ivy lines only (Theo pending his voice) | 260 |
| kun0LRSTTLRnyaVmYdmq | SH025 P1 | all Ivy lines | 167 |
| | **Total** | | **740** (about 190 left of the pilot's ~930 estimate, for Theo and retakes) |
Takes still to be downloaded to `episodes/PILOT_01/audio/vo/` and reviewed by ear. They're cut into lines in post.
