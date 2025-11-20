# ATM Simulation Project

This is a simple ATM simulation written in Python.

## Files
- atm_simulation.py : main program
- statement.md : problem statement
- README.md : basic project info
# ATM Simulation Project

This is a simple ATM simulation written in Python.

## Files
- atm_simulation.py : main program
- statement.md : problem statement
- README.md : basic project info
# ATM Simulation Project (CSE1021)

This project is developed as part of the Build Your Own Project requirement for the 
course **CSE1021 – Introduction to Problem Solving and Programming**.

---

## Project Description
A Python-based ATM simulation system implementing the following functionalities:
- PIN Authentication  
- Balance Inquiry  
- Cash Withdrawal  
- Cash Deposit  
- Transaction History  
- Error Handling  
- Menu-driven interface  

The project also includes system design elements such as flowcharts, architecture 
diagrams, UML diagrams (use case, sequence, class), and a complete test case table.

---

## Files Included
- **atm_simulation.py** – Python source code  
- **ATM project report.docx.pdf** – Project documentation  
- **statement.md** – Problem statement  
- **assets/** – Contains flowchart, system architecture, UML diagrams, and screenshots  
- **README.md** – GitHub documentation file  

# ATM Simulation Program

balance = 10000
pin = "1234"
transactions = []

def authenticate():
    attempts = 0
    while attempts < 3:
        user_pin = input("Enter your PIN: ")

        if user_pin == pin:
            print("PIN verified successfully.\n")
            return True

        else:
            attempts += 1
            print("Incorrect PIN. Attempts left:", 3 - attempts)

    print("Too many incorrect attempts. Card blocked.")
    return False


def check_balance():
    print("\nYour current balance is: ₹", balance)
    transactions.append("Checked Balance")


def withdraw():
    global balance
    amount = int(input("\nEnter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrawal successful! New balance: ₹", balance)
        transactions.append(f"Withdrew ₹{amount}")


def deposit():
    global balance
    amount = int(input("\nEnter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount!")
    else:
        balance += amount
        print("Deposit successful! New balance: ₹", balance)
        transactions.append(f"Deposited ₹{amount}")


def show_transactions():
    print("\nTransaction History:")
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)


def main_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


# MAIN PROGRAM FLOW
print("----- Welcome to the ATM Simulation -----")

if authenticate():
    main_menu()


---

## How to Run the Program
1. Install Python 3  
2. Download the project folder or clone the GitHub repo  
3. Open Command Prompt or Terminal inside the project folder  
4. Run the program:



