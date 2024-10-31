# app.py
from flask import Flask, request, jsonify
import cv2
from flask_cors import CORS 
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the model
model = load_model('vgg17.keras')

# Define categories
categories = {  0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
    26: 'del',
    27: 'nothing',
    28: 'space'
}
 # (include your categories here)

app = Flask(_name_)
CORS(app)  
@app.route('/predict', methods=['POST'])
def predict():
    # Get image from POST request
    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Preprocess the image
    img = cv2.resize(img, (200, 200)) / 255.0
    img = np.expand_dims(img, axis=0)

    # Make prediction
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction)

    # Return result as JSON
    return jsonify({
        "prediction": categories[predicted_class],
        "confidence": float(confidence)
    })

if _name_ == '_main_':
    app.run(debug=True,port=5000)