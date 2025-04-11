## Author: Robot Group 1
## Date: 2025-04-08
## Description: HAB Taxi Service Company Service System

# import libraries
import datetime

# Constants 
CUR_DATE = datetime.datetime.now()
ALLOWED_CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ .-'abcdefghijklmnopqrstuvwxyz0123456789")

# Functions
# Open Defaults.dat
def _openDefaults():
    try:
        with open("Defaults.dat", "r") as f:
            nextTransactionNumber = int(f.readline())
            nextDriverNumber = int(f.readline())
            monthlyStandFee = float(f.readline())
            dailyRentalFee = float(f.readline())
            weeklyRentalFee = float(f.readline())
            hstRate = float(f.readline())
        return nextTransactionNumber, nextDriverNumber, monthlyStandFee, dailyRentalFee, weeklyRentalFee, hstRate
    except:
        # create Defaults.dat if it doesn't exist
        with open("Defaults.dat", "w") as f:
            f.write("1\n")
            f.write("1\n")
            f.write("0.00\n")
            f.write("0.00\n")
            f.write("0.00\n")
            f.write("0.00\n")
            f.write("0.15\n")  
        # return default values  
        return 1, 1, 0.00, 0.00, 0.00, 0.15
    
def _getDate():
    # Get the current date
    today = CUR_DATE
    # Format the date as YYYY-MM-DD
    formattedDate = today.strftime("%Y-%m-%d")
    return formattedDate

# Get total revenue, HST, and total amount
def _getTotalRevenue():
    global revenues, hstRate
    revenue = sum(revenues)
    hst = revenue * hstRate
    total = revenue + hst
    return revenue, hst, total

# Save defaults to Defaults.dat
def _saveDefaults():
    with open("Defaults.dat", "w") as f:
        f.write(str(nextTransactionNumber) + "\n")
        f.write(str(nextDriverNumber) + "\n")
        f.write(str(monthlyStandFee) + "\n")
        f.write(str(dailyRentalFee) + "\n")
        f.write(str(weeklyRentalFee) + "\n")
        f.write(str(hstRate) + "\n")

# Print values Defaults.dat
def _printDefaults ():
    print("Defaults.dat:")
    with open("Defaults.dat", "r") as f:
        for line in f:
            print(line.strip())

_openDefaults()

# Get current date
_getDate()

# Load defaults
nextTransactionNumber, nextDriverNumber, monthlyStandFee, dailyRentalFee, weeklyRentalFee, hstRate = _openDefaults()

# Tables
employees = []
revenues = []
expenses = []
carRentals = []
payments = []

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
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Quit Program.")
    print("\n")
    
    # Get user input for choice number
    choice = input("Enter a Choice (1-8): ")

    # Validate choice number
    if choice.isdigit() == False:
        # If invalid, ask for input again
        print("Invalid choice. Please enter a number between 1 and 8.")
    elif int(choice) < 1 or int(choice) > 8:
        # If invalid, ask for input again
        print("Invalid choice. Please enter a number between 1 and 8.")
    else:
        print("You have selected: " + str(choice))

    # Input and validation for employee name
    if choice == 1:
        name = input("Enter Employee (Driver) name: ")
        if name == "" or set(name).issubset(ALLOWED_CHARS) == False:
            print("Invalid name.")
        else:
            employees.append(name)
            print("Employee name is " + str(employees))
        
    # Input and validation for revenue amount
    elif choice == 2:
        revenueAmount = float(input("Enter revenue amount: "))
        if revenueAmount < 0:
            print("Invalid revenue amount.")
        else:
            revenues.append(revenueAmount)
            print("Revenue amount is " + str(revenueAmount))

    # Input and validation for expense amount
    elif choice == 3:
        expenseAmount = float(input("Enter expense amount: "))
        if expenseAmount < 0: 
            print("Invalid expense amount.")
        else:
            expenses.append(expenseAmount)
            print("Expense amount is " + str(expenseAmount))

    # Input and validation for car rental info
    elif choice == 4:
        carRentalInfo = input("Enter car rental info: ")
        if carRentalInfo == "" or set(carRentalInfo).issubset(ALLOWED_CHARS) == False:
            print("Invalid car rental info.")
        else:
            carRentals.append(carRentalInfo)
            print("Car rental info: \n" + str(carRentalInfo))
            
    # Input and validation for employee payment info
    elif choice == 5:
        payment = float(input("Enter employee payment info: "))
        if payment < 0:
            print("Invalid payment amount.")
        else:
            payments.append(payment)
            print("Employee payment: " + str(payment))

    # Print company profit listing
    elif choice == 6:
        if not revenues or not expenses:
            print("Insufficient data to calculate profit.")
        else:
            totalRevenue = sum(revenues)
            totalExpenses = sum(expenses)
            profit = totalRevenue - totalExpenses
            print(f"Total Revenue: ${totalRevenue:.2f}")
            print(f"Total Expenses: ${totalExpenses:.2f}")
            print(f"Profit: ${profit:.2f}")

    # Print driver financial listing
    elif choice == 7:
        employeeNum = input("Enter employee Number: ")
        if employeeNum.isdigit() == False or int(employeeNum) < 0:
            print("Invalid employee Number.")
        else:
            print("Driver Financial Listing:")
            print(f"name: {name}")
            ##print(f"Date Range: ")
            transaction_date = _getDate()
            print(f"Transaction Date: {transaction_date}")
            print(f"Employee Number: {employeeNum}")
            revenue, hst, total = _getTotalRevenue()
            print(f"Revenue: ${revenue:.2f}")
            print(f"HST: ${hst:.2f}")
            print(f"Total: ${total:.2f}")

    # Quit program
    elif choice == 8:
        print("Exiting program.")
        break

_saveDefaults()
_printDefaults()

