
v1 = 1 or 3
v2 = 1 and 3
v3 = 0 and 2 and 1
v4 = 0 and 2 or 1
v5 = 0 and 2 or 1 or 4
# v6 = 0 or Flase and 1
print(v1)

# 短路逻辑--
# 任何以False 开头的 and 语句都会直接处理成 False
print(1 or True)  # 1 ---> 1即为true or 直接输出
print(1 and 2)    # 1 为true 遇到and 继续向下推演 2 也为true  输出2
print(0 and 1)    #输出 0  0为Flase 遇到and  直接输出自己
print(0 or False) # 输出false 0为flase 遇到 or 继续推演
print(0 or True)  # 输出true
s=['1','2','3']
s1 = ':'.join(s)
print(s1)
s2= '1,2,3'
print(s2.split(','))

