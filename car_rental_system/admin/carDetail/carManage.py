from database.database import create_connection
import sqlite3

def add_car(model, year, mileage, available_now, min_rent_period, max_rent_period):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO carDetails (model, year, mileage, availability, min_rent_period, max_rent_period) VALUES (?, ?, ?, ?, ?, ?)", (model, year, mileage, available_now, min_rent_period, max_rent_period))
        conn.commit()
        print("Car added successfully")
    except sqlite3.IntegrityError as e:
        print(f"Car Addition failed: {e}")
    conn.close()

# def update_car():
#     conn = create_connection()
#     cursor = conn.cursor()
#     try: 
#         cursor.execute("UPDATE users SET model = ? WHERE carID = ?", (model, availability, carId))
#         conn.commit()
#         print(f"User {name}'s email updated successfully.")
#     except sqlite3.IntegrityError:
#         print("Error: Email must be unique.")
#     finally:
#         conn.close()

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
    # if len(rows) > 0: 
    conn.close()
        # for availability in rows:
        #     print(availability[4])
    return rows
    # else:
    #     print("-----No Car Aavailable-----")

def delete_car(car_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carDetails WHERE car_id = ?", (car_id,))
    if cursor.rowcount == 0:   # ✅ no rows affected means ID not found
        print("❌ No car found with that ID.")
    else:
        conn.commit()
        print("🗑️ Car deleted.")
    
    conn.close()