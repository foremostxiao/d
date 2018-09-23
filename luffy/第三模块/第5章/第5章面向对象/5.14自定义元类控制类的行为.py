
#Chinese = Mymeta(class_name,class_bases,class_dic)

#步骤一：如果说People=type(类名,类的父类们,类的名称空间)，那么我们定义元类如下，来控制类的创建


#我们把 Person 类变成一个可调用对象：

# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def __call__(self, friend):
#         print('My name is %s...' % self.name)
#         print('My friend is %s...' % friend)
# p = Person('Bob','male')
# p('Tim')

# def fib(max):
#     n, a, b = 0, 0, 1
#     while True:
#         if n < max:
#             print(b)
#             a ,b = b,a+b
#         else:
#             break
#         n = n + 1
# fib(4)
# #--------------
# print('-----------------------')
# def fib(max):
#     n,a,b = 0,0,1
#
#     while n < max:
#         print(b)
#         #yield  b
#         a,b = b,a+b
#         n += 1
#     return 'done'
# fib(10)

# class People(object,metaclass=type):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __call__(self, *args, **kwargs):
#         print(self,args,kwargs)
# obj=People('egon',18)
# obj(1,2,3,a=1,b=2,c=3)


#-------------------#步骤三：自定义元类，控制类的调用（即实例化）的过程------------------------------------------------
# class Mymeta(type): #继承默认元类的一堆属性
#     def __init__(self,class_name,class_bases,class_dic):
#         if not class_name.istitle():
#             raise TypeError('类名首字母必须大写')
#
#         super(Mymeta,self).__init__(class_name,class_bases,class_dic)
#
#     def __call__(self, *args, **kwargs):
#         #self=People
#         print(self,args,kwargs) #<class '__main__.People'> ('egon', 18) {}
#
#         #1、实例化People，产生空对象obj
#         obj=object.__new__(self)
#
#         #2、调用People下的函数__init__，初始化obj
#         self.__init__(obj,*args,**kwargs)
#
#         #3、返回初始化好了的obj
#         return obj
#
# class People(object,metaclass=Mymeta):
#     country='China'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk(self):
#         print('%s is talking' %self.name)
#
# obj=People('egon',18)
# print(obj.__dict__) #{'name': 'egon', 'age': 18}

#------------------------基于元类实现单例模式,比如数据库对象,实例化时参数都一样,就没必要重复产生对象,浪费内存-------------------------------------------------------
# class MySQL:
#     __instance = None   # 第一次实例化后  __instance = obj
#     def __init__(self):
#         self.host = '127.0.0.1'
#         self.port = 3306
#     @classmethod
#     def singlethon(cls):
#         if not cls.__instance:
#             obj = cls() # obj = MySQL() 实例化
#             print(obj)
#             cls.__instance = obj
#         return cls.__instance
#     def conn(self):
#         pass
#     def execute(self):
#         pass
# obj1 = MySQL.singlethon()
# obj2 = MySQL.singlethon()
# print(obj1 is obj2)

#---------------------------------元类方式实现单例模式---------------------
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            obj = object.__new__(self)
            self.__init__(obj) #初始化
            self.__instance = obj
        return self.__instance

class Mysql(object,metaclass=Mymeta):
    '''
    注释
    '''
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
    def conn(self):
        pass
    def execute(self):
        pass

obj1 = Mysql()
obj2 = Mysql()
print(obj1 is obj2)
