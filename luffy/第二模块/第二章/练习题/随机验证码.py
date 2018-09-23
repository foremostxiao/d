#写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母.

# def choice():
#     global ran1,ran2,ran3
#     ran1 = random.randint(0,9) # randint()头尾都包括
#     ran2 = chr(random.randint(65,90))# 大写
#     ran3 = chr(random.randint(97,122))# 小写
# def random_num():
#     global code
#     code = ''
#     for i in range(3):#生成为3位数的验证码
#         choice()
#         add = random.choice([ran1,ran2,ran3])
#         code = ''.join([code,str(add)])
#     return code
# import random
# choice()
# code2 =''.join([str(ran1),str(ran2),str(ran3)])
# random_num()
# print(''.join([code2,code]))

#-----------------------------------
#使用 string模块
# 在大、小写、数字中随机返回6位数
import string,random
s = ''.join(random.sample(string.ascii_letters + string.digits, 3))
ran1 = random.randint(0,9) # randint()头尾都包括
ran2 = chr(random.randint(65,90))# 大写
ran3 = chr(random.randint(97,122))# 小写
code =''.join([str(ran1),str(ran2),str(ran3)])
print(''.join([code,s]))

