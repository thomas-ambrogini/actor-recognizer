import tensorflow as tf
from tensorflow import keras
import os

PROJECT_DIRECTORY = ".."
model = keras.models.load_model(os.path.join(PROJECT_DIRECTORY, "Model", 'TFSVC.h5'))


# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model(model) 
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)