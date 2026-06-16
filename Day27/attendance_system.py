import cv2     #type:ignore
import pickle
import datetime
import csv
import os
import time

# Load trained ML model
model = pickle.load(open("attendance_model.pkl", "rb"))

# Load face detector
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Attendance file
attendance_file = "attendance.csv"

# Store last marked time
last_marked = {}

def get_session():
    hour = datetime.datetime.now().hour

    if 8 <= hour < 12:
        return "Morning"

    elif 12 <= hour < 16:
        return "Afternoon"

    elif 16 <= hour < 20:
        return "Evening"

    else:
        return "Outside Time"

def mark_attendance(name):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    session = get_session()

    if session == "Outside Time":
        print("Attendance time closed")
        return

    records = []

    if os.path.exists(attendance_file):
        with open(attendance_file,"r") as file:
            reader = csv.reader(file)
            records = list(reader)

    # Check duplicate
    for row in records:
        if len(row) >= 3:
            if (row[0] == name and row[1] == today and row[2] == session):
                print(f"{name} already marked for {session}")
                return
            
    # Save attendance
    with open(attendance_file,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,today,session,datetime.datetime.now().strftime("%H:%M:%S")])
    print(f"Attendance Marked: {name} - {session}")

# Start camera
camera = cv2.VideoCapture(0)

print("Camera started...")
print("Press ESC to stop")


while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # Create feature input
        sample = [[x/1000,y/1000,w/1000]]
        name = model.predict(sample)[0]

        # Avoid continuous marking
        current_time = time.time()
        if name not in last_marked:
            mark_attendance(name)
            last_marked[name] = current_time
        else:
            if current_time - last_marked[name] > 30:
                mark_attendance(name)
                last_marked[name] = current_time
        cv2.putText(frame,name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    cv2.imshow("AI Attendance System",frame)

    # ESC key
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()