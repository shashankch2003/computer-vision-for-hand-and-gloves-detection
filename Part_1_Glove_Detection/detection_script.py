import os
import json
from ultralytics import YOLO

MODEL_PATH = "runs/detect/train/weights/best.pt"
INPUT_FOLDER = "dataset/test_images"
OUTPUT_FOLDER = "submission/Part_1_Glove_Detection/output"
LOG_FOLDER = "submission/Part_1_Glove_Detection/logs"
CONF_THRESHOLD = 0.3

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

model = YOLO(MODEL_PATH)

for file in os.listdir(INPUT_FOLDER):
    if not file.lower().endswith(".jpg"):
        continue

    image_path = os.path.join(INPUT_FOLDER, file)
    results = model.predict(source=image_path, conf=CONF_THRESHOLD, save=True, project=OUTPUT_FOLDER, name='', exist_ok=True)
    
    detections = []
    for box in results[0].boxes:
        cls = int(box.cls)
        label = model.names[cls]
        conf = float(box.conf)
        xyxy = [round(x, 2) for x in box.xyxy[0].tolist()]
        detections.append({"label": label, "confidence": conf, "bbox": xyxy})

    with open(os.path.join(LOG_FOLDER, file.replace(".jpg", ".json")), "w") as f:
        json.dump({"filename": file, "detections": detections}, f, indent=4)

print("✅ Detection complete — outputs and logs generated.")
