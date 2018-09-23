# 抽象类
# class People:
#     def walk(self):
#         print('is walking')
# class Dog:
#     def zou(self):
#         print('is zouing')
# class Pig():
#     def run(self):
#         print('is running')
# people1 = People()
# dog1 = Dog()
# pig1 = Pig()
# people1.walk()
# dog1.zou()
# pig1.run()

# 每个人都有走的功能，但调用方法不一样，
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
       pass
    @abc.abstractmethod
    def eat(self):
        pass

class People(Animal):
    def run(self):
        print('people is walking')
    def eat(self):
        print('people is eating')

class Dog(People):
    def run(self):
        print('dog is walking')
    def eat(self):
        print('dog is eating')
    def zou(self):
        print('haohao ')

class Pig(People):
    def run(self):
        print('pig is walking')
    def eat(self):
        print('pig is eating')

people1 = People()
dog1 = Dog()
pig1 = Pig()
people1.run()
dog1.run()
dog1.zou()
pig1.run()

# 在python中 实现抽象类
#一切皆文件
# import abc #利用abc模块实现抽象类
#
# class All_file(metaclass=abc.ABCMeta):
#     all_type='file'
#     @abc.abstractmethod #定义抽象方法，无需实现功能
#     def read(self):
#         '子类必须定义读功能'
#         pass
#
#     @abc.abstractmethod #定义抽象方法，无需实现功能
#     def write(self):
#         '子类必须定义写功能'
#         pass
#
# # class Txt(All_file):
# #     pass
# #
# # t1=Txt() #报错,子类没有定义抽象方法
#
# class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
#     def read(self):
#         print('文本数据的读取方法')
#
#     def write(self):
#         print('文本数据的读取方法')
#
# class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
#     def read(self):
#         print('硬盘数据的读取方法')
#
#     def write(self):
#         print('硬盘数据的读取方法')
#
# class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
#     def read(self):
#         print('进程数据的读取方法')
#
#     def write(self):
#         print('进程数据的读取方法')
#
# wenbenwenjian=Txt()
#
# yingpanwenjian=Sata()
#
# jinchengwenjian=Process()
#
# #这样大家都是被归一化了,也就是一切皆文件的思想
# wenbenwenjian.read()
# yingpanwenjian.write()
# jinchengwenjian.read()
#
# print(wenbenwenjian.all_type)
# print(yingpanwenjian.all_type)
# print(jinchengwenjian.all_type)

