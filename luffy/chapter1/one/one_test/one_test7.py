#7、写代码
#i 实现用户输入用户名和密码，当用户名为seven且密码为123时显示登录成功，否则登入失败
# user_name="seven"
# pass_word="123"
# username=input("用户名：")
# password=input("密码：")
# if user_name==username and pass_word==password:
#     print("登入成功！")
# else:
#     print("登录失败！")




#ii.实现用户输入用户名和密码，当用户名为seven且密码为123时显示登录成功，否则登入失败，失败时允许重新输入三次！

###太复杂了-----
# user_name = "seven"
# pass_word = "123"
# count=1
#
# def fun():
#
#
#         if user_name == username and pass_word == password:
#             print("登入成功！")
#
#         else:
#             print("登录失败！---------------")
#
# #-----主体部分--------------------------
# username = input("用户名：")
# password = input("密码：")
# if user_name == username and pass_word == password:
#     print("登入成功！")
#
# else:
#     print("登录失败！允许在重新登录三次")
#     while count<=3:
#         if count != 0:
#             print(f"第{count}次重新输入")
#         username = input("用户名：")
#         password = input("密码：")
#
#         fun()
#         if user_name == username and pass_word == password:
#             break
#         count+=1
#     else:
#         print("----不能再登录了----")

#-----------按题目要求最多允许三次输入认证！--第二种方法---最终的版本-----------------------
#------------------------定义的函数必须在程序main的前面-比上一种方法更简洁一点---
# user_name = "seven"
# pass_word = "123"
# count=3
# while count > 0:
#     username = input("用户名：")
#     password = input("密码：")
#     count -= 1
#     if user_name == username and pass_word == password:
#         print("登入成功！")
#         break
#     else:
#         print(f"登录失败！还有{count}次机会输入")
#
# else:
#     print("----不能再输入----")
#



#iii.实现用户输入用户名和密码，当用户名为seven或者alex且密码为123时显示登录成功，否则登入失败，失败时允许重新输入三次！

##------------------------定义的函数必须在程序main的前面-比上一种方法更简洁一点----------------------------------------
# user_name = ["seven",'alex']#用列表 if username in user_name
# pass_word ='123'
# count=3
# while count >0:
#     username = input("用户名：")
#     password = input("密码：")
#     count-=1
#     if (username in user_name) and pass_word in password:
#         print("登入成功！")
#         break
#     else:
#         print(f"登录失败！还有{count}次机会输入")
#
# else:
#     print("----不能再输入----")

# user_name = {"seven":'123','alex':'456'}#用列表 if username in user_name
# pass_word ='123'

user_name = ["seven",'alex']#用列表 if username in user_name
pass_word =['123','456']
count=3
while count >0:
    username = input("用户名：")
    password = input("密码：")
    count-=1

    if (username in user_name) and password == pass_word[user_name.index(username)]:
        print("登入成功！")
        break
    else:
        print(f"登录失败！还有{count}次机会输入")

else:
    print("----不能再输入----")