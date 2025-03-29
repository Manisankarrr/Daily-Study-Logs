from script2 import * # Import everything from script2

def foods(food): # third
    print(f"food: {food}")
def main(): # second
    print("script1 is being run directly")
    foods("pizza")
    drinks("water") # Call drinks function from script2
    print("script1 is done")

if __name__ == "__main__": # first running
    main()