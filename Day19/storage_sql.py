import sqlite3
from datetime import datetime
def save_attendance(name="Employee"):
    conn = sqlite3.connect("attendance.db")

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS attendance(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   date TEXT,
                   time TEXT)
                   """)
    now = datetime.now()
    date=now.strftime("%Y-%m-%d")
    time=now.strftime("%H:%M:%S")
    
    cursor.execute(
        """INSERT INTO attendance(name,date,time) values(?,?,?)""",(name,date,time)
        )
    conn.commit()
    conn.close()
    print("Attendance Saved")


def view_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM attendance")
    print("\nAttendance Records")
    for row in data:
        print(row)
    conn.close()