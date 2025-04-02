from carclass import Car

car1 = Car("mustang", 2020, "red", False, False) # creating object of class Car
car2 = Car("audi", 2021, "black", True, True) # creating object of class Car
car3 = Car("bmw", 2022, "white", True, False) # creating object of class Car
car4 = Car("mercedes", 2023, "blue", False, True) # creating object of class Car

print(car1.model) # accessing attribute of object car1

car2.start() # calling method of object car2
car2.stop() # calling method of object car3

car1.describe() # calling method of object car1
car4.electric() # calling method of object car4