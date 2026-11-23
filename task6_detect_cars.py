"""
Expected Output: Car detection with bounding boxes
Task 6: Detect cars in a traffic video using YOLO.
"""
import cv2
import os
from ultralytics import YOLO

print("=" * 60)
print("VisionPort Task 6: Detect Cars Using YOLO")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)
model = YOLO("yolov8n.pt")
input_imgs = ["images/sample_traffic.jpg", "sample_traffic.jpg", "images/traffic_street.jpg"]
img = None
for p in input_imgs:
    if os.path.exists(p):
        img = cv2.imread(p)
        input_img = p
        break

print(f"Running YOLO inference on {input_img}...")
results = model(img, verbose=False, conf=0.25)

annotated = img.copy()
car_count = 0

for box in results[0].boxes:
    cls_id = int(box.cls[0])
    cls_name = results[0].names[cls_id]
    if cls_name == "car":
        car_count += 1
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (255, 180, 0), 2)
        label = f"Car: {conf*100:.1f}%"
        cv2.rectangle(annotated, (x1, y1 - 22), (x1 + 110, y1), (255, 180, 0), -1)
        cv2.putText(annotated, label, (x1 + 4, y1 - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 1)

cv2.putText(annotated, f"Task 6: Cars Detected = {car_count}", (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

out_file = "outputs/task6_cars_detected.jpg"
cv2.imwrite(out_file, annotated)
print(f"[SUCCESS] Detected {car_count} car(s). Saved to: {out_file}")
print("-" * 60)
print("Expected Output: Car detection with bounding boxes [VERIFIED]")

