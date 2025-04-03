class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance  # Initial balance

    def deposit(self, amount):
        self.balance += amount  # Correctly updates balance
        print(f"Deposited amount: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount  # Correctly updates balance
            print(f"Withdrawn amount: {amount}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")  # Now shows updated balance

def main():
    bank = Bank("ABC Bank")
    while True:
        print("\nWelcome to ABC Bank!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            bank.deposit(amount)  # Deposit now correctly updates balance
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(amount)  # Withdraw now correctly updates balance
        elif choice == '3':
            bank.check_balance()  # Balance will now display correctly
        elif choice == '4':
            print("Thank you for using ABC Bank!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
