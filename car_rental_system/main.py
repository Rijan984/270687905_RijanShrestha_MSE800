from database.database import create_table
# from userManage.userManage import add_user, view_users
from login_signup.login import loginDetail
from login_signup.signup import userDetail

def userMenu():
    ## options for user to select where to rediirect
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    # print('4. view users')

def menuRedirect():
    create_table()
    while True:
        userMenu()
        choice = input("Please select (1, 2, or 3): ")
        if choice == '1':
            # this function will redirect user where user will able create account 
            userDetail()
        elif choice == '2':
            # login()
            loginDetail()
            # print("I am user")
        elif choice == '3':
            print("Exiting..")
            break
        # elif choice == '4':
        #     users = view_users()
        #     for user in users:
        #         print(f"i am called: {user}")
        else:
            print("invalid choice")

def main():
    menuRedirect()


if __name__ == "__main__":
    main()