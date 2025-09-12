import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userRegister (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            pnumber TEXT NOT NULL,
            role TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password Text NOT NULL
        )
    ''')
    conn.commit()
    conn.close()