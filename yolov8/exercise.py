'''
https://docs.ultralytics.com/ko/tasks/classify/#models
'''

from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n-cls.yaml')  # build a new model from YAML
model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n-cls.yaml').load('yolov8n-cls.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='./weather-dataset', epochs=1, imgsz=64)

print('train complete')
