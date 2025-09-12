from database.database import create_connection
import sqlite3

def add_car(model, year, mileage, available_now, min_rent_period, max_rent_period):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO carDetails (model, year, mileage, available_now, min_rent_period, max_rent_period) VALUES (?, ?, ?, ?, ?, ?)", (model, year, mileage, available_now, min_rent_period, max_rent_period)
        )
        conn.commit()
        print("Car added successfully")
    except sqlite3.IntegrityError:
        print("Car Addition failed")
    conn.close()

# def userLogin(email, password):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM userRegister WHERE email = ? AND password=?", (email, password,))
#     rows = cursor.fetchone()
#     conn.close()
#     return rows

def view_cars():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carDetails")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_car(car_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carDetails WHERE car_id = ?", (car_id,))
    if cursor.rowcount == 0:   # ✅ no rows affected means ID not found
        print("❌ No user found with that ID.")
    else:
        conn.commit()
        print("🗑️ User deleted.")
    
    conn.close()