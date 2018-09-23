# ## 第二模块
# 3 - 5
# 分钟总结第二模块学习内容
#
# ### 第一模块内容
# 1.
# 请写出 “路飞学城alex” 分别用
# utf - 8
# 和
# gbk
# 编码所占的位数（口述）
#
# 2.
# python有哪几种数据类型，分别什么？哪些数据类型是有序的。
#
#
# 3.
# 列表和字典的pop方法有什么区别。
#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
#
# ###
# 1.
# read, readline, readlines的区别 （口述）
#
#
#
# 2.
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
#
# 3.
# 函数的参数（口述）
#
# - 形参和实参的区别。
#
#
#
# - 位置参数，默认参数，关键参数，非固定参数的顺序。
#
#
#
# - 解释下参数的作用。
#
#
# - 什么数据类型可以做实参。
#
#
#
# 4.
# 解释一下是否会报错，原因是什么？要是不报错打印什么值？报错的可以怎么改就不报错？ （口述）
#
# ```python
#
#
# def test():
#     print(luffy)
#
#
# luffy = "the king of sea."
# test()
# ```
#
# ```python
#
#
# def test():
#     print(luffy)
#     luffy = 'e'
#
#
# test()
# luffy = "the king of sea."
# ```
#
# ```python
#
#
# def test():
#     luffy = 'e'
#     print(luffy)
#
#
# test()
# luffy = "the king of sea."
# ```
#
# 5.
# li = [1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 8, 3]
# 利用生成器功能，写一个所有数值乘以2的功能。（编程）
# li = [i*2 for i in [1,2,3,4]]
# print(li)
#
#
# 6.
# isinstance('s', str)
# 与
# tupe('s') is str
# 效果是否一样？（口述）
#
#
#
# 7.
# 序列化 - json，xml，pickle （口述）
# json和pickle的区别是什么？
#
#
#
#
# 8.
# 描述写硬盘的编码转变（UTF - 8
# 格式，系统格式GBK） (口述)
#
# 9.
# 解释以下代码含义 （口述）
#
# ```python
# from functools import reduce
#
# reduce(lambda x, y: x + y, range(10))
# ```
#
# 10.
# 打印日志11 / 26 / 2017
# 10: 44:21
# PM
# bug
# 24
# 并写入文件example.log中 （编程）
# import logging
# logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
# logging.warning('bug 24')
#
# linux创建目录时候可以使用filemode = 0o755
# 来指定权限
#
#
# def test():
#     print(luffy)
# luffy = "the king of sea."
# test()
#
# # def test():
# #     print(luffy)
# #     luffy = 'e'
# #
# # test()
# # luffy = "the king of sea."
#
# def test():
#     luffy = 'e'
#     print(luffy)
# test()
# luffy = "the king of sea."
# if isinstance('s',str) == type('s') is str:
#     print('123')

# n = "路飞学城"
# print(n)
# #编码encode  解码decode
# n2 = n.encode('utf-8').decode('utf-8')
# print(n2)
# print(type(n2))
# from functools import reduce
# print(reduce(lambda x, y: x+y, [1,2,3,4,5]))  # 使用 lambda 匿名函数
#
# import logging
# logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s')
# logging.warning('bug 24')

# user_status = False
# def login(func):
#     def inner():
#         global user_status
#         if user_status == False:
#             count = 3
#             while count > 0:
#                 with open('test.txt','r+',encoding='utf-8') as file:
#                     data = eval(file.read())
#                     name_user = input('name:').strip()
#                     pass_word = int(input('password:').strip())
#                     if name_user == data['name']:
#                         if data['status'] == 0:
#                             if pass_word == data['password']:
#                                 print('welcome')
#                                 user_status = True
#                                 break
#                             else:
#                                 count -= 1
#                                 if count == 0:
#                                     data['status'] = 1
#                                     print('帐号以锁定')
#                                     file.seek(0)
#                                     file.truncate()
#                                     file.write(data)
#                                     exit()
#                                 else:
#                                     print(f"您还有{count}次机会输入")
#                                     continue
#                         else:
#                             print('账户已锁定')
#                             exit()
#                     else:
#                         print('输入账户名有误')
#         if user_status == True:
#             func()
#     return inner
# @login
# def america():
#     print('123')
# @login
# def japan():
#     print('456')
# america()
# japan()
#
#

