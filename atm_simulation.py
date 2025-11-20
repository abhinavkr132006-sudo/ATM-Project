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
