"""
Fashion MNIST model service (FastAPI).
Loads a trained Keras model and returns a prediction for an uploaded image.
Place your trained model file next to this script as 'fashion_cnn.keras'.

Run locally:  uvicorn main:app --reload
Interactive docs: http://localhost:8000/docs
"""
import io
import os
import functools
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException
import tensorflow as tf

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fashion_cnn.keras")
CLASS_NAMES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

app = FastAPI(title="Fashion MNIST Classifier", version="1.0")

@functools.lru_cache(maxsize=1)
def get_model():
    # Loaded once on the first request and cached for reuse
    return tf.keras.models.load_model(MODEL_PATH, compile=False)

def preprocess(raw_bytes):
    # Convert any uploaded image to the 28x28 grayscale format the model expects
    image = Image.open(io.BytesIO(raw_bytes)).convert("L").resize((28, 28))
    array = np.asarray(image, dtype="float32") / 255.0
    return array.reshape(1, 28, 28, 1)

@app.get("/")
def health():
    return {"status": "ok", "message": "Fashion MNIST classifier is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        batch = preprocess(await file.read())
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read the uploaded image.")
    probs = get_model()(batch, training=False).numpy()[0]
    idx = int(np.argmax(probs))
    return {"class_index": idx,
            "label": CLASS_NAMES[idx],
            "confidence": round(float(probs[idx]), 4)}
