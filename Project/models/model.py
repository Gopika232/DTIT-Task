import cv2    #type:ignore
import os
import numpy as np

class AttendanceModel:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def detect_face(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            return "Image not found"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

        if len(faces) > 0:
            return {
                "status": "Face detected",
                "faces": len(faces)
                }
        return {
            "status": "No face detected",
            "faces": 0
            }

model = AttendanceModel()