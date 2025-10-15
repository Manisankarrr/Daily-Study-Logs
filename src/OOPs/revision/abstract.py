from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")

# Example usage
my_car = Car()
my_car.start_engine()
b1 = Bike()
b1.start_engine()