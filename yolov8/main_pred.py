from ultralytics import YOLO

import os

model = YOLO('./../runs/classify/train7/weights/best.pt')
sample_folder = './brick-data/sample'

sample_files = os.listdir(sample_folder)

for sample_file in sample_files:
    sample_dir = os.path.join(sample_folder, sample_file)
    result = model(sample_dir)
