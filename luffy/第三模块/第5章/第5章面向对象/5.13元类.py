# 一 知识储备
# exec：三个参数
#
# 参数一：字符串形式的命令
#
# 参数二：全局作用域（字典形式），如果不指定，默认为globals()
#
# 参数三：局部作用域（字典形式），如果不指定，默认为locals()

# g = {
#     'x':1,
#     'y':2
# }
# l = {}
#
# exec("""
# global x,z
# x = 100
# z = 200
#
# m = 300
# """,g,l)
#
# print(g)
# print(l)

# ---------------------类的创建-------------------
#----================方式一--------------

# class Chinese():
#     country='China'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def talk(self):
#         print('%s is talking' %self.name)

#---------------------方式二：就是手动模拟class创建类的过程）：将创建类的步骤拆分开，手动去创建--------------------
#类名
class_name='Chinese'
#类的父类
class_bases=(object,)
#类体
class_body="""
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age
def talk(self):
    print('%s is talking' %self.name)
"""
class_dic={}
exec(class_body,globals(),class_dic)

print(class_dic)
Foo=type(class_name,class_bases,class_dic) #实例化type得到对象Foo，即我们用class定义的类Foo
print(Foo)
print(type(Foo))
print(isinstance(Foo,type))