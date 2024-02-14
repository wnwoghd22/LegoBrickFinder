import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

PART_ID = 3004
LIST_LEN = 300
OK = 200

# 이미지를 저장할 디렉터리 경로
image_folder = f'brick-data/pi-{PART_ID}'

# 디렉터리가 없으면 생성
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

for idx in range(LIST_LEN):

    # 브릭 이미지 API
    image_url = f'https://img.bricklink.com/ItemImage/PT/{idx}/{PART_ID}.t1.png' 

    # HTTP 요청 보내기
    response = requests.get(image_url, headers=headers)

    # 응답 코드 확인
    if response.status_code == OK:  # 응답 코드가 200 (OK)일 때만 이미지를 저장
        # 이미지 다운로드
        image_data = response.content
                
        # 이미지를 브릭 ID로 저장
        image_path = os.path.join(image_folder, f'{PART_ID}-{idx}.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_data)
    else:
        print(f"Failed to download image: {idx}, Status code: {response.status_code}")


print(f'Images saved to {image_folder}')