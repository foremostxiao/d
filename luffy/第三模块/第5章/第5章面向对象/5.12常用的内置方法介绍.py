# 把对象做成字典属性，自动初始化执行
#---------------------------item系列------------------------------------

# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):    # item='name'
#         print('getitem..')
#         return self.__dict__[item]  # self.__dict__[name]
#
#     def __setitem__(self, key, value):
#         print('setitem')
#         # print(key,value)
#         # self.key = value  #　错误演示　{'name': 'alex', 'key': 'male'}
#         self.__dict__[key] = value  # {'name': 'alex', 'sex': 'male'}
#
#     def __delitem__(self, key):
#         print('delitem')
#         # print(key)
#         # del self.__dict__[key]
#         self.__dict__.pop(key)
#
# f = Foo('alex')
#
# # 1.查看属性
# # obj.属性名
# print(f['name'])    # 查看属性obj.name
# # print(f['namexxx'])    # 没有namexxx属性
# print('-----------------------------------')
#
# # 2.设置属性
# f['sex'] = 'male'  # 添加属性
# print(f.__dict__)
# print(f.sex)
# print('-----------------------------------')
# # 3.删除属性
# # del obj.name
# del f['name']
# print(f.__dict__)


# 自动触发执行
# 对象可以变成字典对象，可以像字典一样的操作



#-------------------__str__,__repr__,__format__---------------------------

# 改变对象的字符串显示__str__,__repr__
# 自定制格式化字符串__format__


# str 方法
# d = dict({'name':'alex'})
# print(isinstance(d, dict))
# print(d)
#
# # str函数或者print函数--->obj.__str__()
# # repr或者交互式解释器--->obj.__repr__()
# # 如果__str__没有被定义,那么就会使用__repr__来代替输出
# # 注意:这俩方法的返回值必须是字符串,否则抛出异常
#
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print('===>str')
#         return 'aaaa'   # 返回值必须是字符串,否则抛出异常
#
# obj = People('alex', 11)
# print(obj)  # 执行obj.__str__()


# --------------------------------------__del__-----------------------------------------

class Foo:

    def __del__(self):
        print('执行我啦')
f1=Foo()
del f1
print('------->')
