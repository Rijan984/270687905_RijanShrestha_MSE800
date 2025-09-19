from userManage.userManage import view_users, delete_user
from admin.carDetail.car import addCarDetail, viewCars, deleteCar
from admin.carDetail.carManage import view_cars

def viewUser():
    userdata = view_users()
    if userdata ==[]:
        print("No any user found")
    else:
         for user in userdata:
            print(f"i am called: {user}")

def validation(confirmation, userId):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No"):
            return False, "Please enter Yes/No"
        if not userId:
            return False, "Please enter user ID"
        # if isinstance(userId, str):
        #     return False, "Please enter number only"
        if userId.isdigit() == False:
            return False, "❌ Please enter number only"
        return True, "Successfully validate"

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
        id = int(userId)
        delete_user(id)
        viewUser()
    else:
         print(f"Error: {message}")

def menuSelelction():
    print("---------- I Am Super Admin ----------")
    print("1. View Users")
    print("2. Delete Users")
    print("3. View Cars")
    print("4. Delete Cars")
    print("5. Exit")


def superAdminMenu():
    while True:
        menuSelelction()
        selectMenu = input("Please choose between 1 to 5: ")
        if selectMenu not in ("1", "2", "3", "4", "5"):
            print("Please choose between 1 to 4 only")
        if selectMenu == "1":
            users = view_users()
            for user in users:
                print("----- Here are the list of the users -----")
                print(user)
        elif selectMenu == "2":
            deleteUser()
        elif selectMenu == "3":
            print("-----Car Details-----")
            carData = view_cars()
            
            if carData == None:
                print("No car available")
            else:
                for cars in carData:
                    print(cars)
        elif selectMenu == "4":
            print("-----Deleting Car-----")
            deleteCar()
        elif selectMenu == "5":
            print("Exiting...")
            break