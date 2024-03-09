from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)


    from .views import predict_views
    app.register_blueprint(predict_views.bp)


    @app.route('/')
    def hello():
        return 'hello'


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=8000)
