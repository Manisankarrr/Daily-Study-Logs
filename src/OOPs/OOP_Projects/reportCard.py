'''
1. What is the main object?

A Student (because we need to store student details).

2. What data (attributes) should a student have?

name → Student's name

marks → A list of subject marks

3. What actions (methods) should a student have?

calculate_total() → Adds all subject marks.

calculate_average() → Finds the average mark.

display_report() → Shows the student’s name, total, and average marks.'''


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks # storing it as dictuh

    def total_marks(self):
        return sum(self.marks.values())
    
    def percentage(self):
        total = self.total_marks()
        return (total / len(self.marks))
    
    def grade(self):
        average = self.percentage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    def display_report(self):
        print("\n--- Report Card ---")
        print(f"\nName: {self.name}")
        print(f"\nRoll Number: {self.roll_number}")
        print("\nMarks:")
        for subject, mark in self.marks.items():
            print(f"\n{subject}: {mark}")

        total = self.total_marks()
        percentage = self.percentage()
        grade = self.grade()
        
        print(f"\nTotal Marks: {total}")
        print(f"\nPercentage: {percentage}%")
        print(f"\nGrade: {grade}")

        print("\n--- End of Report Card ---")

def main():
    print("Welcome to Student Report Card System!")

    name = input("Enter student name: ")
    roll_number = input("Enter student roll number: ")
    marks = {}
    subjects = int(input("Enter number of subjects: "))
    for i in range(subjects):
        subject = input(f"Enter subject name: ")
        mark = int(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    student = Student(name, roll_number, marks)
    student.display_report()

if __name__ == "__main__":
    main()

    


    

