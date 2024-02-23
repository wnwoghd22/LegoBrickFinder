from ultralytics import YOLO

import os

model = YOLO('./yolo_model/trained/weights/best.pt')

def predict_yolo(image):
    results = model(image)

    probs = results[0].probs

    indices = [results[0].names[i] for i in probs.top5]
    confs = probs.top5conf

    print(indices)
    print(confs)

    return list(zip(indices, confs.tolist()))
