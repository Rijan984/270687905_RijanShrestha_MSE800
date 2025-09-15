from admin.carDetail.carManage import view_cars
from customer.customerManage import bookCar_customer
class customer:
    def __init__(self, choice):
        self.choice = choice

    def viewAvailableCars(self):
        print("----- Available Cars -----")
        rows = view_cars()
        if len(rows) > 0:
            for availability in rows:
                if availability[4] == "yes":
                    print(availability)
        else:
            print("No any cars are available")

    def validation(confirmation, car_id):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No"):
            return False, "Please enter Yes/No"
        if not car_id:
            return False, "Please enter user ID"
        # if isinstance(userId, str):
        #     return False, "Please enter number only"
        if car_id.isdigit() == False:
            return False, "❌ Please enter number only"
        return True, "Successfully validate"
    
    def carBooking(self):
        car_id = input("Please enter the id of car you want to book")
        confirmation = input("Are you sure (y/n): ")
        # if car_id
        is_valid, message = customer.validation(confirmation, car_id) ## storing message and boolean
        if is_valid:
            bookCar_customer(car_id)
        else:
            print(f"Error: {message}")


def customerMenu(data):
    print(f"Welcome {data[1].capitalize()} {data[2].capitalize()}")
    print("1. View Available Cars")
    print("2. Book Car for a rent")
    print("3. Cancel Booking")
    print("4. View booked car")
    print("5. Exit")

#---------- get the option from user and validate it ----------
def customerChoice(data):
    while True:
        customerMenu(data)
        choice = input("Please choose number from menu(1 to 5): ")
        customerChoice = customer(choice)
        if choice == "1":
            customerChoice.viewAvailableCars()
        elif choice == "2":
            print("book a car")
            customerChoice.carBooking()
        elif choice == "3":
            print("cancle booking")
        elif choice == "4":
            print("View Booked Car")
        elif choice == "5":
            break
        else:
            print("Please choose number between 1 to 5 from menu")

def runCustomerMenu(data):
    customerChoice(data)