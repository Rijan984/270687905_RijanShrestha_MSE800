from database.database import create_connection
import sqlite3

def bookCar_customer(car_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET availability = ?, bookingStatus = ? WHERE car_id = ?", ("no", "pending", car_id))
        conn.commit()
        print("Booking successfully wait for admin to aprove it")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()