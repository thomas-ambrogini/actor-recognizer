from PIL import Image
import cv2
import os
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
 
ACTORS_DIR = "../Input/actors/"
OUTPUT_IMAGE_DIR = "../Output"

def open_image(image_path):
	image = cv2.imread(image_path)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return image

def normalize(embedding):
	in_encode = Normalizer(norm="l2")
	embedding_normalized = in_encode.transform(embedding)

	return embedding_normalized

def save_image(image, name):
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	cv2.imwrite(os.path.join(OUTPUT_IMAGE_DIR, name), image)

def check_openable(directory=ACTORS_DIR):
	
	for actor_dir in os.listdir(directory):
		actor_dir_abs = directory + actor_dir + '/'
		for filename in os.listdir(actor_dir_abs):
			path = actor_dir_abs + filename
			try:
				open_image(path)
			except:
				os.remove(path)
				print("impossibile aprire immagine {}".format(path))
			

		
	

		

