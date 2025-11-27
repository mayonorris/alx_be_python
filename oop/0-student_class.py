class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_student_info(self):
        print(f"The student {self.name} is {self.age} years old.")
# create an instance and call the method
s = Student("Mayo", 25)
s.display_student_info()
