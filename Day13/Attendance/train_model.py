import cv2  #type:ignore
import os
import numpy as np
from PIL import Image

data_path = "dataset"
recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

faces = []
ids = []

employee_id = 0

for employee in os.listdir(data_path):
    folder = os.path.join(data_path,employee)
    
    for image in os.listdir(folder):
        img_path = os.path.join(folder,image)
        img = Image.open(img_path).convert("L")
        img_numpy = np.array(img)
        detected_faces = detector.detectMultiScale(img_numpy)

        for x,y,w,h in detected_faces:
            faces.append(img_numpy[y:y+h,x:x+w])
            ids.append(employee_id)
    employee_id += 1

recognizer.train(faces,np.array(ids))

recognizer.save("trainer.yml")

print("Model trained successfully")