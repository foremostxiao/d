# -------------------在继承中父类如果不想让子类覆盖自己的方法，可以将方法定义为私有
# class A:
#     def __fa(self):
#         print('from A')
#     def test(self):
#         self.__fa()
# class B(A):
#     def __fa(self):
#         print('from B')
# b = B()
# b.test() # from A


# -----------------------------------封装数据
# class Teacher:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print('姓名:%s,年龄:%s' %(self.__name,self.__age))
#     def set_info(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是整型')
#         self.__name=name
#         self.__age=age
#
# t=Teacher('alex',18)
# t.tell_info()
#
# t.set_info('lele',19)
# t.tell_info()

#-------------------------------- 封装方法
# class ATM:
#     def __card(self):
#         print('插卡')
#     def __auth(self):
#         print('用户认证')
#     def __input(self):
#         print('输入取款金额')
#     def __print_bill(self):
#         print('打印账单')
#     def __take_money(self):
#         print('取款')
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print_bill()
#         self.__take_money()
# a = ATM()
# a.withdraw()


#--------------------------封装的可扩展性
# class Room:
#     def __init__(self,name,owner,height,weight,length):
#         self.name = name
#         self.owner = owner
#         self.__weight = weight #宽
#         self.__lenght = length #长
#         self.__height = height #高
#     def tell_area(self):
#         return self.__weight*self.__lenght
# r = Room('卫生间','alex',10,10,5)
# print(r.tell_area())



# -------------------------特性（property）
# class People:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#     @property # 装饰器
#     def bim(self):
#         return self.weight/(self.height**2)
# p1 = People('ehon',60,1.70)
# print(p1.bim)

#------正常的情况---------------
# class People:
#     def __init__(self,name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
# p = People('lele')
# print(p.get_name())  # p.get_name() 调用方法
# #-----------加@property-------------
class People:
    def __init__(self,name):
        self.__name = name
    @property
    def get_name(self):
        return self.__name
p = People('lele')
print(p.get_name)  #p.get_name 调用方法

class Foo:
    def __init__(self,val):
        self.__NAME=val #将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)

    @name.setter
    def name(self,value):
        if not isinstance(value,str):  #在设定值之前进行类型检查
            raise TypeError('%s must be str' %value)
        self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')

f=Foo('alex')
print(f.name)
f.name='xoa' #抛出异常'TypeError: 10 must be str'
#del f.name #抛出异常'TypeError: Can not delete'

