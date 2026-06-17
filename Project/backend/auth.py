from backend.database import get_db
from werkzeug.security import generate_password_hash, check_password_hash   #type:ignore

def register(username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?",(username,))
    user = cursor.fetchone()
    if user:
        conn.close()
        return False

    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users(username,password,role) VALUES (?,?,?)",(username, hashed_password,"employee"))
    conn.commit()
    conn.close()
    return True

def login(username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?",(username,))
    user = cursor.fetchone()
    conn.close()
    if user:
        stored_password = user[2]
        if check_password_hash(stored_password,password):
            return True
    return False