
class Animal:
    def __init__(self, name,):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

d1 = Dog("Buddy")
c1 = Cat("Whiskers")

d1.eat()
d1.sleep()