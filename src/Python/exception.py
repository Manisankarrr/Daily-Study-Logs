#exception

# zerDivisionError, TypeError, ValueError
#  try, except, finally

#1/0 # ZeroDivisionError: division by zero

#1 + "1" #TypeError: unsupported operand type(s) for +: 'int' and 'str

#int("pizza") #ValueError: invalid literal for int() with base 10: 'pizza'

try: 
    num = int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
except Exception:
    print("Something went wrong.")
finally:
    print("This will always run.")


