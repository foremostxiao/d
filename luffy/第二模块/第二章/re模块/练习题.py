# 1 验证手机号是否合法
import re
# phone_number = input('phone_number:>').strip()
# print('phone_number:>',type(phone_number))
# if re.findall('1[0-9]{10}',phone_number):
#     print('合法')

# 2 验证邮箱是否合法
#
import re
# email = input('email:>').strip()
# if re.fullmatch('^\w+@\w+\.[a-zA-Z]{3}$',email):
#     print('email合法')
# 3 开发一个简单的python计算器，实现加减乘除及拓号优先级解析
#用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# 等类似公式后，必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，
# 运算后得出结果，结果必须与真实的计算器所得出的结果一致

#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(eval( '3 * 3' ))
print(eval( '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/(16-3*2))'))

# 从里面向外
s = 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
# print(re.search('\([^()]+\)',s).group())
result='aakk123ddd55kk66'

print(re.sub("\d+","A",result))#123整体替换A

#2.将字符串的前4位数字转换为A

print(re.sub("\d","A",result,4))