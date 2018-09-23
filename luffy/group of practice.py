# 2018/8/19

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#A0 = {'a':1,'b':2,'c':3,'d':4,'e':5}
A1 = range(10)
#A1 = [0,1,2,3,4,5,6,7,8,9]
A2 = [i for i in A1 if i in A0]
#A2 = [] # 当对字典进行in判断是，判断的是key
A3 = [A0[s] for s in A0]
#A3 = [1,2,3,4,5]
A4 = [i for i in A1 if i in A3]
#A4 = [1,2,3,4,5]

# python中is和==的区别
# Python中对象包含的三个基本要素，分别是：id(身份标识) 、type(数据类型)和value(值)。
# ‘==’比较的是value值
# ‘is’比较的是id

#https://blog.csdn.net/weixin_40862231/article/details/79504455

#2018/8/20
num = input('输入非负整数(至少有两位):>')
