from database.database import create_connection
import sqlite3

def add_user(fname, lname, pnumber, role, email, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO userRegister (fname, lname, pnumber, role, email, password) VALUES (?, ?, ?, ?, ?, ?)", (fname, lname, pnumber, role, email, password)
        )
        conn.commit()
        print("User added successfully")
    except sqlite3.IntegrityError:
        print("Email must be unique")
    conn.close()

def userLogin(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userRegister WHERE email = ? AND password=?", (email, password,))
    rows = cursor.fetchone()
    conn.close()
    return rows

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userRegister")
    rows = cursor.fetchall()
    conn.close()
    return rows