import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout
from tensorflow.keras.applications.vgg19 import VGG19

# Load the pre-trained VGG19 model
base_model = VGG19(include_top=False, input_shape=(240, 240, 3))
x = base_model.output
flat = Flatten()(x)
class_1 = Dense(4608, activation='relu')(flat)
drop_out = Dropout(0.2)(class_1)
class_2 = Dense(1152, activation='relu')(drop_out)
output = Dense(2, activation='softmax')(class_2)
model = Model(inputs=base_model.inputs, outputs=output)

# Load the model weights
model.load_weights('detection/vgg_unfrozen.h5')

def get_class_name(class_no):
    """Map the class index to the corresponding tumor status."""
    return "No Tumor detected" if class_no == 0 else "Tumor detected"

def preprocess_image(image):
    """Process the uploaded image for prediction."""
    img = Image.open(image)
    img = img.resize((240, 240))
    img_array = np.array(img)
    input_img = np.expand_dims(img_array, axis=0)
    return input_img

def detect_tumor(image):
    """Predict the tumor status using the model."""
    preprocessed_img = preprocess_image(image)
    prediction = model.predict(preprocessed_img)
    class_idx = np.argmax(prediction, axis=1)[0]
    return get_class_name(class_idx)
