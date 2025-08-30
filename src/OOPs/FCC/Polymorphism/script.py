#Polymorphism

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
    def __init__(self, brand, model, year, noofwheels):
        super().__init__(brand, model, year)
        self.noofwheels = noofwheels

    def start(self):
        print("Car is starting...")
    
    def stop(self):
        print("Car is stopping...")

class Bike(Vehicle):
    def __init__(self, brand, model, year, noofwheels):
        super().__init__(brand, model, year)
        self.noofwheels = noofwheels

    def start(self):
        print("Bike is starting...")
    
    def stop(self):
        print("Bike is stopping...")

vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 1998, 4),
    Bike("yamaha","RX",1999,2)
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} model {vehicle.model}({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
    
    
    
    
    # if isinstance(vehicle, Vehicle):
    #     print(f"Inspecting {vehicle.brand} model {vehicle.model} ({type(vehicle).__name__})")
    #     vehicle.start()
    #     vehicle.stop()
    # else:
    #     raise Exception("Object is a valid vehicle")
