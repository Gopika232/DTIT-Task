import cv2  #type:ignore

from storage_sql import save_attendance
def start_camera():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("Camera not detected")
        return
    
    marked = False

    print("Press q to quit")
    
    while True:
        ret,frame = camera.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if marked ==False:
                save_attendance("Employee")
                marked=True
            cv2.imshow("Face Recognition",frame)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
