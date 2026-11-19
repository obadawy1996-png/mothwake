#!/usr/bin/env bash
# Rebuild processed/ from vo/*.mp3 (ElevenLabs takes). Deterministic; no credits used.
set -e; cd "$(dirname "$0")"; mkdir -p processed; P=processed
WALL="aresample=48000,asetrate=48000*0.96,aresample=48000,lowpass=f=1600,highpass=f=180,aecho=0.8:0.6:60|140:0.35|0.2"
TAPE="aresample=48000,highpass=f=300,lowpass=f=3800,vibrato=f=0.7:d=0.15,acrusher=bits=10:mix=0.25"
RADIO="aresample=48000,highpass=f=250,lowpass=f=4200,acompressor=threshold=0.1:ratio=4"
PHONE="aresample=48000,highpass=f=300,lowpass=f=3400"
run(){ ffmpeg -y -loglevel error -i vo/$1.mp3 -af "$2,loudnorm=I=$3:TP=-3:LRA=11" -ar 48000 -c:a pcm_s24le $P/$1.wav; }
tape(){ ffmpeg -y -loglevel error -i vo/$1.mp3 -f lavfi -t 8 -i "anoisesrc=color=pink:amplitude=0.012:r=48000" \
  -filter_complex "[0:a]$TAPE[v];[1:a]aformat=channel_layouts=mono[n];[v][n]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-24:TP=-3:LRA=11" \
  -ar 48000 -c:a pcm_s24le $P/$1.wav; }
run ECHO_coffee "$WALL" -30; run ECHO_night2_window "$WALL" -24; run ECHO_wall_intro "$WALL" -24
run ECHO_voicemail "$PHONE" -24; run ECHO_ending_radio "$RADIO" -20
for f in VISITOR_1974 ECHO_tape1981 ECHO_tape1996 ECHO_tape2009; do tape $f; done
for f in S00_coldopen N02_act1 N03_act2 N04_night2 N05_act3 CAL_onmic; do run $f "aresample=48000,highpass=f=70" -18; done
echo "processed: $(ls $P | wc -l) files"
