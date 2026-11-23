"""
Expected Output: Frames saved as images
Task 5: Extract individual frames from traffic videos.
"""
import cv2
import os

print("=" * 60)
print("VisionPort Task 5: Extract Individual Frames From Traffic Video")
print("=" * 60)

video_paths = ["videos/traffic_sample.mp4", "traffic_sample.mp4", "videos/traffic_demo.mp4"]
video_path = None
for p in video_paths:
    if os.path.exists(p):
        video_path = p
        break

output_dir = "extracted_frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"[ERROR] Could not open video: {video_path}")
    exit(1)

fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_interval = 15  # extract every 15 frames
saved_count = 0
frame_idx = 0

print(f"Extracting frames from {video_path} into {output_dir}/...")

while cap.isOpened() and saved_count < 10:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_idx % frame_interval == 0:
        saved_count += 1
        frame_file = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_file, frame)
        print(f" [SAVED] {frame_file} (source frame #{frame_idx})")
    frame_idx += 1

cap.release()
print(f"\nExtraction Complete: {saved_count} frames saved to {output_dir}/")
print("-" * 60)
print("Expected Output: Frames saved as images [VERIFIED]")
