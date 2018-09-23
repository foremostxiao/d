
# 1
# 现在有个需求，看列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],要求你把列表里的每个值加1，你怎么实现？你可能会想到2种方式

# 普通版本
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
# for i in list1:
#     list2.append(i+1)
# print(list2)
#
# # 文艺青年 Python3 中map 要显示成列表，再前面加list
# a = map(lambda x:x+1,list1)
# print(a)
# print('Python3 中map 要显示成列表，再前面加list:>',list(a))
#
# # 装逼青年版
# b = [i+1 for i in range(0,10)]
# print(type(b))
# print(b)
#
# # 生成器 generator ()
# c = (i+1 for i in range(0,10))
# print(type(c)) # <class 'generator'>
# print(c)
# for n in c:
#     print(n)



# 斐波拉契数列 (Fibonacci)
# a = [1,1]
# i = 2
# while True:
#     j = a[i-1] + a[i-2]
#     a.append(j)
#     i = i + 1
#     if i == 10:
#         print(a)
#         break
# # --------------------------------
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b,end=' ')
#         a,b = b,a+b
#         n = n+1
#     return 'done'
# fib(10)
#
# # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#
# def fib(max):
#     n,a,b = 0,0,1
#
#     while n < max:
#         #print(b)
#         yield  b #把函数执行冻结在这一步，并且把b的值，返回给next()
#         a,b = b,a+b
#
#         n += 1
#
#     return 'done'
# f = fib(10)
# print(fib(10))#<generator object fib at 0x0000000001DE3750>
# print(next(f))#1
# print(next(f))#1
# print(next(f))#2
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# s = '10.3.9.12'
# a = s.split('.')
# print(a)
# ret = []
# for i in a:
#     b = bin(int(i))
#     ret.append(b)
# print(ret)
# str = ''.join(ret) #连接 join() 方法用于将序列中的元素
# # 以指定的字符 连接生成一个新的字符串。
# # print(int(str,2))
# print(str)

# def func(s):
#     l = s.split('.')
#     ret = []
#     for item in l:
#         item = str(bin(int(item)))[2:] #'0b1010' ob是二进制的标识符
#         print(item)
#         if len(item) < 8:
#             n = 8 - len(item)
#             item = ''.join(['0'*n, item])
#         ret.append(item)
#     print(ret)
#
#     temp = ''.join(ret)
#     print(temp)
#     print(int(temp, 2))
#     return ret
#
# func('10.3.9.12')



#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")

# 通过生成器实现协程并行运算
