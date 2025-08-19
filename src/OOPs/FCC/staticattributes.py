class bankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if self._isvalid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Invalid number")

    def _isvalid_amount(self,amount): #protected
        return amount > 0
    
    def __log_transaction(self,transaction, amount): #private
        print(f"Logging the {transaction} of ${amount}. New balance = ${self._balance}")
    
    @staticmethod
    def isvalid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = bankAccount("Manish", 300)
account.deposit(200)

print(bankAccount.isvalid_interest_rate(3))
print(bankAccount.isvalid_interest_rate(9))
