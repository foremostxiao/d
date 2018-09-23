
print('111','222',sep=',')
#
# # print之 file
msg = '又回到最初的起点'
f = open('print_tofile','w',encoding='utf-8')
print(msg,'记忆中你青涩的脸',sep='|',end='')


# python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes
# python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法

# import time
# for n in (100000, 200000, 300000, 400000):
#     data = b'x'*n
#     start = time.time()
#     b = data
#     print(b)
#     while b:
#         b = b[1:]
#     print('bytes', n, time.time()-start)

# for n in (100000, 200000, 300000, 400000):
#     data = b'x'*n
#     start = time.time()
#     b = memoryview(data)
#     while b:
#         b = b[1:]
#     print('memoryview', n, time.time()-start)

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))  # 使用 lambda 匿名函数
