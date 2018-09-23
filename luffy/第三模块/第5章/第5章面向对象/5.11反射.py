# ----1---- isinstance(obj,cls)检查是否obj是否是类 cls 的对象
# class Foo(object):
#     pass
# obj = Foo()
# print(isinstance(obj,Foo))

# ----2--- issubclass(sub, super)检查sub类是否是 super 类的派生类
# class Foo(object):
#     pass
# class Bar(Foo):
#     pass
# print(issubclass(Bar,Foo))

# ---3----  hasattr(object,name)  判断object中有没有一个name字符串对应的方法或属性
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' % self.name)
#
# obj = People('alex', 18)
# print(obj.name)  # print(obj.__dict__['name'])
# print(obj.age)   # print(obj.age)
# # print(obj.__dict__)
#
# print(obj.talk)  # 绑定到对象 <bound method People.talk of <__main__.People object at 0x024339B0>>
#
#
# # hasattr(object,name)
# # 判断object中有没有一个name字符串对应的方法或属性
# print(hasattr(obj, 'name'))  # obj.name  # obj.__dict__['name']
# print(hasattr(obj, 'talk'))     # obj.talk  # obj.__dict__['name']
#
# # print(obj.__dict__)
# # print(People.__dict__)

#---- 4---- .getattr(obj, 'name')：取出object中name字符串对应的方法或属性(该方法必须存在)
#
#
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' % self.name)
#
# obj = People('alex', 18)
#
# # print(obj.__dict__)
# # print(People.__dict__)
# print(getattr(obj, 'name'))
# print(getattr(obj, 'talk')) ## talk函数的内存地址

#-- 5--- setattr(object ,name,value)
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f"{self.name} is talking")
# obj = People('alex',18)
# print(setattr(obj,'sex','male'))
# print(obj.__dict__)

# ---6-- delattr()
# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print(f"{self.name} is talking")
# obj = People('alex',18)
# print(delattr(obj,'age'))
# print(obj.__dict__)

# class Foo(object):
#
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# print (getattr(Foo, 'staticField'))
# print (getattr(Foo, 'func'))
# print (getattr(Foo, 'bar'))

# 反射当前模块 成员
# import sys
#
#
# def s1():
#     print('s1')
#
#
# def s2():
#     print ('s2')
#
#
# this_module = sys.modules[__name__]
#
# print(hasattr(this_module, 's1'))
# print(getattr(this_module, 's2'))

# 反射的应用
# 好处一：实现可插拔机制
#
# 有俩程序员，一个lili，一个是egon，lili在写程序的时候需要用到egon所写的类，但是egon去跟女朋友度蜜月去了，还没有完成他写的类，lili想到了反射，使用了反射机制lili可以继续完成自己的代码，等egon度蜜月回来后再继续完成类的定义并且去实现lili想要的功能。
#
# 总之反射的好处就是，可以事先定义好接口，接口只有在被完成后才会真正执行，这实现了即插即用，这其实是一种‘后期绑定’，什么意思？即你可以事先把主要的逻辑写好（只定义接口），然后后期再去实现接口的功能
#
# egon还没有实现全部功能

# class FtpClient:
#     'ftp客户端,但是还么有实现具体的功能'
#     def __init__(self,addr):
#         print('正在连接服务器[%s]' %addr)
#         self.addr=addr
#不影响lili的代码编写

##from module import FtpClient
# f1=FtpClient('192.168.1.1')
# if hasattr(f1,'get'):
#     func_get=getattr(f1,'get')
#     func_get()
# else:
#     print('---->不存在此方法')
#     print('处理其他的逻辑')
#好处二：动态导入模块（基于反射当前模块成员）

class Service:
    def run(self):
        while True:
            to_input = input('>>:').strip()
            cmds = to_input.split()
            if hasattr(self,cmds[0]):
                func = getattr(self,cmds[0])
                func(cmds)
    def get(self,cmds):
        print('get-----------',cmds)
    def put(self,cmds):
        print('put----------',cmds)
obj = Service()
obj.run()