#Inheritance

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting...")
    
    def stop(self):
        print("Vehicle is stopping...")

class Car(Vehicle):
    def __init__(self, brand, model, year, noofdoors, noofwheels):
        super().__init__(brand, model, year)
        self.noofdoors = noofdoors
        self.noofwheels = noofwheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, noofwheels):
        super().__init__(brand, model, year)
        self.noofwheels = noofwheels

car1 = Car("Ford", "Focus", 1998, 5 , 4)
bike1 = Bike("plusar", "N160", 2020, 2)
print(car1.__dict__)
print(bike1.__dict__)

car1.start()
bike1.start()