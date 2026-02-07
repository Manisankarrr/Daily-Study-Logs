class Grandparent:
    def method_grandparent(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def method_parent(self):
        print("Method from Parent")

class Child(Parent):
    def method_child(self):
        print("Method from Child")