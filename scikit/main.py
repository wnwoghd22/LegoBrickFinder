import os
import pickle

from skimage.io import imread
from skimage.transform import resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# prepare data
input_dir = './brick-data'
categories = ['3004', '3005']

data = []
labels = []

for cat_idx, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, f'pi-{category}')):
        img_path = os.path.join(input_dir, f'pi-{category}', file)
        print(img_path)
        img = imread(img_path)
        img = resize(img, (80, 60))
        data.append(img.flatten())
        labels.append(cat_idx)

data = np.asarray(data)
labels = np.asarray(labels)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(
    data, labels,
    test_size=0.2,
    shuffle=True,
    stratify=labels
)

# train classifier
classifier = SVC()

parameters = [
    {
        'gamma': [0.01, 0.001, 0.0001], 
        'C': [1, 10, 100, 700]
    }
]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)

# test performance
best_estimator = grid_search.best_estimator_

y_pred = best_estimator.predict(x_test)

score = accuracy_score(y_pred, y_test)

print(f'{score * 100}% of samples were correctly classified')

pickle.dump(best_estimator, open('./classifier.p', 'wb'))
