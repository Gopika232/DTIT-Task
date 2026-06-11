import pandas as pd
from datetime import datetime
import os

file = "attendance.csv"

def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if os.path.exists(file):
        df = pd.read_csv(file)

    else:
        df = pd.DataFrame(
            columns=["Name","Date","Time"])

    already = df[(df["Name"]==name)&(df["Date"]==date)]

    if len(already)==0:
        new = pd.DataFrame([[name,date,time]],columns=["Name","Date","Time"])
        df = pd.concat([df,new],ignore_index=True)
        df.to_csv(file,index=False)
        print("Attendance marked:",name)