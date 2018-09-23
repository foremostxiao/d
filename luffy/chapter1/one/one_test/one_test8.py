#--------------8-------------------
#----a----使用while循环实现输出2-3+4-5+6...+100的和
# sum = 0
# i = 2
# while i <= 100:
#     if i % 2 == 0:
#         sum = sum + i
#     else:
#         sum = sum - i
#     i += 1
# else:
#     print(sum)

#--b--使用while循环实现1，2，3，4，5，7，8，9，11，12
# i=1
# while i<=12:
#     if i !=6 and i !=10:####中间填写---or---错误，比如 i等于6时，(i！=6,False) or (i !=10,True)
#
#         ### if 条件即为True，，继续执行后面语句
#         print(i)
#     i += 1
#


#--c--使用while循环输出100-50，从大到小，比如100，99，98....到50时再从0循环输出到50，然后结束
# count = 0
# while count < 50:
#     print(100-count)
#     count += 1
#     if count == 50:
#         count = 0
#         while count <= 50:
#             print(count)
#             count += 1
#--------------------------------------------------------------------------------------------

for i in range(0,50):
    print(100-i,end='\t')
    print(i)  #print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end='\t')
    print()


#--d---使用while循环实现输出1-100的所有奇数
# count=1
# while count<=100:
#     if count%2!=0:
#         print(count)
#     count=count+1
#
# #--e---使用while循环实现输出1-100的所有奇数
# #
# count=1
# while count<=100:
#     if count%2==0:
#         print(count)
#     count=count+1
