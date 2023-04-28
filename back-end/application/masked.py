import numpy as np
import cv2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
maskmodel = load_model('mask_detector.model')
# Retorna confiança de que um rosto está com máscara ou não
def hasMask(face):
    global maskmodel
    face = cv2.resize(face, (224, 224))
    face = preprocess_input(face)
    face = np.expand_dims(face, axis=0)
    return maskmodel.predict(face)[0][0]