from admin.carDetail.carManage import add_car, view_cars, delete_car

class addCarDetails:
    def __init__(self, model, year, mileage, availability, min_rent_period, max_rent_period, bookingStatus, admin_id, bookedBy):
        self.model = model
        self.year = year
        self.mileage = mileage
        self.availability = availability
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period
        self.bookingStatus = bookingStatus
        self.__admin_id = admin_id
        self.__bookedBy = bookedBy
    def validation(self):
        if not self.model or not self.year or not self.mileage or not self.availability or not self.min_rent_period or not self.max_rent_period:
            return False, "-----> Please enter all the details"
        if self.availability not in ("yes", "no"):
            print(self.availability)
            return False, "-----> Please enter only yes or no"
        return True, "Validation Successful"
    def addCar(self):
        add_car(self.model, self.year, self.mileage, self.availability, self.min_rent_period, self.max_rent_period, self.bookingStatus, self.__admin_id, self.__bookedBy) #adding data to database        


def carDetails(data):
    model = input("Please enter the model of the car: ")
    year = input("Please enter the year of the car: ")
    mileage = input("Please enter the mileage of the car: ")
    availability = input("Please enter the availability of the car (yes/no): ")
    min_rent_period = input("Please enter the minimun rent period of the car: ")
    max_rent_period = input("Please enter the maximum rent period of the car: ")
    bookingStatus = "available"
    admin_id = data[0]
    bookedBy = "None"
    # confirmation = input("Are you sure you want too add car?: ")
    
    #passing the variables to class carData
    car = addCarDetails(model, year, mileage, availability, min_rent_period, max_rent_period, bookingStatus, admin_id, bookedBy)

    is_valid, message = car.validation() ## will store boolean(True or false) in is_valid and in another message will be stored
    if not is_valid:
        print(f"Error: {message}")
    if is_valid:
        car.addCar() #calling function to add car data to database

def addCarDetail(data):
    carDetails(data)

# function to fetch all the cars stored in database
def viewCars():
        cars = view_cars()
        for car in cars:
            return car

# function to delete car from database
def deleteCar():
    viewCars()
    carId = input("Please enter car ID you want to delete: ")
    if len(carId) > 0:
        if any(char.isalpha() for char in carId):
            print("❌ Please enter only numbers")
        else:
            delete_car(carId) #passing ID to delete car from database
    else:
        print("❌ Please enter car ID to delete: ")
