Before You use this repo Star it🌟.

I Would really appreciate it🤝 & helps a lot

Computer-vision-for-hand-and-gloves-detection

The entire project is divided into two parts

# Part 1: Glove Detection

## Overview
This project detects **gloved vs bare hands** for safety compliance in industrial settings.

### Dataset
- **Source**: Roboflow Universe ("Hand Glove Detection Dataset")
- **Classes**: `gloved_hand`, `bare_hand`
- **Images**: 1500 (train/val/test split)
- **Preprocessing**: 640x640 resizing, normalization, and augmentation.

### Model
- **Model**: YOLOv8n
- **Framework**: PyTorch (Ultralytics)
- **Training**: Fine-tuned for 50 epochs on custom dataset.
- for better accuracy and use case and edge specific you could train it on more epochs
and choose the best epochs that gibes best.pt


### How to Run
commands:```bash python3 detection_script.py



