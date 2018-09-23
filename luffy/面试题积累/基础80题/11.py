# 11、python递归的最大层数？

#-------10的阶层-----------
# def fun(n):
#     while True:
#         if n == 1:
#             return 1
#         return n*fun(n-1)
# b = fun(10)
# print(b)

# def fun(n):
#     print(n)
#     n += 1
#     fun(n)
# print(fun(0))

#
def foo(n):
    print(n)
    n += 1
    foo(n)


if __name__ == '__main__':
    foo(1)

# import sys
# sys.setrecursionlimit(100000)
# def foo(n):
#     print(n)
#     n += 1
#     foo(n)
# if __name__ == '__main__':
#     foo(1)