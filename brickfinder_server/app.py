from flask import Flask, request
from yolo_model.model import predict_yolo

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/predict', method=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        result = predict_yolo(file)

        return result
        