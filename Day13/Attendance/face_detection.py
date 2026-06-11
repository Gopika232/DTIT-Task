import cv2   #type:ignore

def detect_face(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

    faces = face_detector.detectMultiScale(gray,1.3,5)

    return faces, gray