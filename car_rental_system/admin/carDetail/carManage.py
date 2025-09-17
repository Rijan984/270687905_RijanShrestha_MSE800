from database.database import create_connection
import sqlite3

def add_car(model, year, mileage, available_now, min_rent_period, max_rent_period, bookingStatus, admin_id, bookedBy, rentDuration):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO carDetails (model, year, mileage, availability, min_rent_period, max_rent_period, bookingStatus, admin_id, bookedBy, rentDuration) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (model, year, mileage, available_now, min_rent_period, max_rent_period, bookingStatus, admin_id, bookedBy, rentDuration))
        conn.commit()
        print("Car added successfully")
    except sqlite3.IntegrityError as e:
        print(f"Car Addition failed: {e}")
    conn.close()


def update_car(car_id, new_model=None, new_year=None, new_mileage=None, new_availability=None, new_min_rent_period=None, new_max_rent_period=None, new_bookingStatus=None):
    conn = create_connection()
    cursor = conn.cursor()
    """
    Updates car details in the carDetails table.
    
    Args:
        car_id (int): The ID of the car to update.
        new_model (str, optional): The new model name.
        new_year (str, optional): The new year.
        new_mileage (str, optional): The new mileage.
        new_availability (str, optional): The new availability status.
        new_bookingStatus (str, optional): The new booking status.
    """
    conn = create_connection()
    if conn is None:
        return
        
    cursor = conn.cursor()
    
    # Build the SQL statement dynamically based on provided arguments
    update_data = []
    query_parts = []
    
    if len(new_model) > 1:
        query_parts.append("model = ?")
        update_data.append(new_model)
    if len(new_year) > 1:
        query_parts.append("year = ?")
        update_data.append(new_year)
    if len(new_mileage) > 1:
        query_parts.append("mileage = ?")
        update_data.append(new_mileage)
    if len(new_availability) > 1:
        query_parts.append("availability = ?")
        update_data.append(new_availability)
    if len(new_min_rent_period) > 1:
        query_parts.append("min_rent_period = ?")
        update_data.append(new_min_rent_period)
    if len(new_max_rent_period) > 1:
        query_parts.append("max_rent_period = ?")
        update_data.append(new_max_rent_period)
    if len(new_bookingStatus) > 1:
        query_parts.append("bookingStatus = ?")
        update_data.append(new_bookingStatus)
        
    if not query_parts:
        print("No fields to update.")
        conn.close()
        return

    sql_statement = f"UPDATE carDetails SET {', '.join(query_parts)} WHERE car_id = ?"
    update_data.append(car_id)

    try:
        cursor.execute(sql_statement, tuple(update_data))
        conn.commit()
        print(f"Car with ID {car_id} updated successfully 👍")
        print(f"Number of rows updated: {cursor.rowcount}")
    except sqlite3.IntegrityError as e:
        print(f"Update failed due to an integrity error: {e}")
    except sqlite3.Error as e:
        print(f"An SQLite error occurred: {e}")
    finally:
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

def approveCarRent(car_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE carDetails SET bookingStatus = ? WHERE car_id = ?", ("approved", car_id))
        conn.commit()
        print("Request approved")
    except sqlite3.IntegrityError as e:
        print(f"Booking Failed: {e}")
    conn.close()