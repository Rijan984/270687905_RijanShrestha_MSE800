### **Car Rental System**

This is a console-based Car Rental System developed using Python and SQLite. The application allows different user roles—Customer, Admin, and Super Admin—to manage car rentals through a command-line interface. The system's design incorporates Object-Oriented Programming (OOP) principles and a modular architecture to ensure a robust and maintainable solution.



#### Key Features

#### Customer

* Register: Create a new user account.
* Log In: Access the customer dashboard.
* View Cars: Browse all cars available for rent.
* Book a Car: Submit a rental request for a specific car.
* Cancel Booking: Cancel a pending booking.
* View Booked Cars: Check the status of their own booked cars.



#### Admin

* Log In: Access the admin dashboard.
* Car Management: Add, view, update, and delete their own car listings.
* Approve Rent: Approve or deny customer rental requests.



#### Super Admin

* Log In: Access the super admin dashboard.
* User Management: View and delete any user from the system.
* Car Management: View and delete any car listing in the system.



#### How to Run the Project

* Prerequisites: Ensure you have Python 3.x installed. The project uses the built-in sqlite3 and re libraries, so no additional installations are required.
* Run the application: Navigate to the project directory in your terminal and run the main file.
* &nbsp;	Bash
* &nbsp;	python main.py
* Database: The first time you run the application, it will automatically create a database file named users.db and set up the necessary tables (userRegister and carDetails).



#### Project Structure

The project is organized into a clean, modular structure to separate concerns:



.

├── admin

│   ├── \_\_init\_\_.py

│   ├── admin.py             # Admin menu \& logic

│   ├── carDetail            # Car management module

│   │   ├── \_\_init\_\_.py

│   │   ├── car.py           # Class for car details \& validation

│   │   └── carManage.py     # DB operations for cars

│   └── superAdmin.py        # Super Admin menu \& logic

├── customer

│   ├── \_\_init\_\_.py

│   ├── customer.py          # Customer menu \& logic

│   └── customerManage.py    # DB operations for customer bookings

├── login\_signup

│   ├── \_\_init\_\_.py

│   ├── login.py             # User login logic

│   └── signup.py            # User registration logic

├── database

│   ├── \_\_init\_\_.py

│   └── database.py          # Database connection \& table creation

├── main.py                  # Main entry point of the application

└── userManage.py            # DB operations for users



#### Design \& Architecture



The system's design is based on a modular architecture, with a clear separation of concerns. This approach allows for easier maintenance and scalability.



* Data Model: A simple and effective data model uses two relational tables: userRegister and carDetails. An Entity-Relationship Diagram (ERD) would show a one-to-many relationship, where a single admin can manage multiple cars.
* UML Diagrams: The system's design is further documented through UML diagrams, including Use Case, Class, and Sequence Diagrams, which visually represent its functionality and internal workflows.



#### Object-Oriented Programming (OOP) Concepts

This project effectively applies key OOP principles:



* Encapsulation: This is demonstrated by several classes, such as loginUser and addCarDetails. They encapsulate data and the methods that operate on that data. Sensitive information like passwords and admin IDs are protected using private attributes (\_\_password, \_\_admin\_id), which can only be accessed or modified through a class's methods.
* Other Concepts: The project's design is primarily procedural, with dedicated modules for different functions. While it does not utilize Inheritance or Polymorphism in its class structure, it successfully implements Encapsulation to enhance data integrity and security.





Author: Rijan Shrestha (270687905)

Course: MSE800 Professional Software Engineering

