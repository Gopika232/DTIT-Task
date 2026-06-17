import sqlite3

def get_db():
    conn = sqlite3.connect("attendance.db")
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,password TEXT,role TEXT DEFAULT 'employee')""")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,date TEXT,status TEXT)""")

    conn.commit()
    conn.close()