# 函数基础：

# 1、写函数，计算传入数字参数的和。（动态传参）
# def sum(x,y):
#     return x+y
#
# print(sum(2,3))
#
# #美 /'læmdə/ 匿名函数
# sum = lambda x,y:x+y
# print(sum(2,3))

# 2、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
# 修改列表中字符串首字母大写


# def modify_file(a):
#     file = open(a, 'r+', encoding='utf-8')
#     data_list = []
#     f = file.readlines()
#     print(len(f))
#     for line in f:
#         # 修改后必须赋值否则无效
#         line = line.capitalize()
#         data_list.append(line)
#     file.seek(0)
#     file.truncate()
#     for line in data_list:
#         file.write(line)
#     file.close()
# modify_file('test.txt')

# capitalize() 函数补充
#
# 需要注意的是：
#
# 1、首字符会转换成大写，其余字符会转换成小写。
#
# 2、首字符如果是非字母，首字母不会转换成大写，会转换成小写,其余也转化为小写。

# 3、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
# def check(a):
#     if type(a) == str:#字符串检查长度判断是否为空
#         if len(a) == 0:
#             print(f"{type(a)},为空内容")
#     for i in a:
#         if i == '' :
#             print(f"{type(a)},含有空内容")
#
# need_check_str = ''
# check(need_check_str)
#
# need_check_list = ['a','b',1,'','q']
# check(need_check_list)
#
# need_check_tuple = (1,2,'','qq')
# check(need_check_tuple)

# 4、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def check_dict(a):
#     for k,v in a.items():
#         if len(v) > 2:
#             a[k] = v[0:2]
#     return a
#
# b = check_dict(dic)
# print(b)

# 5 解释闭包的概念
# 闭包(closure)
# 是函数式编程的重要的语法结构。函数式编程是一种编程范式(而面向过程编程和面向对象编程也都是编程范式)。
# 在面向过程编程中，我们见到过函数(function)；在面向对象编程中，我们见过对象(object)。
# 函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。
# 闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

#函数进阶：
#例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
# 1、写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 方块，梅花，红心，黑桃
# def playing_card():
#     playing_card_list = []
#     color = ['方块','梅花','红心','黑桃']
#     card = ['J','Q','K','A']
#     for i in range(2,11):
#         card.insert(i-2,i)
#     for index in card:
#         for j in color:
#             playing_card_list.append((j,index))
#     #print(playing_card_list)
#     return playing_card_list
# playing_card()
# print(playing_card())

# 2、文件处理
# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}
# 第一种直接运动内置函数
# def max_min(a):
#     dict = {}
#     dict['max'] = max(a)
#     dict['min'] = min(a)
#     return dict
# s = [2,3,6,4,3,-100]
# print(max_min(s))
#
# # 第二种
# def max_min(*args):
#     the_max = args[0]
#     the_min = args[0]
#     for i in args:
#         if i > the_max:
#             the_max = i
#         if i < the_min:
#             the_min = i
#     return {'max': the_max, 'min': the_min}
# print(max_min(2,3,6,4,3,-100))
# # 第三种冒泡法排序的方法
# def max_min(b):
#     for i in range(0,len(b)-1):
#         for j in range(i+1,len(b)):
#             if b[i] > b[j]:
#                 k = b[i]
#                 b[i] = b[j]
#                 b[j] = k
# b = [2,3,6,4,3,-100]
# max_min(b)
# print({'max': b[-1], 'min': b[0]})
# 3、写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
#
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积

# *args 返回是元组的形式
# ('长方形的面积为：', 12)
# ('圆的面积为：', 28.274333882308138)
# ('正方形的面积为：', 9)

# import math
# def area(name,*args):
#     def areas_rectangle(x,y):
#         return "长方形的面积为：",x*y
#     def area_square(x):
#         return "正方形的面积为：",x**2
#     def area_round(r):
#         return '圆的面积为：',math.pi*r*r
#     if name == 'rectangle':
#         return  areas_rectangle(*args)
#     if name == 'square':
#         return area_square(*args)
#     if name == 'round':
#         return area_round(*args)
# print(area('rectangle', 3, 4))
# print(area('round', 3))
# print(area('square', 3))

# 4、写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)
# 计算7*6*5*4*3*2*1

# def cal(nmuber):
#     s = 1
#     for i in range(1,nmuber+1):
#         s = s*i
#     return s
# print(cal(5))

# 递归函数法
# def cal(nmuber):
#
#     if nmuber == 1:
#        return 1
#     else:
#         return nmuber*cal(nmuber-1)
# print(cal(4))

# 5、编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
#dict_file = eval(file) # 字符串转为字典
# user_status = False
# def login(func):
#     def inner(*args,**kwargs):
#         global user_status
#         while True:
#             if user_status == False:
#                 username = input('name:>').strip()
#                 password = input('password:>').strip()
#                 with open('user_info.txt','r+',encoding='utf-8') as f:
#                     userinfo = f.read().strip()
#                     userinfo = eval(userinfo)
#                     print(userinfo)
#                     if username in userinfo['name'] and password == userinfo['password']:
#                         print('-------welcome-------')
#                         user_status = True
#                         break
#                     else:
#                         print('name or password wrong')
#                         continue
#         if user_status == True:
#             return func(*args, **kwargs)
#     return inner()


# @login
# def home():
#     print('-----首页-----')
# home()
# @login
# def japan():
#     print('----daoguo-----')
# japan()
#
#
#

# user_tatus = False
# def login(func):
#     def inner():
#         global user_tatus
#         if user_tatus == False:
#             user_name = input('name:').strip()
#             pass_word = input('password:').strip()
#             with open('user_info.txt','r',encoding='utf-8') as file:
#                 f = eval(file.read())
#                 if f['name'] == user_name and f['password'] == pass_word:
#                     user_tatus = True
#                 else:
#                     print('wrong name or password')
#         if user_tatus == True:
#             func()
#     return inner
#
# @login#语法糖
# def america():
#     print('nice')
# @login
# def japan():
#     print('good')
# america()
# japan()


# 生成器和迭代器
# 1 # 生成器和迭代器的区别？
# list = [1,2,34,5]
# it = iter(list)
# print(next(it))
# print(it_next_())
# print(next(it))
# print(next(it))

# 2 生成器generator有几种方式获取value？
# 两种方式获取：
#    for  循环
#    next 获取
import  sys
# def fib(max):
#     n,a,b = 0,0,1
#
#     while n < max:
#         #print(b)
#         yield  b
#         a,b = b,a+b
#         n += 1
#     return 'done'
# g = fib(10)
#
# while True:
#     try:
#         x = next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print('generator return value:',e.value)
#         break
# # 普通函数         生成器函数 - 斐波那契
# def fib(max):
#     n,a,b = 0,0,1
#
#     while n < max:
#         print(b)
#         #yield  b
#         a,b = b,a+b
#         n += 1
#     return 'done'
# fib(10)

# 内置函数
# 1 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=['alex','wupeiqi','yuanhao','nezha']
# def change(x):
#     return x+'_nice'
# print(map(change,name))
#
# print(list(map(lambda x:x+'_nice',name)))

# 2、用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num = [1,3,5,6,7,8]
# def choice(x):
#     if x %2 == 0:
#         return x
# ret = filter(choice,num)
# print(list(ret))
# print(list(filter(lambda x:x%2==0,num)))

# 3 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65},
# ]
# # 计算购买每支股票的总价
# #
# # 用filter过滤出，单价大于100的股票有哪些
#
# for index in range(len(portfolio)):
#     print(f"{portfolio[index]['name']}的股票总价为:{portfolio[index]['shares']*portfolio[index]['price']}")
# for index in range(len(portfolio)):
#     if portfolio[index]['price'] > 100:
#         print('股票单价大于100的有：',portfolio[index]['name'])
#
#
# f = filter(lambda d: d['price'] >= 100, portfolio)
# print(list(f))

# List = [1, 2, 1, 2, 1, 13, 3, 3, 4, 4, 2, 6, 7, 8, 8, 9]
# print(set(List))