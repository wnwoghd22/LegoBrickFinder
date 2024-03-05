import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# pickle로 저장된 모델을 로드
with open('scikit_model/classifier.p', 'rb') as f:
    classifier = pickle.load(f)


def predict_sk(image):
    result = classifier.predict(image)

    return result