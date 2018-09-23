# 1 属性的查找
#  类的数据属性是所有对象共享的
# class OldboyStudent:
#     school='oldboy'
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
# s1=OldboyStudent()
# s2=OldboyStudent()
# s3=OldboyStudent()
# print(id(OldboyStudent.school))
# print(id(s1.school))
# print(id(s2.school))
# print(id(s3.school))

# 类的函数数据是绑定给对象用的，称为绑定到对象的方法
#
# class OldboyStudent:
#     school='oldboy'
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
# s1=OldboyStudent()
# s2=OldboyStudent()
# s3=OldboyStudent()
# print(OldboyStudent.learn,type(OldboyStudent.learn))
# print(s1.learn)
# print(s2.learn)
# print(s3.learn)

# 2 绑定方法
# class OldboyStudent:
#     school='oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def learn(self):
#         print('%s is learning' %self.name) #新增self.name
#
#     def eat(self):
#         print('%s is eating' %self.name)
#
#     def sleep(self):
#         print('%s is sleeping' %self.name)
#
#
# s1=OldboyStudent('李坦克','男',18)
# s2=OldboyStudent('王大炮','女',38)
# s3=OldboyStudent('牛榴弹','男',78)
# #类中定义的函数（没有被任何装饰器装饰的）是类的函数属性，类可以使用，但必须遵循函数的参数规则，有几个参数需要传几个参数
# OldboyStudent.learn(s1)
# OldboyStudent.learn(s2)
# OldboyStudent.learn(s3)
#
# s1.learn() #等同于OldboyStudent.learn(s1)
# s2.learn() #等同于OldboyStudent.learn(s2)
# s3.learn() #等同于OldboyStudent.learn(s3)

#--------------------------------------------- 练习题---------------------------------------------------------------------------
# 练习1：编写一个学生类，产生一堆学生对象， (5分钟)
#
# 要求：
#
# 有一个计数器（属性），统计总共实例了多少个对象
# class Students:
#     school = 'wuhan_university'
#     count = 0
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.count += 1
#         Students.count += 1
#
#     def learn(self):
#         print(f"{self.name},lean too much")
#     def playgame(self):
#         print(f"{self.name},playgame too much")
#     def sleep(self):
#         print(f"{self.name},sleep too much")
#
# s1 = Students('xiao','man',18)
# s2 = Students('lele','man',20)
# s3 = Students('dawang','man',23)
# print(Students.count)#所有对象的
# print(s1.count)#算单个对象的

#练习2：模仿王者荣耀定义两个英雄类， (10分钟)

# 要求：
#
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
class hero():
    role = '战士'
    def __init__(self,name,atk,blood):
        self.name = name
        self.atk = atk
        self.blood = blood
    def attack(self,enemy):
        enemy.blood = enemy.blood - self.atk
        print(f"英雄{enemy.name}剩余血值{enemy.blood}--被英雄{self.name}攻击一次")
        if enemy.blood < 0:
            print(f"英雄{enemy.name}已阵亡")
        else:
            pass
class hero2():
    role2 = '法师'
    def __init__(self,name,atk,blood):
        self.name = name
        self.atk = atk
        self.blood = blood
    def attack(self, enemy):
        enemy.blood = enemy.blood - self.atk
        print(f"英雄{enemy.name}剩余血值{enemy.blood}--被英雄{self.name}攻击一次")
        if enemy.blood < 0:
            print(f"英雄{enemy.name}已阵亡")
        else:
            pass
s1 = hero('德玛西亚',100,1000)
s2 = hero2('瑞文',200,1000)

s1.attack(s2)

s2.attack(s1)

