#!/bin/bash
# checks/run_final.sh — final assembly sequence (run from experiment root after render completes)
set -e
cd "$(dirname "$0")/.."

BL="D:/Software/Blender Foundation/Blender 5.2/blender.exe"

echo "=== [1/7] mechanism checks ==="
"$BL" -b scene.blend -P checks/check_mechanisms.py > checks/mech_output.txt 2>&1
tail -3 checks/mech_output.txt

echo "=== [2/7] selfcheck (300 frames) ==="
"$BL" -b --factory-startup -P checks/selfcheck_frames.py > checks/selfcheck_output.txt 2>&1
tail -3 checks/selfcheck_output.txt

echo "=== [3/7] rerun check (f123, f234) ==="
"$BL" -b scene.blend -P checks/rerun_check.py -- --frames 123,234 > checks/rerun_check.txt 2>&1
cat checks/rerun_check.txt

echo "=== [4/7] video.mp4 ==="
ffmpeg -y -v error -framerate 30 -start_number 0 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 -movflags +faststart video.mp4
ls -la video.mp4

echo "=== [5/7] out.mp4 (with audio) ==="
ffmpeg -y -v error -framerate 30 -start_number 0 -i frames/f%04d.png -i audio/score.wav -c:v libx264 -pix_fmt yuv420p -crf 16 -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4
ls -la out.mp4

echo "=== [6/7] accept ==="
bash checks/run_accept.sh | tail -5

echo "=== [7/7] sheets ==="
"$BL" -b --factory-startup -P make_sheets.py > checks/sheets_log.txt 2>&1
tail -4 checks/sheets_log.txt

echo "ALL_DONE"
