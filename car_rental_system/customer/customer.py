class customer:
    def __init__(self, choice):
        self.choice == choice
    
    #---------- get the option from user and validate it ----------
    def customerChoice():
        choice = input("Please choose number from menu(1 to 4): ")
        is_valid, message = menuValidation(choice) # passing user input for validation
        if is_valid:
            print(f"{message}")
        elif not is_valid:
            print(f"{message}")
    # messageText()


def customerMenu():
    print("1. View Available Cars")
    print("2. Book Car for a rent")
    print("3. Cancel Booking")
    print("4. View booked car")
    customerChoice()

#---------- get the option from user and validate it ----------
def customerChoice():
    choice = input("Please choose number from menu(1 to 4): ")
    is_valid, message = menuValidation(choice) # passing user input for validation
    if is_valid:
        print(f"{message}")
    elif not is_valid:
        print(f"{message}")
    # messageText()

# ---------- Validation ----------
def menuValidation(choice):
    if choice not in ("1", "2", "3", "4"):
        return False, "Please choose number between 1 to 4 from menu"
    return True, "Validation successful"

def runMenu():
    customerMenu()

if __name__ == "__main__":
    runMenu()