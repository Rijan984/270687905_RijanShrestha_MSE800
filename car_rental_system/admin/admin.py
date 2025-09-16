from userManage.userManage import view_users, delete_user
from admin.carDetail.car import addCarDetail, viewCars, deleteCar
from admin.carDetail.carManage import view_cars


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
                if carData[8]==data[0]:
                    if carData[7] == "pending":
                        print(carData)
                    elif carData[7] == "available":
                        print("No any request for booking")

# class deleteUsers:
def menuSelelction(data):
    print(f"Welcome {data[1].capitalize()} {data[2].capitalize()}")
    print("1. Add Cars")
    print("2. View Cars")
    print("3. Delete Cars")
    print("4. Aprove Rent")
    print("5. Exit")
    # adminMenu()


def adminMenu(data):
    while True:
        menuSelelction(data)
        selectMenu = input("Please choose between 1 to 5: ")
        if selectMenu not in ("1", "2", "3", "4", "5"):
            print("Please choose between 1 to 5 only")
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
                    if carData[8]==data[0]:
                        print(carData)
        elif selectMenu == "3":
            print("-----Deleting Car-----")
            deleteCar()
        elif selectMenu == "4":
            aprove_car_rent(data)
        elif selectMenu == "5":
            print("Exiting...")
            break