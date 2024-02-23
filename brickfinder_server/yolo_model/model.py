from ultralytics import YOLO

import os

model = YOLO('./trained/weights/best.pt')

def predict_yolo(image):
    return model(image)
