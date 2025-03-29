# Banking Program

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))

    if amount < 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount < 0:
        print("Withdrawal amount must be positive.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to the Banking Program \n")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)        
            case '4':
                is_running = False
                print("Exiting the Banking Program.")
            case _:
                print("Invalid choice. Please try again.")

    print("Thank you for using the Banking Program!")

if __name__ == "__main__":
    main()

    