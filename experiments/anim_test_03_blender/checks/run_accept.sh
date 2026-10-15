#!/bin/bash
# checks/run_accept.sh — acceptance commands (run from experiment root), raw output to checks/accept_out.txt
cd "$(dirname "$0")/.." || exit 1
{
echo "### ffprobe frame count (out.mp4)"
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 out.mp4
echo
echo "### ffprobe streams/format (out.mp4)"
ffprobe -v error -show_entries stream=index,codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels -show_entries format=duration,size,bit_rate -of default=nw=1 out.mp4
echo
echo "### key/ listing"
ls key/*.png
echo
echo "### key sizes + hashes"
for f in key/k0000.png key/k0050.png key/k0100.png key/k0150.png key/k0200.png key/k0250.png key/keyframes_sheet.png; do
  [ -f "$f" ] && echo "$f $(stat -c%s "$f") $(sha256sum "$f" | cut -c1-16)"
done
echo
echo "### frames count + first/last"
ls frames/f*.png | wc -l
ls frames/f*.png | head -2
ls frames/f*.png | tail -2
echo
echo "### audio"
ffprobe -v error -show_entries stream=codec_name,sample_rate,channels -show_entries format=duration,size -of default=nw=1 audio/score.wav
echo
echo "### video.mp4 (silent intermediate)"
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate -show_entries format=duration,size -of default=nw=1 video.mp4
} > checks/accept_out.txt 2>&1
cat checks/accept_out.txt
