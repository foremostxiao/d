# ------继承的方法--------------
#
# class B:
#     def __init__(self):
#         pass
#     def __handle(self):
#         print('调用B的handle')
#
# class A(B):
#     def __init__(self):
#         pass
#     def handle(self):
#         print('调用A的handle')
# a = A()
# a._B__handle()

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name,self.age)
#
#
# if __name__ == '__main__':
#     #在构造对象的时候会自动调用初始化构造函数
#     student = Student("Alex",100)
#     # 输出对象：
#     print(student)
#     print(student.__dict__)


class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__tell()

    def __tell(self):
        print("%s---%s" % (self.name, self.age))

class Student(People):
    def __tell(self):
        print("呵呵!")

if __name__ == '__main__':
    student = Student("alex",20)

