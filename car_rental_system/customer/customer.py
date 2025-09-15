from admin.carDetail.carManage import view_cars
class customer:
    def __init__(self, choice):
        self.choice = choice

    def viewAvailableCars(self):
        print("----- Available Cars -----")
        rows = view_cars()
        if len(rows) > 0:
            for availability in rows:
                if availability[4] == "yes":
                    print(availability)
        else:
            print("No any cars are available")


def customerMenu():
    print("1. View Available Cars")
    print("2. Book Car for a rent")
    print("3. Cancel Booking")
    print("4. View booked car")
    print("5. Exit")

#---------- get the option from user and validate it ----------
def customerChoice():
    while True:
        customerMenu()
        choice = input("Please choose number from menu(1 to 5): ")
        customerChoice = customer(choice)
        if choice == "1":
            customerChoice.viewAvailableCars()
        elif choice == "2":
            print("book a car")
        elif choice == "3":
            print("cancle booking")
        elif choice == "4":
            print("View Booked Car")
        elif choice == "5":
            break
        else:
            print("Please choose number between 1 to 5 from menu")

def runCustomerMenu():
    customerChoice()