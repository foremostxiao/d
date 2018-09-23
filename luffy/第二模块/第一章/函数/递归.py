# i = 10
# print(int(2.1))

# 递归函数 二分查找
# 1、	用Python实现一个二分查找的函数。
# 给出列表如下，用二分查找判断36在不在其中。
# data = [1,3,6,7,9,14,16,17,18,20,21,22,23,30,32,33,35]



# def binary_search(dataset,num):
#     mid = int(len(dataset)/2)
#     if len(dataset) > 1:
#         if dataset[mid] == num:
#             print(f'找到{dataset[mid]}')
#         elif dataset[mid] > num:
#             print(f"{num}在{dataset[mid]}的左边")
#             binary_search(dataset[0:mid],num)
#         else:
#             print(f"{num}在{dataset[mid]}的右边")
#             binary_search(dataset[mid+1:],num)
#     else:
#         if dataset[0] == num:
#             print('find it',dataset[0])
#         else:
#             print('no find')
# binary_search(data,35)


# 之所以有限制，是为了不让其发生无线调用，占内存  之前的 函数都没结束，都在占内存
# 超过的递归调用的次数，发生错误,,最多可以递归1000次

# 通俗来讲，是因为每个函数在调用自己的时候 还没有退出，占内存，多了肯定会导致内存崩溃。
#
# 本质上讲呢，在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# import  sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500) # 可以增加递归次数
# def recursion(n):
#     print(n)
#     recursion(n+1)
# recursion(1)

# 求阶乘
# def fun(n):
#     if n == 0:
#         return 1
#     return n*fun(n-1)
# d = fun(4)
# print(d)
#

#
# def calc(n):
#     print(n)
#
#     s = int(n/2)
#     if s > 0:
#       return calc(s)
#     else:
#         pass
# calc(10)

# def calc(n):
#     v = int(n/2)
#     print(v)
#     if v > 0:
#         calc(v)
#     print(n)
# calc(10)

# 尾递归
# def cal(n):
#     print(n)
#     return cal(n+1)
# cal(1)
# count = 3
# while True:
#     if count > 0:
#         count -= 1
#         print('welcome')
#         while True:
#             print('123')
#             choice = input('请输入：>')
#             if choice == 'q':
#                 exit()

# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65},
# ]
#
# #用filter过滤出，单价大于100的股票有哪些
# f = filter(lambda d: d['price'] >= 100, portfolio)
# print(list(f))