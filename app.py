# app.py
from flask import Flask, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the model
model = load_model('vgg17.keras')

# Define categories
categories = { ... }  # (include your categories here)

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
