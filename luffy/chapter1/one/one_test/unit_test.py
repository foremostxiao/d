#---作业题目: 编写登陆认证程序-----

# -------基础需求--------------
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
# user_name='xiaolei'
# pass_word='123'
#
# while True:
#     username = input("用户名：")
#     if username != user_name:
#         print("用户名不存在，请重新输入:")
#         continue
#     else:
#         count = 3
#         while True:
#             password = input("密码：")
#
#             count-=1
#             if password==pass_word:
#                 print("登录成功，欢饮您！")
#                 break
#             else:
#                 print(f"输入错误，还有{count}次机会输入")
#             if count == 0:
#                 break #跳出本次while循环
#     if count==0:
#         break #跳出本次while循环
#     if password==pass_word:
#
#         break
# print("提示：只允许输错三次！")

# ---------升级需求------------------------
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
# 用户指同一个账户，累计输错三次密码就锁定
####---{}---花括号，{'x':5,'y':}
#　字典是由花括号{}来包含其数据的，花括号内包含键(key)和其对应的值(value)，一对键和值成为一个项，键和值用冒号:隔开，
# 项和项之间用逗号,隔开，空字典就是不包含任何项的字典，也可理解为空字典就是花括号内不包含任何内容，直接使用花括号{}表示。

# user_name = ['xiaolei','xiaoman','lixia']
# pass_word=['123','456','789']
# count = 0
# while True:
#     username = input("用户名：")
#
#     if username not in user_name:
#         print("您输入的用户不存在,请重新输入：")
#         continue
#     else:
#         with open('account_lock.txt','r') as account:
#             user=account.read()
#             if username in user:
#                 print(f"{username}该用户被已锁定")
#                 break
#     password=input("请输入密码：")
#     if username == user_name[0] and password==pass_word[0]:
#         print(f"登录成功，欢迎您：{username}")
#         break
#     elif username == user_name[1] and password==pass_word[1]:
#         print(f"登录成功，欢迎您：{username}")
#         break
#     elif username == user_name[2] and password==pass_word[2]:
#         print(f"登录成功，欢迎您：{username}")
#         break
#     else:
#         print("密码错误，请重新输入：")
#         count+=1
#         if count>=3:
#             account_lock=open ('account_lock.txt','a')
#             account_lock.write(username)
#             account_lock.close()
#             break
# print("用户三次认证失败后账户已被锁定")

#
user_name = ['xiaolei','xiaoman','lixia']
pass_word=['123','456','789']

while True:
    username = input("用户名：")

    if username not in user_name:
        print("您输入的用户不存在,请重新输入：")
        continue
    else:
        with open('account_lock.txt','r') as account:
            user=account.read()
            if username in user:
                print(f"用户{username}被已锁定")
                break

    count=3
    while True:

        password=input("请输入密码：")
        if username == user_name[0] and password==pass_word[0]:
            print(f"登录成功，欢迎您：{username}")
            break #跳出当前的whlie循环
        elif username == user_name[1] and password==pass_word[1]:
            print(f"登录成功，欢迎您：{username}")
            break
        elif username == user_name[2] and password==pass_word[2]:
            print(f"登录成功，欢迎您：{username}")
            break
        else:
            count -= 1
            print(f"密码错误，还有{count}次机会重新输入：")

            if count==0:
                account_lock=open ('account_lock.txt','a')
                account_lock.write(username)
                account_lock.close()
                print(f"{username}已被锁定")
                break
    if username == user_name[0] and password == pass_word[0]:

        break  # 跳出当前的whlie循环
    elif username == user_name[1] and password == pass_word[1]:

        break
    elif username == user_name[2] and password == pass_word[2]:

        break
    else:
        break
print("提示：用户三次认证失败后账户将被锁定")



