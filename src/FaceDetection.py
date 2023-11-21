from Utils import utils 
from Utils import drawing
from PIL import Image
import os
from mtcnn.mtcnn import MTCNN


IMAGES_DIRECTORY = "../Input/images"

class FaceDetector():
	def __init__(self, detector=MTCNN()):	
		self.current_dir = os.path.curdir
		self.detector = detector

	def faces_boxes(self, image):
		faces = self.detect_faces(image)
		boxes = []
		for face in faces:
			x,y,w,h = map(lambda co:0 if co<0 else co, face["box"])
			boxes.append([x, y, x+w, y+h])
		return boxes

	def detect_faces(self, image):
		faces = self.detector.detect_faces(image)
		return faces

	def crop_faces(self, image, boxes):
		image = image.copy()
		face_crops = []
		
		for box in boxes:
			x1,y1,x2,y2 = box
			face_crop = image[y1:y2,x1:x2]
			face_crops.append(face_crop)
		
		return face_crops

	def draw_boxes(self, image, boxes, color=(255,0,0),thickness=5):
		
		image_with_boxes = drawing.draw_boxes(image, boxes, color, thickness)
		return image_with_boxes

