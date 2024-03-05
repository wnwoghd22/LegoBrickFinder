from flask import Flask, request, jsonify
from PIL import Image
from yolo_model.model import predict_yolo
from tensorflow_model.model import predict_tf
from scikit_model.model import predict_sk


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)


    @app.route('/')
    def hello():
        return 'hello'

    @app.route('/predict', methods=['POST'])
    def predict():
        if request.method == 'POST':
            file = request.files['file']
            img = Image.open(file.stream)
            # result = predict_yolo(img)
            # result = predict_tf(img)
            result = predict_sk(img)

            return jsonify(result)


    @app.route('/predict/sklearn', methods=['POST'])
    def predict_sk():
        if request.method == 'POST':
            file = request.files['file']
            img = Image.open(file.stream)
            result = predict_sk(img)

            return jsonify(result)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=8000)
