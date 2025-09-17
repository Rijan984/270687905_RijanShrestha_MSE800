from database.database import create_connection
import sqlite3

def bookCar_customer(data, car_id, rentDuration):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET availability = ?, bookingStatus = ?, bookedBy = ?, rentDuration = ? WHERE car_id = ?", ("no", "pending", str(data[0]), rentDuration, car_id))
        conn.commit()
        print("You request sent for booking. Please wait for admin to aprove it")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()

def cancel_booking(carId):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET availability = ?, bookingStatus = ?, bookedBy = ?, rentDuration = ? WHERE car_id = ?", ("yes", "available", "none", "none", carId))
        conn.commit()
        print("Booking canceled")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()