from userManage.userManage import userLogin
from admin.admin import adminMenu
from admin.superAdmin import superAdminMenu
from customer.customer import runCustomerMenu
class loginUser:
    def __init__(self, email, password):
        self._email=email
        self.__password=password

    def validation(self, confirmation):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No", "yes", "no", "YES", "NO"):
            return False, "Please enter Yes/No"
        if not self._email or not self.__password:
            return False, "Please enter all the login details"
        return True, "Successfully validate"
    def userSearch(self, is_valid, message):
        user_id = 0
        if not is_valid:
            print(message)
        elif is_valid:
            # if super admin will redirect to superAdmin pannel if not then will redirect according to the role of the user
            if self._email == "admin" and self.__password == "admin":
                superAdminMenu() 
            else:
                data = userLogin(self._email, self.__password) ## will search on database
                print(f"i am called: {data}")
                if data!=None:
                    user_id == data[0]
                    if data[4]=="admin":
                        print(data)
                        print("I am admin")
                        # loginUser.userId(user_id)
                        adminMenu(data)
                    elif data[4]=="customer":
                        print("-----Customer Menu-----")
                        # loginUser.userId(user_id)
                        runCustomerMenu(data)

                else:
                    print("Please enter correct credentials")
            # else:
    def userId(self, user_id):
        return user_id
                
    
def loginDetail():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    confirmation = input("Do you want to continue(y/n): ")
    loginClass = loginUser(email, password)
    
    is_valid, message = loginClass.validation(confirmation)
    if confirmation not in ("n", "No", "no", "N"):
        loginClass.userSearch(is_valid, message)
    else:
        return False