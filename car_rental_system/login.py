from userManage.userManage import userLogin
class loginUser:
    def __init__(self, email, password):
        self._email=email
        self.__password=password

    def validation(self, confirmation):
        if confirmation not in ("y", "n", "Y", "N", "Yes", "No"):
            return False, "Please enter Yes/No"
        if not self._email or not self.__password:
            return False, "Please enter all the login details"
        return True, "Successfully validate"
    def userSearch(self, is_valid, message):
        if not is_valid:
            print(message)
        if is_valid:
            # print(message)
            data = userLogin(self._email, self.__password) ## will search on database
            # print(data)
            if data:
               print("Successfully Login")
            else:
                print("Please enter correct credentials")
    
def loginDetail():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    confirmation = input("Do you want to continue(y/n): ")
    loginClass = loginUser(email, password)
    # loginClass.validation(confirmation)
    is_valid, message = loginClass.validation(confirmation)
    loginClass.userSearch(is_valid, message)