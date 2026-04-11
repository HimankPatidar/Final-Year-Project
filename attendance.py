import pandas as pd
from datetime import datetime
import os

def mark_attendance(name):
    file = "attendance.csv"

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # If file exists, load it
    if os.path.exists(file):
        df = pd.read_csv(file)
    else:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    # Check duplicate (same name + same date)
    if not ((df["Name"] == name) & (df["Date"] == date)).any():
        df.loc[len(df)] = [name, date, time]
        df.to_csv(file, index=False)
        print(f"✅ Attendance marked for {name}")
    else:
        print(f"⚠️ Already marked: {name}")