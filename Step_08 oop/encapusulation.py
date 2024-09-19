#meaning of encapsulation is just like a capsule
class school:
    def __init__(self,teacher,student):
        self.__teacher=teacher #when you put two underscore on attribute you are making it private 
#it can only access by geter method this is known as encapsulation
        self.student=student
    def get_teacher(self):#this is getter method if we want to get a refine output
        return f"{self.__teacher} is respected for {self.student}"
my_school=school("bashir","ali")
#print(my_school.__teacher) it will give err
print(my_school.get_teacher())