class Animal:# Animal <- prey,predator <- rabbit,hawk,fish || C(B) <- B(A) <- A
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass    

class Fish(Prey, Predator):#multiple
    pass

rabbit = Rabbit("rabbit")
hawk = Hawk("hawk")
fish = Fish("fish")

rabbit.flee()
#tried exception handling
try:
    hawk.flee()
except Exception:
    print("Hawk wont flee!")

hawk.hunt()# from predator class
fish.flee()# from prey class

rabbit.eat()#from animal class
