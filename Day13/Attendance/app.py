from flask import Flask, render_template, Response   #type:ignore
import cv2   #type:ignore
import os
from attendance import mark_attendance

app = Flask(__name__)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainer.yml")
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
names = []

for folder in os.listdir("dataset"):
    names.append(folder)

camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray,1.3,5)

        for x,y,w,h in faces:
            face = gray[y:y+h,x:x+w]
            id, confidence = recognizer.predict(face)
            if confidence < 70:
                name = names[id]
                mark_attendance(name)
                text = name
            else:
                text="Unknown"

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        ret,buffer=cv2.imencode(".jpg",frame)
        frame=buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')

@app.route("/")
def index():

    return """
    <h1>
    AI Attendance System
    </h1>
    <img src="/video">
    """

@app.route("/video")
def video():
    return Response(generate_frames(),mimetype="multipart/x-mixed-replace; boundary=frame")

app.run(debug=True)