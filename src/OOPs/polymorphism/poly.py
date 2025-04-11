#Polymorpism = Greek word that means to "have many forms or faces"
#              Poly = Many
#              Morphe = Form
#              TWO WAYS TO ACHIEVE POLYMORPHISM
#              1. Inheritance An object could be treated of the same type as a parent class
#              2. "Duck typing" = Object must have necessary attributes/methods

# Example of Inheritance -
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape): 
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    
class pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)  # call parent class constructor
        self.toppings = toppings
        self.radius = radius

shape = [Circle(4), Square(5), Rectangle(6,7),pizza("pepperoni",15)]

for s in shape:
    print(f"Area of {type(s).__name__}: {s.area()}")