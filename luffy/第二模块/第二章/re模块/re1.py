# with open("兼职白领学生空姐模特护士联系方式.txt",'r',encoding="utf-8") as f:
#     #file = f.read()
#     # print(file)
#     # data = []
#     for line in f:
#         name,region,height,weight,phone = line.split()
#         if phone.isdigit():
          #if phone.startswith('1') and len(phone) == 11:
#             print(phone)

#正则表达式
import re

#re.findall 把所有匹配的字符放到以 列表中的元素返回
# with open("兼职白领学生空姐模特护士联系方式.txt",'r',encoding="utf-8") as f:
#     data = f.read()
#     a = re.findall("[0-9]{11}",data)
#     #或者a = re.findall("1[0-9]{10}",data)
#     print(a)

# re.match从头开始匹配 返回的是对象
# 找字母字符re.match('[a-z]',s)
# 找数字字符re.match('[0-9]',s)
# s = 'abc1d3e'
# print(re.match('[a-z]',s).group())
# print(re.match('[0-9]',s))
# re.search,匹配包含 ,只能返回一个符合的，其他不返回 返回的是对象


#re.search

# pattern = re.search('w','aw,bw,cw,dw')  #匹配结果
# print(pattern)  #返回一个match对象
# print(pattern.group())   #获取一个分组截获的字符串
# print(pattern.start())  #截获字符串的开始索引
# print(pattern.end())  #截获字符串的结束索引



# re.findall 把所有匹配的字符放到以 列表中的元素返回
# s = 'abc1d3e'
# print(re.findall('[a-z]',s))
#
# print(re.findall('[0-9]','a1b2c3'))
#
# print(re.findall('\d+','a21b32c35'))
#以列表的形式返回所有匹配的子串，\d+为匹配1到多个数字


# re.finditer(pattern, string, flags=0)
#
# 搜索string，返回访问每一个匹配结果的match对象的迭代器
# pat = re.finditer('\d+','aa123bb456cc')  #返回match对象的一个迭代器
# print(pat)
#
# for i in pat:     #循环迭代器取值
#   print(i.group())


# re.sub(pattern, repl, string, count=0, flags=0)
#
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。
# count用于指定最多替换的次数，不知道时全部替换。
# pat = re.sub('\d+','@@@','aaa1bbb22ccc333')
# print(pat)   #替换匹配对象
# print(re.sub('\d+','@@@','aaa1bbb22ccc333',count=2))


# re.compile(pattern,flags=0)
#
# 编译一个正则表达式模式，返回一个模式对象
# import re
# re1 = re.compile(r'hello')   #编译一个正则匹配模式
# print(type(re1))
# print(re.match(re1,'hello world').group())


# re.spilt

# re.split(pattern, string[, maxsplit])
# 按照能够匹配的子串将string分割后返回列表。
#
# maxsplit用于指定最大分割次数，不指定将全部分割。

import re

s='9-2*5/3+7/3*99/4*2998+10*568/14'
print(re.split('[\*\-\/\+]',s))

print(re.split('[\*\-\/\+]',s,3))

