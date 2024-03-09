import pytest
from io import BytesIO

from app import create_app

TEST_CONFIG = {
    'TESTING': True
}


@pytest.fixture(scope='session') # 한 번만 실행
def app():
    app = create_app(TEST_CONFIG)
    return app


@pytest.fixture # 매 테스트 실행 마다 실행
def client(app):
    client = app.test_client()
    return client


def test_main(client):
    response = client.get('/')

    assert response.status_code == 200


def test_sk_model(client):
    # 테스트할 이미지 파일 경로
    test_image_path = 'samples/3004-2.jpg'

    # 이미지 파일 열기
    with open(test_image_path, 'rb') as f:
        image_data = f.read()

    # POST 요청 데이터
    data = {
        'file': (BytesIO(image_data), 'test_image.jpg')  # 파일 형식으로 전송
    }

    # POST 요청 보내기
    response = client.post('/predict/sklearn', data=data, content_type='multipart/form-data')

    # 응답 코드 확인
    assert response.status_code == 200
