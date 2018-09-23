

# class MysqlHandler:
#     def __init__(self,host,port,db,charset='utf-8'):
#         self.host =host
#         self.port = port
#         self.db = db
#         self.charset = charset
#         self.conn = connect(self.host,self.port,self.db,self.charset)
#     def exc1(self,sql):
#         self.conn.execute(sql)
#         return XXX
#     def exc2(self,sql):
#         self.conn.call_proc(sql)
#         return XXX
# obj = MysqlHandler('127.0.0.0',3306,'db1')
# obj.exc1('select * from tb1')
# obj.exc2('存储过程的名字')

# 封装的知识
# class People(object):
#     __name = "luffy"
#     age = 18
#
# p1 = People()
# print(p1._People__name, p1.age)

# class People(object):
#
#    def __init__(self):
#        print("__init__")
#
#    def __new__(cls, *args, **kwargs):
#        print("__new__")
#        return object.__new__(cls, *args, **kwargs)
#
# People()

#--------------11、题绑定方法与非绑定方法------------------------
# class Foo:
#     def __init__(self,name):
#         self.name =name
#
#     def walk(self):
#         print('123')
#     @classmethod # 绑定方法  只给类调用
#     def tell(cls):
#         print(cls)
#     @staticmethod  #非绑定方法
#     def fun(x,y):
#         print(x+y)
# f = Foo('egon')
#
# f.walk()
# Foo.walk(Foo)
#
# Foo.tell() # 类的绑定方法
# f.tell()
#
# Foo.fun(1,2) # 非绑定方法
# f.fun(2,3)

#-------------------------------
# class A(object):
#
#    def foo(self, x):
#        print("executing foo(%s, %s)" % (self,x))
#
#    @classmethod
#    def class_foo(cls, x):
#        print("executing class_foo(%s, %s)" % (cls,x))
#
#    @staticmethod
#    def static_foo(x):
#        print("executing static_foo(%s)" % (x))
#
# a = A()
# print('------------')
# a.foo(2)
# A.foo(A,2)
# print('------------')
# A.class_foo(2)
# print('------------')
# a.static_foo(2)
# A.static_foo(2)

#-------------------------12请执行以下代码，解释错误原因，并修正错误。---------------------
# class Dog(object):
#
#    def __init__(self,name):
#        self.name = name
#
#    @property
#    def eat(self):
#        print(" %s is eating" %self.name)
#
# d = Dog("ChenRonghua")
# d.eat()


#-------------------------13、下面这段代码的输出结果将是什么？请解释-----------------------------
# class Parent(object):
#    x = 1
#
# class Child1(Parent):
#    pass
#
# class Child2(Parent):
#    pass
#
# print(Parent.x, Child1.x, Child2.x)
# # 1，1，1 从内存地址的角度来讲
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# # 1，2，1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
# # 3，2，3
#---------------14 多重继承的执行顺序，请解答以下输出结果是什么？并解释。 -------------------------------
class A(object):
   def __init__(self):
       print('A')
       super(A, self).__init__()

class B(object):
   def __init__(self):
       print('B')
       super(B, self).__init__()

class C(A):
   def __init__(self):
       print('C')
       super(C, self).__init__()

class D(A):
   def __init__(self):
       print('D')
       super(D, self).__init__()

class E(B, C):
   def __init__(self):
       print('E')
       super(E, self).__init__()

class F(C, B, D):
   def __init__(self):
       print('F')
       super(F, self).__init__()

class G(D, B):
   def __init__(self):
       print('G')
       super(G, self).__init__()

if __name__ == '__main__':
   g = G()
   print(g.__class__.mro())
   print('----------')
   f = F()
   print(f.__class__.mro())



