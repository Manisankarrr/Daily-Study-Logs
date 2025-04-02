## object = A "bundle" of related attributes (variables) and methods (functions)
#Ex. phone,cup, book
#You need a "class" to create many objects

##class = (blueprint) used to design the structure and layout of an object


class Car:
    # we need constructor to create objects
    def __init__(self, model, year, color, for_sale, is_electric): #methods are functions that belong to an object
        self.model = model# attributes are variables that an object has
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.is_electric = is_electric
    

    def start(self): # method to start the car
        print(f"{self.color} color {self.model} started")

    def stop(self): # method to stop the car
        print(f"{self.color} color {self.model} stopped")

    def describe(self): # method to describe
        print(f"{self.color} color {self.model} of year {self.year} is {'for sale' if self.for_sale else 'not for sale'}")

    def electric(self): # method to check if the car is electric
        print(f"{self.color} color {self.model} is {'electric car' if self.is_electric else 'not an electric car' }")
