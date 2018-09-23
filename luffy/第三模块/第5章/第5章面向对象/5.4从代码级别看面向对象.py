# 1 在没有学习类这个概念时，数据与功能是分离的
# def exc1(host,port,db,charset):
#     conn = connect(host,port,db,charset)
#     conn.execute(sql)
#     return xx
# def exc2(host,port,db,charset,proc_name):
#     conn = connect(host,port,db,charset)
#     conn.call_proc(sql)
#     return xxx
#每次调用都需要重复传入一堆参数
# exc1('127.0.0.1',3306,'db1','utf-8','select * from tb1;')
# exc2('127.0.0.1',3306,'db1','utf-8','储存过程的名字')



# class MySQLHandler:
#     def __init__(self,host,port,db,charset='utf-8'):
#         self.host = host
#         self.port = port
#         self.db = db
#         self.charset = charset
#         self.conn = connect(self.host,self.port,self.db,self.charset)
#     def exc1(self,sql):
#         return self.conn.execute(sql)
#     def exc2(self,sql):
#         return self.conn.call_proc(sql)
# obj = MySQLHandler('127.0.0.1',3306,'db1')
# obj.exc1('select * from tb1;')
# obj.exc2('储存过程的名字')

# 2 可扩展性高
# 定义类并产生三个对象
# class Chinese:
#     name = 'china'
#     country = 'china2'
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# s1 = Chinese('alex','man','22')
# s2 = Chinese('alex2','woman','23')
# s3 = Chinese('alex3','man','21')
# print(s1,type(s1),s1.__dict__)
# print(Chinese.__dict__)
# print(s1.name)
# print(s1.country)



# # 如果我们新增一个类属性，将会立刻反映给所以对象，而对象却无需修改
# print('----------------------------------------------')
# class Chinese:
#     country = 'china'
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def tell_info(self):
#         info = f"""
#         国籍：{self.country}
#         姓名：{self.name}
#         性别：{self.sex}
#         年龄:{self.age}
#         """
#         print(info)
# s1 = Chinese('alex','man','22')
# s2 = Chinese('alex2','woman','23')
# s3 = Chinese('alex3','man','21')
# print(s1.country)
# s1.tell_info()
#
#
# class Student:
#     count = 0
#     country = 'china'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         Student.count += 1
#
#
#     def learn(self):
#         country2 = 'american'
#         print('%s is learning'%self.name)
#
#
# print(Student.__dict__)
# stu1 = Student('张三', 18, '女')
# stu2 = Student('李四', 28, '女')
# stu3 = Student('王五', 38, '女')
# print(Student.__dict__)
# print(Student.count)
# print(stu1.country)
# print(Student.__dict__['country'])
#
#
# class Math2:
# #与上面的案例相比，去掉初始化函数
#     def Add(self,c,d):
#         return c+d
#
# z=Math2().Add(3,4)
# print(z)