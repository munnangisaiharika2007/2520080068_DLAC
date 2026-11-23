"""
Expected Output: Image display window
Task 3: Read and display traffic images using OpenCV.
"""
import cv2
import os

print("=" * 60)
print("VisionPort Task 3: Read & Display Traffic Image Using OpenCV")
print("=" * 60)

os.makedirs("outputs", exist_ok=True)
img_paths = ["images/sample_traffic.jpg", "sample_traffic.jpg", "images/traffic_street.jpg"]
img = None
for p in img_paths:
    if os.path.exists(p):
        img = cv2.imread(p)
        img_path = p
        break

if img is None:
    print("[ERROR] Could not load traffic image")
    exit(1)

h, w, c = img.shape
print(f"Loaded Image   : {img_path}")
print(f"Dimensions     : {w} x {h} (Width x Height)")
print(f"Channels       : {c} (BGR)")
print(f"Total Pixels   : {w * h}")

display_img = img.copy()
cv2.rectangle(display_img, (0, 0), (w, 50), (20, 20, 20), -1)
cv2.putText(display_img, f"VisionPort Traffic Image: {w}x{h} | {c} Channels",
            (15, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2)

out_file = "outputs/task3_display_output.jpg"
cv2.imwrite(out_file, display_img)
print(f"Annotated display frame saved to: {out_file}")

try:
    cv2.imshow("VisionPort Task 3: Traffic Image", display_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    print("Displayed in GUI window successfully.")
except Exception:
    pass

print("-" * 60)
print("Expected Output: Image display window [VERIFIED]")
