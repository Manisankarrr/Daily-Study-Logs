#class variables = Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class Student:
    # class variable
    school = "ABC School"  # shared among all instances
    roll_number = 0 # number of students
    
    def __init__(self, name, age):
        self.name = name # instance variable
        self.age = age
        Student.roll_number += 1

    def introduce(self):
        print(f"Hello, my name is {self.name} and My roll number is {Student.roll_number}.")



student1 = Student("John", 20)
student2 = Student("Jane", 22)
student3 = Student("Doe", 21)
student4 = Student("Smith", 23)
student5 = Student("Alice", 24)

print(student1.name)
print(student1.age)
print(student1.school)  # Accessing class variable through instance
print(f"{student1.name} is a student of {Student.school}.")
print(f"Total number of students: {Student.roll_number:.2f}")

student1.introduce()