from admin.carDetail.carManage import view_cars
from customer.customerManage import bookCar_customer, cancel_booking
# from admin.carDetail.carManage import search_user

booked_cars = []
class customer:
    def __init__(self, choice, data):
        self.choice = choice
        self.__userId = str(data[0])
    def viewAvailableCars(self):
        print("----- Available Cars -----")
        rows = view_cars()
        availableCar = ""
        if len(rows) > 0:
            for availability in rows:
                if availability[4].lower() == "yes":
                    availableCar = availability
                    print(availability)
            if availableCar == "":
                print("No any cars are available")
            
        else:
            print("No any cars are available")

    def validation(confirmation, car_id, duration):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No", "yes", "no", "YES", "NO"):
            return False, "Please enter Yes/No"
        if confirmation == ("n", "no", "No", "NO"):
            return False, "Exiting..."
        if not car_id:
            return False, "Please enter car ID"
        if not duration:
            return False, "Please enter for howmany days you need car"
        # if isinstance(userId, str):
        #     return False, "Please enter number only"
        if car_id.isdigit() == False:
            return False, "❌ Please enter number only"
        if duration.isdigit() == False:
            return False, "❌ Please enter number only"
        return True, "Successfully validate"
    def cancleBookingValidation(confirmation, car_id):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No", "yes", "no", "YES", "NO"):
            return False, "Please enter Yes/No"
        if confirmation == ("n", "no", "No", "NO"):
            return False, "Exiting..."
        if not car_id:
            return False, "Please enter car ID"
        if car_id.isdigit() == False:
            return False, "❌ Please enter number only"
        return True, "Successfully validate"
    
    def carBooking(self, data):
        car_id = input("Please enter the id of car you want to book: ")
        rentDuration = input("For howmany days you want to rent a car: ")
        confirmation = input("Are you sure (y/n): ")
        is_valid, message = customer.validation(confirmation, car_id, rentDuration) ## storing message and boolean
        if is_valid:
            bookCar_customer(data, car_id, rentDuration)
        else:
            print(f"Error: {message}")
    def bookedCars(self):
        myCar = view_cars()
        available = []
        booked_cars = []
        # print(myCar)
        if len(myCar) > 0:
            for myCars in myCar:
                if myCars[9] == str(self.__userId):
                    print(myCars)
                    available.append(myCars)
                    booked_cars.append(myCars)
                    print(f"The price of {myCars[1]} is: {int(myCars[10]) * 2000} for {myCars[10]} days")
            if available==[]:
                    print("You didn't book any car")
        else:
                    print("You didn't book any car")
    def cancelBooking(self):
        customer.bookedCars(self)
        carId = input("To cancel booking please enter car id: ")
        confirmation = input("Are you sure you want to cancel(y/n): ")

        is_valid, message = customer.cancleBookingValidation(confirmation, carId)
        if is_valid:
            bookingCancle = True
            if booked_cars!=[]:
                for cars in booked_cars:
                    if booked_cars[0] == int(carId):
                        print(f"I am booked cars: {cars}")
                        cancel_booking(carId)
                    else:
                        bookingCancle == False
                if bookingCancle == False:
                    print("No any cars are booked to cancel")

            else:
                print("No any cars are booked")
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
        customerChoice = customer(choice, data)
        if choice == "1":
            customerChoice.viewAvailableCars()
        elif choice == "2":
            print("------ Book a car -----")
            car = view_cars()
            availableCar = []
            if len(car) > 0:
                for cars in car:
                    if cars[4].lower() == "yes":
                        print(cars)
                        availableCar.append(cars)
                        # print(f"The price for this car is: Rs. {}")
                        # print(f"I am availableCar: {availableCar}")
                        # customerChoice.carBooking(data)
                if availableCar==[]:
                    print("No any car available for booking")
                elif availableCar!=[]:
                    customerChoice.carBooking(data)

            else:
                print("No any car available for booking")
        elif choice == "3":
            print("----- Cancel Booking -----")
            customerChoice.cancelBooking()
        elif choice == "4":
            print("----- View Booked Car -----")
            customerChoice.bookedCars()
        elif choice == "5":
            break
        else:
            print("Please choose number between 1 to 5 from menu")

def runCustomerMenu(data):
    customerChoice(data)