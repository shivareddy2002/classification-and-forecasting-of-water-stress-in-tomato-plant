import os
import tensorflow as tf
from tensorflow import keras

MODEL_FOLDER = "models"

def load_models(X_train=None, y_train=None):
    if not os.path.exists(MODEL_FOLDER):
        os.makedirs(MODEL_FOLDER)

    h5_path = os.path.join(MODEL_FOLDER, "model.h5")
    if os.path.exists(h5_path):
        keras_model = keras.models.load_model(h5_path)
    else:
        if X_train is None or y_train is None:
            raise ValueError("Training data required to create new Keras model")

        keras_model = keras.Sequential([
            keras.layers.Input(shape=(X_train.shape[1],)),
            keras.layers.Dense(64, activation="relu"),
            keras.layers.Dense(1, activation="sigmoid")
        ])

        keras_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        keras_model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
        keras_model.save(h5_path)

    return keras_model
