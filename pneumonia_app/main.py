import streamlit as st
from keras.models import load_model
from PIL import Image

from util import classify

# set title
st.title('pneumonia classification')

# set header
st.header('Please upload a chest X-Ray image')

# set uploader
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./pneumonia_classifier.h5')

# load class names
with open('./labels.txt', 'r') as f:
    class_names = [a.strip().split()[1] for a in f.readlines()]
    f.close()

print(class_names)

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

# classify image
class_name, conf_score = classify(image, model, class_names)

# write classification
st.write(f'## {class_name}')
st.write(f'### {conf_score}')