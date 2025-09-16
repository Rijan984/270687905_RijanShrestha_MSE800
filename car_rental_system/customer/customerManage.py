from database.database import create_connection
import sqlite3

def bookCar_customer(data, car_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET availability = ?, bookingStatus = ?, bookedBy = ? WHERE car_id = ?", ("no", "pending", str(data[0]), car_id))
        conn.commit()
        print("You request sent for booking. Please wait for admin to aprove it")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()

def cancel_booking(carId):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET availability = ?, bookingStatus = ?, bookedBy = ? WHERE car_id = ?", ("Yes", "available", "None", carId))
        conn.commit()
        print("Booking canceled")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()