from database.database import create_table
from userManage.userManage import add_user, view_users
from login_signup.login import loginDetail
import re
class person:
    def __init__(self, fname, lname, pnumber, role, email, password):
        self.fname=fname
        self.lname=lname
        self._role=role
        self._pnumber=pnumber
        self._email=email
        self.__password=password
     ## function to validate user details   
    def validate(self):
        if not self.fname or not self.lname:
            return False, "First name and Last name can't be empty"
        if not self._pnumber:
            return False, "Please fill all the details"
        if not self._email:
            return False, "Please fill all the details"
        if not re.fullmatch(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", self._email):
            return False, "Invalid email address."
        if self._role not in ("admin", "customer"):
            return False, "Please enter admin or customer"
        if not self.__password:
            return False, "Please fill all the details"
        if len(self.__password) < 8:
            return False, "Password must be 8 characters long"
        return True, "Validation Success"
    
    # def successRegister(self):


def userDetail():
    fname = input("enter your first name: ").lower()
    lname = input("enter your last name: ").lower()
    pnumber = input("enter your contact number: ").lower()
    role = input("enter role (admin/customer): ").lower()
    email = input("enter your email: ").lower()
    password = input("enter your new password: ")

    userValidation = person(fname, lname, pnumber, role, email, password) 
    is_valid, message=userValidation.validate()
    if not is_valid:
        print(f"Error: {message}")
    if is_valid:
        add_user(fname, lname, pnumber, role, email, password) ##sending data to database
    

# def userMenu():
#     ## options for user to select where to rediirect
#     print('1. Register')
#     print('2. Login')
#     print('3. Exit')
#     print('4. view users')

# def menuRedirect():
#     create_table()
#     while True:
#         userMenu()
#         choice = input("Please select (1, 2, 3 or 4): ")
#         if choice == '1':
#             # this function will redirect user where user will able create account 
#             userDetail()
#         elif choice == '2':
#             # login()
#             loginDetail()
#             # print("I am user")
#         elif choice == '3':
#             print("Exiting..")
#             break
#         elif choice == '4':
#             users = view_users()
#             for user in users:
#                 print(f"i am called: {user}")
#         else:
#             print("invalid choice")

# def main():
#     menuRedirect()


# if __name__ == "__main__":
#     main()
