#Polymorphism

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting...")
    
    def stop(self):
        print("Car is stopping...")

class Bike:
    def __init__(self, brand, model, year ):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Bike is starting...")
    
    def stop(self):
        print("Bike is stopping...")
    
vehicles = [
    Car("Ford", "Focus", 1998),
    Bike("yamaha","RX",1999)
]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} model {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle , Bike):
        print(f"Inspecting {vehicle.brand} model {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is a valid vehicle")

