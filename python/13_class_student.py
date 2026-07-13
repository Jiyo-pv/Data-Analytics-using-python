# Q13 Class Student with display - @JIYO P V 2026-07-13
class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Course:", self.course)


s = Student("Anu", 101, "Python")
s.display()
