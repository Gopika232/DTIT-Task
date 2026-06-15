from tkinter import *
from facial_reg import start_camera
from storage_sql import view_attendance

def start():
    start_camera()

def view():
    view_attendance()

root = Tk()
root.title("AI Attendance System")
root.geometry("350x250")

Label(root,text="Corporate Attendance System",font=("Arial",15)).pack(pady=20)

Button(root,text="Start Recognition",command=start,width=20).pack(pady=10)
Button(root,text="View Attendance",command=view,width=20).pack(pady=10)
Button(root,text="Exit",command=root.destroy,width=20).pack(pady=10)

root.mainloop()