#Encapsulation hides how data is stored or protected,
# while abstraction hides how things work 
# — both aim to reduce complexity, but from different angle

# class BadBankAccount:
#     def __init__(self, balance):
#         self.balance = balance

# account = BadBankAccount(500)
# account.balance = -1
# print(account.balance)

class BankAccount:
    def __init__(self):
        self.__balance = 0.0 #encapsulated private / protected _

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit: Invalid number")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(" Withdraw: Invalid number")
        if amount >= self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
account = BankAccount()
print(account.balance)
account.deposit(199)
print(account.balance)
account.withdraw(100)
print(account.balance)
