from flask import Blueprint, request, jsonify
from PIL import Image
from yolo_model.model import predict_yolo
from tensorflow_model.model import predict_tf
from scikit_model import predict as pred_sk


bp = Blueprint('predict', __name__, url_prefix='/predict')


@bp.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file.stream)
        # result = predict_yolo(img)
        # result = predict_tf(img)
        result = pred_sk(img)

        return jsonify(result)


@bp.route('/sklearn', methods=['POST'])
def predict_sk():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file.stream)
        result = pred_sk(img)

        return jsonify(result.tolist())
