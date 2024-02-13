import requests
from bs4 import BeautifulSoup
import os

# 웹 페이지 URL
url = 'https://www.bricklink.com/catalogList.asp?v=2&pg=1&catString=5&catType=P'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# HTML 요청
response = requests.get(url, headers=headers)

print(response)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 클래스가 'blCatalogImagePopup'인 모든 태그 찾기
image_tags = soup.find_all(class_='blCatalogImagePopup')

# 이미지를 저장할 디렉터리 경로
image_folder = 'brick_images'

# 디렉터리가 없으면 생성
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 이미지 태그를 순회하면서 이미지 다운로드 및 저장
for tag in image_tags:

    # 이미지 태그 찾기
    img_tag = tag.find('img')
    
    # 이미지 URL 추출
    if img_tag:
        image_url = img_tag['src']
        
        # 이미지 URL에서 브릭 ID 추출
        brick_id = tag['title'].split(' ')[2]
        
        # 이미지 다운로드
        image_data = requests.get(image_url).content
        
        # 이미지를 브릭 ID로 저장
        image_path = os.path.join(image_folder, f'{brick_id}.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_data)

print(f'Images saved to {image_folder}')