import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from PIL import Image


# pickle로 저장된 모델을 로드
with open('scikit_model/classifier.p', 'rb') as f:
    classifier = pickle.load(f)


def predict(image):

    # 이미지를 배열로 변환
    img_array = np.asarray(image)

    img = resize(img_array, (80, 60))  # 이미지 크기 조정
        
    # 이미지를 평탄화
    flat_img = img.flatten()

    # 이미지 데이터를 SVC 모델에 입력으로 사용
    result = classifier.predict([flat_img])
    
    return result
    