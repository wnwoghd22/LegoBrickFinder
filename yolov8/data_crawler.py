import requests
import os
import random
import shutil

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

PART_IDS = [3001, 3002, 3003, 3004, 3005]
LIST_LEN = 300
OK = 200
TRAIN_RATIO = 0.7

for part_id in PART_IDS:

    # 이미지를 저장할 디렉터리 경로
    image_folder = f'brick-data/pi-{part_id}'

    # 디렉터리가 없으면 생성
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    for idx in range(LIST_LEN):

        # 브릭 이미지 API
        image_url = f'https://img.bricklink.com/ItemImage/PT/{idx}/{part_id}.t1.png' 

        # HTTP 요청 보내기
        response = requests.get(image_url, headers=headers)

        # 응답 코드 확인
        if response.status_code == OK:  # 응답 코드가 200 (OK)일 때만 이미지를 저장
            # 이미지 다운로드
            image_data = response.content
                    
            # 이미지를 브릭 ID로 저장
            image_path = os.path.join(image_folder, f'{part_id}-{idx}.png')
            with open(image_path, 'wb') as f:
                f.write(image_data)
        else:
            print(f"Failed to download image: {idx}, Status code: {response.status_code}")

    # train, val 나눠 담기
    train_folder = os.path.join('brick-dataset', 'train', str(part_id))
    val_folder = os.path.join('brick-dataset', 'val', str(part_id))
    
    # 디렉토리가 없으면 생성
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    image_files = os.listdir(image_folder)
    
    # 이미지 파일을 분할 비율에 따라 train과 val에 복사
    random.shuffle(image_files)  # 파일 목록을 무작위로 섞음
    num_train = int(len(image_files) * TRAIN_RATIO) # 학습용 이미지 비율 구하기
    train_files = image_files[:num_train] # 슬라이싱
    val_files = image_files[num_train:]

    # train 폴더에 이미지 복사
    for file_name in train_files:
        src_path = os.path.join(image_folder, file_name)
        dest_path = os.path.join(train_folder, file_name)
        shutil.copy(src_path, dest_path)
    
    # val 폴더에 이미지 복사
    for file_name in val_files:
        src_path = os.path.join(image_folder, file_name)
        dest_path = os.path.join(val_folder, file_name)
        shutil.copy(src_path, dest_path)


print(f'Images saved to {image_folder}')
