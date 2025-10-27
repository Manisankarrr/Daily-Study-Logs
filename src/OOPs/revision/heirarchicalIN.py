class Parent:
    def common_method(self):
        print("Common method from Parent")

class Child1(Parent):
    def specific_method1(self):
        print("Specific method from Child1")

class Child2(Parent):
    def specific_method2(self):
        print("Specific method from Child2")