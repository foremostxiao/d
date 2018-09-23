import re
# print(re.findall('abb+','abbab'))
# print(re.findall('ab+','abab'))
# print(re.findall('ab+','aaabbb'))
#
# #分组匹配
# print(re.search('[a-z]+[0-9]+','alex123').group())
#
# print(re.search('([a-z]+)([0-9]+)','alex123').group())
#
# s = '429005199304075271'
# #方法一
# print(re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s).group())
# # 方法二6
# res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
# print(res.groupdict())

# re.spilt以匹配到的字符当做列表分隔符
s = 'alex22jack23rainjinxin50'
#整体['alex', 'jack', 'rainjinxin', '']
print(re.split('\d+',s))
#单个['alex', '', 'jack', '', 'rainjinxin', '', '']
print(re.split('\d',s))
pat = re.sub('\d','@@@','aaa1bbb22ccc333')
print(pat)



# re.sub 匹配字符并替换,每匹配一次就替换一次
print(re.sub('[a-z]','sb','王abc123'))

# re.fullmatch
print(re.fullmatch('\w+@\w+\.(com|cn|edu)','alex@oldboyedu.cn').group())

# re.match
obj = re.match('\d+','123uuasf').group()
print(obj)

# 标志位 Flags
print(re.search('a','Alex',re.I).group())