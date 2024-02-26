from flask import Flask, request, jsonify
from PIL import Image
from yolo_model.model import predict_yolo
from tensorflow_model.model import predict_tf

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file.stream)
        # result = predict_yolo(img)
        result = predict_tf(img)

        return jsonify(result)
