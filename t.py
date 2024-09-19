class student:
    total_student=0
    def __init__(self,name,age,grade):
        self.user_name=name
        self.life=age
        self.score=grade
        student.total_student+=1
    def display_info(self):
        return f"{self.user_name} of {self.life} year got {self.score} grade"
    @classmethod
    def get_total_students(cls):
        return cls.total_student
    @staticmethod
    def is_adult(life):
        if life>=18:
            return "you are adult"
        else:
            return "you are not adult"
    @property
    def grade_info(self):
        return f"student got {self.score}"

    # Creating instances of the student class
student1 = student("John", 20, "A")
student2 = student("Alice", 17, "B")

# Displaying student information
print(student1.display_info())  # Output: Name: John, Age: 20, Grade: A
print(student2.display_info()) # Output: Name: Alice, Age: 17, Grade: B

# Accessing the class variable through the class method
print(student.get_total_students())  # Output: 2

# Checking if the student is an adult using the static method
print(student.is_adult(student1.life))  # Output: True
print(student.is_adult(student2.life))  # Output: False

# Accessing the property
print(student1.grade_info)  # Output: student is in grade A
print(student2.grade_info)