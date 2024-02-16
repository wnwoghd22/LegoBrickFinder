from ultralytics import YOLO

model = YOLO('./../runs/classify/train2/weights/best.pt')

result = model('./weather-dataset/train/sunrise/sunrise1.jpg')

# print(result)