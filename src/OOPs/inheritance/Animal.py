class Animal:

    def __init__(self, name, is_extinct=False):
        self.name = name
        self.is_extinct = is_extinct

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Mammoth(Animal):
    def speak(self):
        print(f"{self.name} says Roar!")

class Walrus(Animal):
    def speak(self):    
        print(f"{self.name} says Ar-ar-ar!")

dog = Dog("Tommmy",False)

mammoth = Mammoth("Nick",True)

walrus = Walrus("Willy",True)

print(f"{mammoth.is_extinct}")

print(f"{dog.name} is a dog.")

print(f"{mammoth.name} is a mammoth. {mammoth.name} is {'extinct' if mammoth.is_extinct else 'is not extinct'}.")


print(f"{walrus.name} is a walrus. {walrus.name} is {'extinct' if walrus.is_extinct else 'is not extinct'}.")

dog.speak()