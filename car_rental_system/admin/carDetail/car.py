from admin.carDetail.carManage import add_car, view_cars, delete_car

class addCarData:
    def __init__(self, model, year, mileage, availability, min_rent_period, max_rent_period):
        self.model = model
        self.year = year
        self.mileage = mileage
        self.availability = availability
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period

    def validation(self):
        if not self.model or not self.year or not self.mileage or not self.availability or not self.min_rent_period or not self.max_rent_period:
            return False, "Please enter all the details"
        if self.availability not in ("yes", "no"):
            print(self.availability)
            return False, "Please enter only yes or no"
        return True, "Validation Successful"
    def addCar(self):
        add_car(self.model, self.year, self.mileage, self.availability, self.min_rent_period, self.max_rent_period) #adding data to database        


def carDetails():
    model = input("Please enter the model of the car: ")
    year = input("Please enter the year of the car: ")
    mileage = input("Please enter the mileage of the car: ")
    availability = input("Please enter the availability of the car: ")
    min_rent_period = input("Please enter the minimun rent period of the car: ")
    max_rent_period = input("Please enter the maximum rent period of the car: ")
    # confirmation = input("Are you sure you want too add car?: ")
    
    #passing the variables to class carData
    car = addCarData(model, year, mileage, availability, min_rent_period, max_rent_period)

    is_valid, message = car.validation() ## will store boolean(True or false) in is_valid and in another message will be stored
    if not is_valid:
        print(f"Error: {message}")
    if is_valid:
        car.addCar() #calling function to add car data to database

def addCarDetail():
    carDetails()

# function to fetch all the cars stored in database
def viewCars():
        cars = view_cars()
        for car in cars:
            print(car)

# function to delete car from database
def deleteCar():
    viewCars()
    carId = int(input("Please enter car ID you want to delete"))
    delete_car(carId) #passing ID to delete car from database
