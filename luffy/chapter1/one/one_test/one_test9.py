#-------1------
#
# username=input("name: ")
# site=input("site ")
# hobby=input("hobby ")
# print(f"敬爱的{username},最喜欢在{site},从事他喜欢的{hobby}")


# #----2--输入一年份，判断该年份是否是闰年并输出结果
#  #凡符合下面两个条件之一是闰年（1）能被4整除但不能被100整除（2）能被400整除
## 2004 2000 2008 2012 2016 2020每隔四年
# year=int(input("请输入年份： "))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year}年是闰年")
# else:
#     print(f"{year}年不是闰年")

#--3---假设一年定期利率为3.25%，计算一下需要过多少年，一万元定期存款连本带息能翻番？
#import  math  ---if语句不是循环语句，不能指望它判断后循环判断-------

# n=1
# if n<3:
#     n=n+1
#     print("hah")
# else:
#     print(n)

#-----正确方案----------------

n=1
while ((1+0.0325)**n)<2:
    n += 1
    pass
else:
    print(n)

# money = 10000
# rate = 0.0325
# years = 0
# while money <= 20000:
#     years += 1
#     money = money * (1 + rate)
# print(str(years))