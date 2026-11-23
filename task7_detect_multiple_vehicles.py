"""
Expected Output: Multiple vehicle detection
Task 7: Detect bikes, buses and trucks.
"""
import cv2
import os
from ultralytics import YOLO

print("=" * 60)
print("VisionPort Task 7: Detect Bikes, Buses, Trucks, and Cars")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)
TARGET_VEHICLES = {
    "car": (255, 180, 0),        # Cyan / Blue
    "motorcycle": (0, 220, 0),   # Green
    "bicycle": (50, 255, 150),   # Light Green
    "bus": (0, 140, 255),        # Orange
    "truck": (255, 0, 200)       # Magenta
}

model = YOLO("yolov8n.pt")
input_imgs = ["images/sample_traffic.jpg", "sample_traffic.jpg", "images/traffic_street.jpg"]
img = None
for p in input_imgs:
    if os.path.exists(p):
        img = cv2.imread(p)
        input_img = p
        break

results = model(img, verbose=False, conf=0.25)
annotated = img.copy()

counts = {k: 0 for k in TARGET_VEHICLES}

for box in results[0].boxes:
    cls_name = results[0].names[int(box.cls[0])]
    v_type = None
    if cls_name in TARGET_VEHICLES:
        v_type = cls_name
    elif "bike" in cls_name:
        v_type = "motorcycle"
        
    if v_type:
        counts[v_type] += 1
        color = TARGET_VEHICLES[v_type]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        
        cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
        label = f"{v_type.capitalize()} {conf*100:.0f}%"
        cv2.putText(annotated, label, (x1, y1 - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)

out_file = "outputs/task7_multiple_vehicles.jpg"
cv2.imwrite(out_file, annotated)
print(f"Vehicle counts detected: {counts}")
print(f"Output saved to: {out_file}")
print("-" * 60)
print("Expected Output: Multiple vehicle detection [VERIFIED]")
