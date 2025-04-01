
class Shapes:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This shape is {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"Area: {3.14 * self.radius * self.radius}")
        super().describe() # method overriding returns parent's description

class Square(Shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Area: {self.width * self.width}")
        super().describe() # method overriding returns parent's description

class Rectangle(Shapes):
    def __init__(self,color,is_filled,width,length):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length

    def describe(self):
        print(f"Area: {self.width * self.length}")
        super().describe() # method overriding returns parent's description

circle = Circle("red", True, 5)

square = Square("blue", False, 10)

rectangle = Rectangle("green", True, 8, 12)

print(f"Circle color: {circle.color}")
print(f"radius: {circle.radius}")

print(f"Square color: {square.color}")
print(f"width: {square.width}")


print(f"Rectangle color: {rectangle.color}")
print(f"width: {rectangle.width}")
print(f"length: {rectangle.length}")

circle.describe()
square.describe()
rectangle.describe()# method overriding returns child
