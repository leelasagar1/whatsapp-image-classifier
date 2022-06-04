import os
import sys

from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np
from util import base64_to_pil


app = Flask(__name__)

from keras.applications.mobilenet_v2 import MobileNetV2
model = load_model("VGG19_model_weights.h5")

print('Model loaded. Check http://127.0.0.1:5000/')

MODEL_PATH = 'models/your_model.h5'

def convertImage(imgData1):
    imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
    with open('output.jpg', 'wb') as output:
        output.write(base64.b64decode(imgstr))
def model_predict(image,model):
    print("file_loaded")
    class_list = ["Food", "Gods", "Greetings","Group_pics","Memes","Notes","Selfies","Telugu_quotes","Temples","Whatsapp_Screeshots"]
    im = cv2.imread(image)
    im = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (256, 256)).astype(np.float32) / 255.0
    im = np.expand_dims(im, axis =0)
    outcome = model.predict(im)
    ind = np.argmax(outcome)

    return ind,class_list[ind]  


@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.FILES['file'])
        
        img = request.get_data()
        convertImage(img)
        prob,category = model_predict('output.jpg', model)
        return jsonify(result=category,prob=prob)

    return None


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
