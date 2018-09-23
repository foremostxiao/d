# 绑定给类的方法（classmethod）
# classmethod是给类用的，即绑定到类，类在使用时会将类本身当作参数传给类方法的第一个参数
# import os,sys
# HOST = '127.0.0.1'
# PORT = 3306
# DB_PATH = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(DB_PATH)
# import db.json


# ------绑定给对象
# class Foo:
#     def __init__(self,name):
#         self.name = name
#     def tell(self):
#         print(f"名字{self.name}")
# f = Foo('LELE')
# print(f.tell())
# print(f.tell)



#--------绑定给类
# class Foo:
#     def __init__(self,name):
#         self.name = name
#     def tell(self):
#         print(f"名字{self.name}")
#     @classmethod # 把类本身当作第一个参数
#     def func(cls):  # cls = Foo
#         print(cls)
# f = Foo('LELE')
# Foo.func()

#=====非绑定方法----对象和类都可以用
# class Foo:
#     def __init__(self,name):
#         self.name = name
#     def tell(self):# 绑定方法，绑定给对象
#         print(f"名字{self.name}")
#     @classmethod # 绑定方法：绑定给类 把类本身当作第一个参数
#     def func(cls):  # cls = Foo
#         print(cls)
#
#     @staticmethod  # 非绑定方法
#     def func2(x,y):
#         print(x+y)
#
# # -----非绑定方法--------
# f = Foo('LELE')
# Foo.func2(1,2) # 类
# f.func2(1,4)  # 对象

# 类内部定义的函数：
# 绑定方法：绑定给对象 ，在内部创建的函数没有装饰器；绑定给类，有装饰器@classmethod把类本身当作第一个参数
# 非绑定方法：@staticmethod普通函数,谁都可调用

#---------------------------练习-------------------------
# 练习 1 定义MySQL类
# 要求：
#
# 1.对象有id、host、port三个属性
#
# 2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
#
# 3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
#
# 4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，
# 保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象

import conf
import hashlib,time,os,sys,pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

class MySQL:
    def __init__(self,host,port):#对象的初始化操作是自动完成的
        self.host = host
        self.port = port
        self.id = MySQL.create_id()

    @staticmethod # 非绑定方法
    def create_id():
        #m = hashlib.md5()
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        #m.update(bytes(str(m),encoding='utf-8'))
        return m.hexdigest()

    def tell(self):
        print(f"{self.id},{self.host},{self.port}")

    def save(self):
        id_filename = os.path.join(conf.DB_PATH,self.id+'.txt') #结合目录名和文件名
        print(id_filename)
        with open(id_filename,'wb') as f:
            print(self.__dict__) #{'host': '127.0.0.1', 'port': 80, 'id': '79b3fd8d38ce989a29f30bcf5b5801b3'}
            return pickle.dump(self,f) #保存的是对象

    @classmethod # 绑定方法 MySQL(db.host,db.port)
    def get_obj_by_id(cls,filename):
        id_filename = os.path.join(conf.DB_PATH,filename+'.txt')
        with open(id_filename,'rb') as f:
            return pickle.load(f)

    @classmethod # 绑定方法
    def id_from_conf(cls):  #本题为类绑定 MySQL(db.host,db.port)
        return cls(conf.host,conf.port)
# # 用户传入host和port
user1 = MySQL('127.0.0.1',80)
# #user1.tell()
# # #
# # # # save能自动将对象序列化到文件中
user1.save()


# 从配置文件中读取host和port进行实例化
# user2 = MySQL.id_from_conf()
# user2.tell()

#get_obj_by_id方法用来从文件中反序列化出对象
# user3 = MySQL.get_obj_by_id('5c6bbc3f3f8aca6baf61a403a1993ebc')
# user3.tell()




# s = 'xiao'
# s2 = 'xiao'
# print(id(s))
# print(id(s2))
# print()
# if s == s2:
#     print('11')
# else:
#     print('456')