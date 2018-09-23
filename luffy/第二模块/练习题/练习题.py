# 1.有如下字符串：n = "路飞学城"（编程题）
#
# - 将字符串转换成utf-8的字符编码的字节，再将转换的字节重新转换为utf-8的字符编码的字符串
# - 将字符串转换成gbk的字符编码的字节，再将转换的字节重新转换为utf-8的字符编码的字符串
# n = "路飞学城"
# #编码encode  解码decode
# print(n.encode('utf-8'))
# print(n.encode('utf-8').decode('utf-8'))
# #----------------------------------------
# print(n.encode('gbk'))
# #以什么样的形式编码就要以什么样的什么解码
# print(n.encode('gbk').decode('gbk').encode('utf-8').decode('utf-8'))



# 2，读文件找到第9个字符，华 ，找到第二行的 实，删除最后一行 写入文件
# 桃之夭夭，灼灼其华。之子于归，宜其室家。
# 桃之夭夭，有蕡其实。之子于归，宜其家室。
# 桃之夭夭，其叶蓁蓁。之子于归，宜其家人。
import re
# with open('test.txt','r',encoding='utf-8') as file:

   #------------华
    # file.seek(3*8)
    # print(file.read(1))
   #------------实
    # file.seek(3*28+2)#换行符\n算两个字节
    # print(file.read(1))#read(size)读的是字符数
#----------------第一种  删除最后一行
#     f = file.readlines()
#     del f[2]
# with open('test.txt','w',encoding='utf-8') as file2:
#
#     for i in f:
#         file2.write(str(i))
# ----------------第二种删除
#     f = file.readlines()
#     f.pop()
#     with open('test.txt', 'w', encoding='utf-8') as file2:
#         for i in f:
#             file2.write(str(i))


# 3 求出函数执行的时间，利用装饰器
# import time
# def time_func(func):
#     def wrapper(a,b):
#         time_start = time.time()
#         ret = func(a,b)
#         time_end = time.time()
#         print(time_end - time_start)
#         return ret#没有这个返回值,print()为空
#     return wrapper
# @time_func
# def x(a,b):
#     time.sleep(1)
#     return a+b
# print(x(1,8))

import time
# def login(func):
#     def inner():
#         start_time = time.time()
#         ret = func()
#         end_time = time.time()
#         print(end_time - start_time)
#         return ret
#     return inner
# @login
# def x():
#     time.sleep(2)
# x()

#-----------------带参数的装饰器-------------------

# import time
# def login(s):
#     def out(func):
#         def inner(a,b):
#             start_time = time.time()
#             ret = func(a,b)
#             end_time = time.time()
#             print(end_time - start_time)
#             return ret
#         return inner
#     if s == 'qq':
#         return out
# @login('qq')
# def x(a,b):
#     time.sleep(2)
#     return a+b
# print(x(1,2))

# 4 作用域
#LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__
# 全局范围：全局存活，全局有效
# 局部范围：临时存活，局部有效
# 1-----------------------
# def test():
#     print(luffy)
# luffy = 'the way to the python'
# test()
#-2---------------------------------
# def test():
#     luffy = 'e'
#     print(luffy)
# luffy = 'the way to the python'
# test()

# 5 li = [1,2,3,5,5,6,7,8,9,9,8,3] 利用生成器功能，写一个所有数值乘以2的功能
# li = [1,2,3,5,5,6,7,8,9,9,8,3]
# # 列表生成式
# f = [i*2 for i in li]
# print(f)
# # 生成器把 [] 变成 () 就行
# f2 = (i*2 for i in li)
# # 一个个打印，取一次执行一次不可取
# print(next(f2))
# print(f2.__next__())#f2.__next__()和next(f2)表达效果相同
# for i in f2:
#     print(i,end=' ')

# 6 .打印日志11/26/2017 10:44:21 PM bug 24 并写入文件example.log中
# import logging
# logging.basicConfig(filename='example.log',format='%(asctime)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
# logging.warning('bug 24')

# 7 json 和 pickle
import json,pickle  # json 可序列化的有 int str list tuple dict 没有集合
# pickle 可序列化python所有数据类型包括函数 pickle 可序列化一些类 但类需要引用
# def canl(n):
#     if n == 0:
#         return True
#     return n*canl(n-1)
# print(canl(4))

# ===> 5 * (4 * (3 * (2 * fact(1))))当n=1时 canl(1)==1
# ===> 5 * (4 * (3 * (2 * 1)))
# 8 闭包 内部函数在外部函数被返回后执行
# def fun1():
#     n = 10
#     def fun2():
#         return n
#     return fun2
# f = fun1()
# print(f())

# 9 生成器 迭代器   #可迭代对象有 str 列表 元组 字典 集合 yield函数
# s = (i for i in range(10))
# print(next(s))#只输出一个
# def fun(n):
#     x = 0
#     while(x<n):
#         yield x #yield返回数据，冻结当前的执行过程
#         x += 1
# s = fun(3)
# print(next(s))
# print(s.__next__())
# print(next(s))
# print(s.__next__())
#判断是否是可迭代对象
# from collections import Iterable,Iterator
# print(isinstance({1,2,3},Iterable))
# s = iter([1,2,3,4,3,2,1])
# print(s.__next__())
# print(next(s))
# for i in s:
#     print(i)

# 10 斐波那契数列
# def fun(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n +1
# print(fun(4))
# 把函数变成生成器#生成器就是迭代器
# def fun(max):
#     n,a,b = 0,0,1
#     while n < max:
#         #print(b)
#         yield b
#         a,b = b,a+b
#         n = n +1
# s = fun(4)
# # print(s.__next__())
# # print(s.__next__())
# print(next(s))
# for i in s:
#     print(i)

# 9. 为此函数加装饰器
#
# def foo():
# 　　print('hello foo')
#
# （1）为此函数加一个装饰器，执行对应函数内容后，将当前时间写入一个文件做一个日志记录。
# （2）改成参数装饰器，即可以根据调用时传的参数决定是否记录时间，比如@logger(True)
import time

# def login(func):
#     def inner():
#         a = str(time.time())
#         b = str(time.strftime('%Y-%m-%d',time.localtime()))
#         c= str(time.localtime())
#         with open('test.txt','a',encoding='utf-8') as f:
#             f.write(a+'\n')
#             f.write(b +'\n')
#             f.write(c + '\n')
#             func()
#     return inner
# @login
# def foo():
#     print('hello foo')
# foo()

#(2)改成参数装饰器，即可以根据调用时传的参数决定是否记录时间，比如@logger(True)
# import time
# def login(func):
#     def inner(s):
#         a = str(time.time())
#         b = str(time.strftime('%Y-%m-%d',time.localtime()))
#         c= str(time.localtime())
#         func(s)
#         if s == True:
#             with open('test.txt','a',encoding='utf-8') as f:
#                 f.write(a+'\n')
#                 f.write(b +'\n')
#                 f.write(c + '\n')
#     return inner
# @login
# def foo(s):
#     print('hello foo')
# foo(True)


#----------------文件处理
#2、有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请将以字母“a”开头的元素的首字母改为大写字母；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# # 方法1
# li2 = []
# for i in li:
#     if i.startswith('a'):
#         li2.append(i.capitalize())
#     else:
#         li2.append(i)
# print(li2)
# # 方法2
# for i in range(len(li)):
#     if li[i][0] == 'a':
#         li[i] = li[i].capitalize()
#     else:
#         continue
# print(li)

# 3 有如下程序, 请给出两次调用show_num函数的执行结果，并说明为什么：
num = 20
def show_num(x=num):
    print(x)
show_num()
num = 30
show_num()

# 4 有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请以列表中每个元素的第二个字母倒序排序；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# print(sorted(li, key=lambda x: x[1], reverse=True))
# #sorted默认以第一个字母进行对比
#
# # 5 有名为poetry.txt的文件，其内容如下，请删除第三行；
# # 昔人已乘黄鹤去，此地空余黄鹤楼。
# # 黄鹤一去不复返，白云千载空悠悠。
# # 晴川历历汉阳树，芳草萋萋鹦鹉洲。
# # 日暮乡关何处是？烟波江上使人愁。
# with open('poetry.txt','r+',encoding='utf-8') as file:
#     f = file.readlines()
#     del f[2]
#     file.seek(0)
#     file.truncate()
#     for i in f:
#         file.write(i)
#         print(i.strip())
# map(func,iterable(可迭代对象))
# file(func,iterable(可迭代对象))
# list(filter(lambda x:x%2==0,num))

# 6 lambda是什么？请说说你曾在什么场景下使用lambda？
# 答案
# lambda函数就是可以接受任意多个参数(包括可选参数)并且返回单个表达式值得函数
#     好处：
#         1.lambda函数比较轻便，即用即扔，适合完成只在一处使用的简单功能
#         2.匿名函数，一般用来给filter，map这样的函数式编程服务
#         3.作为回调函数，传递给某些应用，比如消息处理

# 7 题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
#要求：三个骰子，摇大小，每次打印摇骰子数。
# import random
# def login(func):
#     def inner():
#         money = int(input('请输入金额:').strip())
#         while True:
#             big_small = input("""
# 请输入：is_big = 11 <= total <= 18/is_small = 3 <= total <= 10
# 大
# 小
# """).strip()
#             a = random.randint(1, 6)
#             print(f"第一颗骰子数为{a}")
#             b = random.randint(1, 6)
#             print(f"第二颗骰子数为{b}")
#             c = random.randint(1, 6)
#             print(f"第三颗骰子数为{c}")
#             d = a + b + c
#             if big_small == '大':
#                 if d <= 10:
#                     print(f"您选择{big_small}骰子总和{d}为小,输{money}")
#                     func()
#                     exit()
#                 else:
#                     print(f"您选择{big_small}骰子总和{d}为大,赢{money}")
#                     func()
#                     exit()
#             elif big_small == '小':
#                 if d <= 10:
#                     print(f"您选择{big_small}骰子总和{d}为小,赢{money}")
#                     func()
#                     exit()
#                 else:
#                     print(f"您选择{big_small}骰子总和{d}为大,输{money}")
#                     func()
#                     exit()
#             else:
#                 print('输入错误，请重新输入')
#                 continue
#     return inner
# @login
# def func():
#     print('游戏结束')
# func()
#
