# 匿名函数就是不需要显式的指定函数名
# def calc(x,y):
#     return x**y
# print(calc(2,5))
#
# f = lambda x,y:x**y
# print(f(2,5))
#
# res = map(lambda x:x**2,[1,5,7,4,8])
# for i in res:
#     print(i)
#


# 0 到 9 自乘
data = list(range(0,10))
print(data)
for index,i in enumerate(data):
    data[index] = i*i
print(data)

#--------------------------------
data = list(range(0,10))
def f(n):
    return n**n
print(list(map(lambda x:x*x,data)))


#-----------------------------------------
f = lambda x:x*x
for i in range(0,10):
    print(f(i),end=' ')

