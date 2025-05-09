#Edit config so that it can run without running main.py like import files(math)

# print(dir())

# print(__name__) #__main__  #__name__ is a built-in variable that represents the name of the module or script being executed.

from script1 import foods # Import everything from script1

def drinks(drink):
    print(f"drinks: {drink}")

def main():
    print("Script 2")
    foods("Burger")
    drinks("Coke")
    print("Script 2 is done")

if __name__  == '__main__':
    main()  