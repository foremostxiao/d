# 多态：同一个事物的多种形态
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass
class People(Animal):
    def talk(self):
        print('say people')
class Dog(Animal):
    def talk(self):
        print('say dog')
class Pig(Animal):
    def talk(self):
        print('say Pig')
people = People()
dog = Dog()
pig = Pig()

people.talk()
dog.talk()
pig.talk()

# 多态性，指的是可以不考虑对象的类型的情况下而直接使用对象
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass
class People(Animal):
    def talk(self):
        print('say people')
class Dog(Animal):
    def talk(self):
        print('say dog')
class Pig(Animal):
    def talk(self):
        print('say Pig')
people = People()
dog = Dog()
pig = Pig()

# people.talk()
# dog.talk()
# pig.talk()
def func(Animal):
    Animal.talk()
func(people)
func(dog)
func(pig)

# 鸭子类型
# 有read 和 write
class File:
    def read(self):
        pass
    def write(self):
        pass
class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')
class Text:
    def read(self):
        print('text read')

    def write(self):
        print('text write')
disk = Disk()
text = Text()
disk.read()
disk.write()
text.read()
text.write()