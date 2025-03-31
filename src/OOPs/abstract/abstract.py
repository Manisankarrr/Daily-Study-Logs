#Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                They can contain abstract methods, which are declared but have no implementation.
#                Abstract classes benefits:
#                1. Prevents instantiation of the class itself
#                2. Requires children to use inherited abstract methods
#                3. Provides a common interface for all subclasses



from abc import ABC, abstractmethod

# Abstract class for all vehicles
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("Starting engine...")

    @abstractmethod
    def stop_engine(self):
        print("Stopping engine...")

# vehicle = Vehicle()  # This will raise an error because Vehicle is abstract and cannot be instantiated
# TypeError: Can't instantiate abstract class Vehicle with abstract methods start_engine, stop_engine

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

car = Car()

car.start_engine()
car.stop_engine()

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")
    def stop_engine(self):
        print("Bike engine stopped.")

bike = Bike()

bike.start_engine()
bike.stop_engine()


