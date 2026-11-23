"""
Expected Output: Working Python Environment Verification
Task 1: Install Python, OpenCV and required libraries.
"""
import sys
import os
import importlib
import numpy as np

print("=" * 60)
print("VisionPort Task 1: Environment & Library Verification")
print("=" * 60)

# Check Python version
print(f"Python Version: {sys.version}")
if sys.version_info < (3, 8):
    print("WARNING: Python 3.8 or higher is recommended.")
else:
    print("[OK] Python version is compatible.\n")

# Required libraries for the VisionPort project
required_libraries = [
    ("cv2", "OpenCV (opencv-python)"),
    ("numpy", "NumPy"),
    ("PIL", "Pillow"),
    ("ultralytics", "Ultralytics YOLOv8"),
    ("torch", "PyTorch"),
    ("fastapi", "FastAPI"),
    ("uvicorn", "Uvicorn")
]

all_passed = True

print("Checking installed packages:")
print("-" * 60)
for module_name, display_name in required_libraries:
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, "__version__", "Installed")
        print(f"[PASSED] {display_name:<28} : v{version}")
    except (ImportError, ModuleNotFoundError):
        print(f"[MISSING] {display_name:<28} : NOT INSTALLED")
        all_passed = False

# OpenCV Test Image Generation
try:
    import cv2
    os.makedirs("outputs", exist_ok=True)
    test_img = np.zeros((300, 500, 3), dtype=np.uint8)
    test_img[:] = (30, 30, 30)
    cv2.putText(test_img, "OpenCV Working Successfully!", (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    
    out_path = "outputs/task1_opencv_test.jpg"
    cv2.imwrite(out_path, test_img)
    cv2.imwrite("task1_opencv_test.jpg", test_img)
    print(f"\n[PASSED] Generated OpenCV test image: {out_path} and task1_opencv_test.jpg")
except Exception as e:
    print(f"\n[FAILED] OpenCV image generation error: {e}")
    all_passed = False

print("-" * 60)
if all_passed:
    print("Expected Output: Working Python environment [VERIFIED]")
else:
    print("Expected Output: Environment setup incomplete [FAILED]")
