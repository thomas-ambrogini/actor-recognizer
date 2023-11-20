import os
import argparse
import numpy as np
import tensorflow as tf
import boto3
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers, models
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications.resnet50 import preprocess_input
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.applications import ResNet50
from keras.models import Sequential
from keras.layers import Flatten, Dense, Resizing
from Training import dataset
from sklearn.preprocessing import LabelEncoder

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=os.environ.get('SM_OUTPUT_DATA_DIR'))
    parser.add_argument('--model-dir', type=str,  default=10)
    args, _ = parser.parse_known_args()

		class_count = 100

    data_path = '/opt/ml/input/data/train/'
		with np.load(data_path + 'dataset.npz') as data:
		        train_faces = data["arr_0"]
		        train_labels = data["arr_1"]

		face_images = preprocess_input(np.array(train_faces))
		
		out_encode = LabelEncoder()
		out_encode.fit(train_labels)
		face_labels = out_encode.transform(train_labels)

		x_train, x_test, y_train, y_test = train_test_split(face_images, face_labels, train_size=0.8, stratify=face_labels, random_state=0)

		base_model = ResNet50(weights='imagenet', include_top=False)
		base_model.trainable = False
		
		model = Sequential()
		model.add(Resizing(224, 224))
		model.add(base_model)
		model.add(Flatten())
		model.add(Dense(1024, activation='relu'))
		model.add(Dense(class_count, activation='softmax'))
		
		model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

		hist = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=10, epochs=10)

    model.save('/opt/ml/model/mnist_model/1')
