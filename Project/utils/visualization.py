import pandas as pd
import matplotlib.pyplot as plt    #type:ignore

df=pd.read_csv("dataset/attendance_data.csv")

plt.bar(df["Name"],df["Days_Present"])
plt.xlabel("Employee")
plt.ylabel("Days Present")
plt.title("Attendance")
plt.show()