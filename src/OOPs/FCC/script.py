class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        return f"{self.name} says Woof!"

class Owner:
    def __init__(self, name, address):
        self.name = name
        self.address = address
class Cat:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def meow(self):
        return f"{self.name} says Meow!"
    
cat1 = Cat("Whiskers", "Siamese", Owner("Bob", "456 Cat Ave"))
print(cat1.owner.name)



owner1 = Owner("Alice", "123 Dog St")
dog = Dog("Buddy", "Golden Retriever",owner1)
print(dog.bark())
print(dog.name)
print(dog.breed)
print(dog.owner.name)
print(dog.owner.address)
print(owner1.name)