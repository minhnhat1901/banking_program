def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    
    if amount < 0:
        print("Cannot enter negative amount. Please try again.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: "))
    
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Cannot enter negative amount.")
        return 0
    else:
        return amount

def main():
    balance = 0.00
    is_running = True
    welcome_message = "Welcome to Python Banking Program"
    print(f"{welcome_message}")
    
    while is_running:
        print('-' * len(welcome_message))
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please try again.\n")

    print("Thank you for using Python Banking Program. Have a nice day!")