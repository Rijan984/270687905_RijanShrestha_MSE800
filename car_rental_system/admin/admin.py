from userManage.userManage import view_users, delete_user
from admin.carDetail.car import addCarDetail, viewCars, deleteCar
from admin.carDetail.carManage import view_cars, update_car


def validation(confirmation, userId):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No"):
            return False, "Please enter Yes/No"
        if not userId:
            return False, "Please enter user ID"
        # if isinstance(userId, str):
        #     return False, "Please enter number only"
        if userId.isdigit() == False:
            return False, "Please enter number only"
        return True, "Successfully validate"

def viewUser():
    userdata = view_users()
    if userdata ==[]:
        print("❌ No any user found")
    else:
         for user in userdata:
            print(f"i am called: {user}")

def deleteUser():
    print("-------User Details-------")
    viewUser()
    
    print("----------Delete User----------")
    userId = input("Please enter user ID of user you want to delete: ")
    confirmation = input("Are you sure(y/n): ")
    ## authentication for confirmation
    print(userId)
    # validation(confirmation)
    
    is_valid, message = validation(confirmation, userId) ## storing message and boolean

    if is_valid:
        id = userId
        delete_user(id)
        viewUser()

    else:
         print(f"Error: {message}")

def aprove_car_rent(data):
        car = view_cars()
        if len(car) < 1:
            print("No car available")
        else:
            for carData in car:
                # if carData[8]==data[0]:
                if carData[7] == "pending":
                    print(carData)
                elif carData[7] == "available":
                    print("No any request for booking")

# def updateCar_validation(car_id, new_model, new_year, new_mileage, new_availability, new_min_rent_period, new_max_rent_period, new_bookingStatus):
#         # if not new_model or not new_year or not new_mileage or not new_availability or not new_min_rent_period or not new_max_rent_period:
#         #     return False, "-----> Please enter all the details"
#         if new_availability not in ("yes", "no"):
#             print(new_availability)
#             return False, "-----> Please enter only yes or no"
#         return True, "Validation Successful"
def updateCar():
    car_id = input("Please enter the id of the car you want to update: ")
    new_model = input("Please enter the model of the car: ")
    new_year = input("Please enter the year of the car: ")
    new_mileage = input("Please enter the mileage of the car: ")
    new_availability = input("Please enter the availability of the car (yes/no): ")
    new_min_rent_period = input("Please enter the minimun rent period of the car: ")
    new_max_rent_period = input("Please enter the maximum rent period of the car: ")
    new_bookingStatus = "available"
    
    update_car(car_id, new_model, new_year, new_mileage, new_availability, new_min_rent_period, new_max_rent_period, new_bookingStatus)
    # is_valid, message = updateCar_validation(car_id, new_model, new_year, new_mileage, new_availability, new_min_rent_period, new_max_rent_period, new_bookingStatus) ## will store boolean(True or false) in is_valid and in another message will be stored
    # if not is_valid:
    #     print(f"Error: {message}")
    # if is_valid:
    #     update_car()

# class deleteUsers:
def menuSelelction(data):
    print(f"Welcome {data[1].capitalize()} {data[2].capitalize()}")
    print("1. Add Cars")
    print("2. View Cars")
    print("3. Delete Cars")
    print("4. Aprove Rent")
    print("5. Exit")
    print("6. Update Car details")
    # adminMenu()


def adminMenu(data):
    while True:
        menuSelelction(data)
        selectMenu = input("Please choose between 1 to 6: ")
        if selectMenu not in ("1", "2", "3", "4", "5", "6"):
            print("Please choose between 1 to 6 only")
        # if selectMenu == "1":
        #     deleteUser()
        if selectMenu == "1":
            print("-----Adding Car-----")
            addCarDetail(data)
        elif selectMenu == "2":
            print("-----Car Detailssssss-----")
            car = view_cars()
            if len(car) < 1:
                print("No car available")
            else:
                for carData in car:
                    # if carData[8]==data[0]:
                    print(carData)
        elif selectMenu == "3":
            print("-----Deleting Car-----")
            deleteCar()
        elif selectMenu == "4":
            aprove_car_rent(data)
        elif selectMenu == "5":
            print("Exiting...")
            break
        elif selectMenu == "6":
            car = view_cars()
            for carData in car:
                print(carData)
            updateCar()