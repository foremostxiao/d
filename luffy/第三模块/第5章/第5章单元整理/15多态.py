# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print(f"{self} is talking")
#     pass
# class Dog(Animal):
#     def talk(self):
#         print(f"{self} is talking")
#     pass
# peo = People()
# dog = Dog()
# # peo.tal()
# # dog.talk()
# def func(obj):
#     obj.talk()
# func(peo)
# func(dog)

import abc
class Animal(metaclass=abc.ABCMeta):   # metaclass元类
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod    # 定义抽象方法，无需实现功能
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print('people %s is talking loudly' % self.name)

class Pig(Animal):
    def talk(self):
        print('pig %s is talking' % self.name)

class Dog(Animal):
    def talk(self):
        print('Dog %s is talking' % self.name)

def func(animal):
    animal.talk()

s = Dog('was')
func(s)