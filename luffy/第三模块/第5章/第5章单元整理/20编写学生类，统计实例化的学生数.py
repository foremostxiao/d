class Student:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.count += 1
stu = Student('aa',18)
stu2 = Student('bb',20)
print(Student.count)

