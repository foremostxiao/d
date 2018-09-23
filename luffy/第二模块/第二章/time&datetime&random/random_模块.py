#（1）随机小数
# import random
# print(random.random())  #随机大于0 且小于1 之间的小数

import random
# print(random.uniform(0,9))   #随机一个大于0小于9的小数
#
#
#
# #（2）随机整数
print(random.randint(-10,0))  #随机一个大于等于1且小于等于10的整数
#
#
#print(random.randrange(1,10,2))   #随机一个大于等于1且小于等于10之间的奇数，其中2表示递增基数
#print(random.randrange(0,10,2))
#
# #（3）随机返回
# print(random.choice(['123','abc',52,[1,2]]))    #随机返回参数列表中任意一个元素
# print(random.choice('qsfqef'))
# import random
# print(random.sample(['123','abc',52,[1,2]],2))  #随机返回参数列表中任意两个元素，参数二指定返回的数量
# #
# #（4）打乱列表顺序
# lis = [1,2,5,7,9,10]
# random.shuffle(lis)
# print(lis)

#（5）验证码生成器

# import random
# def random_num():
#     code = ''
#     for i in range(4):#生成为四位数的验证码
#         ran1 = random.randint(0,9)
#         ran2 = chr(random.randint(65,90))
#         add = random.choice([ran1,ran2])
#         print(str(add))
#         code = ''.join([code,str(add)])
#     return code
# print(random_num())

# 生成随机字符串
# import string
# a = ''.join(random.sample(string.ascii_lowercase+string.ascii_uppercase + string.digits, 6))
# print(a)
#
# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
#
# print(random.uniform())
# print(random.random())
# print(random.randint(0,1))