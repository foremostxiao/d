# 单继承和多继承，，__bases__ 查看所继承的父类，输出用元组表示
# class ParentClass1:
#     pass
# class ParentClass2:
#     pass
# class SubClass1(ParentClass1):#单继承，基类是ParentClass1，派生类是SubClass1
#     pass
# class SubClass2(ParentClass1,ParentClass2):#python 支持多继承，用逗号分隔开多个继承类
#     pass
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

# 继承与重用性
# 开发A类 ，再开发B类，B类大部分内容与A类相同
# class Hero:
#     def __init__(self,nickname,aggressivity,life_value):
#         self.nickname = nickname
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#     def move_forward(self):
#         print(f"move_forward{self.nickname}")
#     def move_backward(self):
#         print(f"move_backward{self.nickname}")
#     def move_left(self):
#         print(f"move_left{self.nickname}")
#     def move_right(self):
#         print(f"move_right{self.nickname}")
#     def ack(self,enemy):
#         enemy.life_value -= self.aggressivity
# class Garen(Hero):
#     pass
# class Riven(Hero):
#     pass
# hero = Garen('dema',30,200)
# hero2 = Riven('HAHA',50,150)
# print(hero2.life_value)
# hero.ack(hero2)
# print(hero2.life_value)

# 再看属性查找
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# b=Bar()
# b.f2()

# 多继承属性的查找，经典类（深度优先），新式类（广度优先）
# class A(object):
#     def test(self):
#         print('from A')
# class B(A):
#     # def test(self):
#     #     print('from B')
#     pass
# class C(A):
#     # def test(self):
#     #     print('from C')
#     pass
# class D(B):
#     # def test(self):
#     #     print('from D')
#     pass
# class E(C):
#     # def test(self):
#     #     print('from E')
#     pass
# class F(D,E):
#     # def test(self):
#     #     print('from F')
#     pass
#
# f1 = F()
# f1.test()
# print(F.__mro__)

# -------在子类中调用父类的方法----------------
# class Vehicle:  # 定义交通工具类
#     Country = 'China'
#
#     def __init__(self, name, speed, upload, power):
#         self.name = name
#         self.speed = speed
#         self.upload = upload
#         self.power = power
#
#     def run(self):
#         print('开动啦...')
#
#
# class Subway(Vehicle):  # 地铁
#     def __init__(self, name, speed, upload, power, line):
#         Vehicle.__init__(self, name, speed, upload, power)
#         self.line = line
#
#     def run(self):
#         print('地铁%s号线欢迎您' % self.line)
#         Vehicle.run(self)
# line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
# line13.run()

#方式二：super()

# class Vehicle: #定义交通工具类
#      Country='China'
#      def __init__(self,name,speed,load,power):
#          self.name=name
#          self.speed=speed
#          self.load=load
#          self.power=power
#      def run(self):
#          print('开动啦...')
# class Subway(Vehicle): #地铁
#     def __init__(self,name,speed,load,power,line):
#         #super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
#         super().__init__(name,speed,load,power)
#         self.line=line
#     def run(self):
#         print('地铁%s号线欢迎您' %self.line)
#         #super(Subway,self).run()
#         super().run()
# class Mobike(Vehicle):#摩拜单车
#     pass
# line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
# print(line13.name)
# line13.run()



# class A:
#     def test(self):
#         # super().test()
#         print('123')
#     pass
# class B:
#     def test(self):
#         print('456')
#     pass
# class C:
#     pass
# class D(B,C):
#     pass
#
# c = D()
# c.test()
# print(D.__mro__)

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
   print(g.__class__)
   print()
   f = F()