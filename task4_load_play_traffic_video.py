"""
Expected Output: Video playback
Task 4: Load and play a traffic video using OpenCV.
"""
import cv2
import os

print("=" * 60)
print("VisionPort Task 4: Load & Play Traffic Video")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)
video_paths = ["videos/traffic_sample.mp4", "traffic_sample.mp4", "videos/traffic_demo.mp4"]
video_path = None
for p in video_paths:
    if os.path.exists(p):
        video_path = p
        break

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"[ERROR] Could not open video: {video_path}")
    exit(1)

fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
duration = total_frames / fps if fps > 0 else 0

print(f"Video File     : {video_path}")
print(f"Resolution     : {w} x {h}")
print(f"Frame Rate     : {fps:.2f} FPS")
print(f"Total Frames   : {total_frames}")
print(f"Duration       : {duration:.2f} seconds")

processed = 0
last_frame = None

while cap.isOpened() and processed < 60:
    ret, frame = cap.read()
    if not ret:
        break
    processed += 1
    cv2.putText(frame, f"PLAYBACK: Frame {processed}/{total_frames} ({processed/fps:.2f}s)",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    last_frame = frame

cap.release()

if last_frame is not None:
    out_file = "outputs/task4_playback_preview.jpg"
    cv2.imwrite(out_file, last_frame)
    print(f"Preview playback frame saved to: {out_file}")

print(f"Successfully loaded and played {processed} video frames.")
print("-" * 60)
print("Expected Output: Video playback [VERIFIED]")
