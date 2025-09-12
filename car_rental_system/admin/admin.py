from userManage.userManage import view_users, delete_user

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
        print("No any user found")
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
        id = int(userId)
        delete_user(id)
        viewUser()
    else:
         print(f"Error: {message}")

# class deleteUsers:

def menuSelelction():
    selectMenu = input("Please choose between 1 to 4: ")
    if selectMenu not in ("1", "2", "3", "4"):
        print("Please choose between 1 to 4 only")
    if selectMenu == "1":
        deleteUser()
    elif selectMenu == "2":
        print("Car added")
    elif selectMenu == "3":
        print("Car deleted")
    elif selectMenu == "4":
        print("Car Rent Approved")

def adminMenu():
    print("1. Delete Users")
    print("2. Add Cars")
    print("3. Delete Cars")
    print("4. Aprove Rent")
    # adminMenu()
    menuSelelction()