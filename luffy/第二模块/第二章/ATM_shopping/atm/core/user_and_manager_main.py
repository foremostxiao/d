import os,time,datetime
import sys,json
#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #找到路径
sys.path.append(BASE_DIR)          #添加路径

from conf import settings
from atm.core import user_conroller
from atm.core import auth
from atm.core import manager_conroller
from shopping import shopping_main
from atm.core import logger


def login(func):
    def inner(*args, **kwargs):
        user_entrance = {  # 存储账户的认证状态，和账户信息
            "user_status": False,
            'data': None}
        while user_entrance["user_status"] is not True:  # 如果用户没有认证则输入密码
            #auth.userjudge()  # 通过userjudge函数 来判断用户和密码是否正确

            """对用户信息进行验证"""
            account = input("Username:").strip()

            f = os.path.join(settings.account_path, "%s.json" % account)  # 读取用户全部信息
            if os.path.isfile(f):
                with open(f,'r', encoding='utf-8') as account_file:
                    data = json.load(account_file)
                    if data['status'] == 1:
                        print(f"用户：{account}已被冻结")
                        exit()
                    if data['status'] == 2:
                        print(f"用户：{account}已被锁定")
                        exit()
                    if data['status'] == 0:
                        auth.userjudge(data, user_entrance, account)

            else:
                print(f"\033[32;0m 用户：{account}不存在\033[0m")
            if  user_entrance["user_status"] == True:
                return func(account)

    return inner
# --------------------------------普通用户认证---------------------------------------------
@login
def conroller(account):
    if not account.isdigit():
        if len(account) <= 5:
            logger.logger_user.error(f"{account}登录成功 ")
            while True:
                user_choice = input("""
1.查看
2.提现
3.还款
4.转账
5.日常消费记录
q.退出
>""").strip()
                if user_choice == '1':
                    user_conroller.view_account_info(account)
                elif user_choice == '2':
                    user_conroller.with_draw(account)
                elif user_choice == '3':
                    user_conroller.pay_back(account)
                elif user_choice == '4':
                    user_conroller.transfer(account)
                elif user_choice == '5':
                    user_conroller.purchase_history(account)
                elif user_choice == 'q':
                    exit()
                else:
                    print('\033[1;31;40m----输入有误----\033[0m')
                    continue
        else:
            print('\033[32;0m----您选择的是用户登录，输入的是管理账户，请重新的输入----\033[0m')

    else:
        print('\033[32;0m----输入非信用卡账户-----\033[0m')

#----------------------- 管理员认证--------------------------------
@login
def conroller2(account):
    if not account.isdigit():
        if len(account) > 5:
            print('----欢迎登陆管理员界面----')
            logger.logger_manager.error(f"{account}登录成功 ")
            while True:
                manager_choice = input("""
1.查看
2.添加账户
3.用户额度
4.冻结
q.退出
>""").strip()
                if manager_choice == '1':
                    manager_conroller.view_account_info()
                elif manager_choice == '2':
                    manager_conroller.add_account()
                elif manager_choice == '3':
                    manager_conroller.limit_balance()
                elif manager_choice == '4':
                    manager_conroller.frozen_account()
                elif manager_choice == 'q':
                   exit()
                else:
                    print('\033[32;0m----输入错误----\033[0m')
                    continue
        else:
            print('----您选择的是管理登录，输入的是普通账户，请重新的输入----')
    else:
        print('\033[32;0m-----输入非信用卡用户账户---------\033[0m')

#-----------------------------购物商城登录认证----------------------------------------------
@login
def shopping_auth(account):
    if account.isdigit():
        while True:
            shopping_choice = input("""
1.进入购物中心选购
2.查看购物记录
q 退出""").strip()
            if shopping_choice == '1':
                shopping_main.shopping_center(account)
            elif shopping_choice == '2':
                path = os.path.join(settings.logs_path,'shopping.log')
                with open(path,'r',encoding='utf-8') as f:
                   shopping_record = f.read()
                if len(shopping_record) == 0:
                    print('----当前购物记录为空-----')
                else:
                    print(shopping_record)
            elif shopping_choice == 'q':
                break
            else:
                print('\033[32;0m----输入有误----\033[0m')
                continue
    else:
        print('\033[32;0m----登录非购物商城帐号----\033[0m')


#--------------------网上银行支付认证---------------------------
# 不能把购物商城的用户名(account)也传参过来，本人不会，也弄不了
@login
def online(account):
    if account.isdigit():
        print('\033[32;0m----输入错误----\033[0m')
    elif len(account) <= 5:
        user_conroller.inter_shopping(account)
    else:
        print('\033[32;0m----输入错误----\033[0m')
