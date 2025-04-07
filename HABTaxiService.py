## Date:
## Authors:
## Description:

# import libraries
import datetime

# Open Defaults.dat file and read the contents
f = open("Defaults.dat", "r")
nextTransactionNumber = int(f.readline())
nextDriverNumber = int(f.readline())
monthlyStandFee = float(f.readline())
dailyRentalFee = float(f.readline())
weeklyRentalFee = float(f.readline())
hstRate = float(f.readline())
f.close()

# Constants 
CUR_DATE = datetime.datetime.now()
ALLOWED_CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ .-'abcdefghijklmnopqrstuvwxyz0123456789_")

# Main Program
while True:
    print("\n")
    print(" " * 10 + "HAB Taxi Service")
    print(" " * 7 + "Company Service System")
    print("\n")
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Compnay Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Quit Program.")
    print("\n")
    print(" " * 8 + "Enter a Choice (1-8:)")
    print("\n")
    
    # Exit the program if the user enters 8
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue
    
    # input and validation for the choice
    if choice < 1 or choice > 8:
        print("Invalid choice. Please enter a number between 1 and 8.")
        continue
    
    if choice == 1:
        driver = input("Enter Employee (Driver) name: ")
        if driver == "" or set(driver).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid name.")
        else:
            break 
              
    if choice == 2: 
        revenues = input("Enter Company Revenues: ")
        if revenues == "" or set(revenues).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid revenue.")
        else:
            break
        
    if choice == 3:
        expenses = input("Enter Company Expenses: ")
        if expenses == "" or set(expenses).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid expense.")
        else:
            break
        
    if choice == 4:
        rentals = input("Enter Car Rentals: ")
        if rentals == "" or set(rentals).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid rental.")
        else:
            break
        
    if choice == 5:
        payment = input("Enter Employee Payment: ")
        if payment == "" or set(payment).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid payment.")
        else:
            break
        
    if choice == 6:
        profit = input("Enter Company Profit: ")
        if profit == "" or set(profit).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid profit.")
        else:
            break
        
    if choice == 7:
        financialListing = input("Enter Driver Financial Listing: ")
        if financialListing == "" or set(financialListing).issubset(ALLOWED_CHARS) == False:
            print("Invalid input. Please enter a valid financial listing.")
        else:
            break
    # Exit the program if the user enters 8 
    if choice == 8:
        print("Exiting the program.")
        break
        
