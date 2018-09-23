import sys,os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)  #添加环境变量
from core import user_and_manager_main


def user_choice():
    while True:
        choice = input("""\033[31;1m
请选择序号:（规定ATM用户名不能由纯数字组成，普通用户名长度<=5,管理员用户名>5）
1.ATM普通用户模式
2.ATM管理员模式
>\033[0m""")
        if choice == '1':
            print("""\033[32;1m
格式如下：
帐号：user 密码：abc
帐号：user2 密码：abc
帐号：user3 密码：abc\033[0m""")
            user_and_manager_main.conroller()
        elif choice == '2':
            print("\033[32;1m帐号：manager 密码：abc\033[0m")
            user_and_manager_main.conroller2()
        else:
            print('\033[32;0m----输入错误----\033[0m')
            continue


