import sqlite3
from fastapi import  FastAPI, HTTPException
from model.schemas import Login, User

app = FastAPI()

def login_user(email:str, password:str):
    conn = sqlite3.connect("../revhire.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email, password FROM User WHERE email=?", (email,))
    user = cursor.fetchone()
    
    conn.close()
    
    if user[0] == email and user[1] == password:
        return True
    else:
        return False

def create_user(user: User):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO USER (user_id, name, email, password, mobile) VALUES (?, ?, ?, ?, ?)""", (user.user_id, user.name, user.email, user.password, user.mobile))

        conn.commit()
        conn.close()

        return {"message": "User created successfully"}
    
    except:
        raise HTTPException(status_code=500, detail="failed to create user")
    


def get_user(user_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM USER WHERE user_id = ?""", (user_id,))
        user = cursor.fetchone()

        conn.close()

        return {"user": user}
    except:
        return "No user found with that ID."

def update_user(user_id: int, user: User):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE USER SET name = ?, email = ?, password = ?, mobile = ? WHERE user_id = ?", 
                       (user.name, user.email, user.password, user.mobile, user_id))

        conn.commit()
        conn.close()

        return "User details updated successfully!"
    except:
        return "Error when updating the user details"

def delete_user(user_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM USER WHERE user_id = ?", (user_id,))

        conn.commit()
        conn.close()

        return "User deleted successfully!"
    except:
        return "Error when deleting the user."