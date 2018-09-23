import json
import os
import sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from conf import settings
from atm.core import logger

def view_account_info():
    """查看用户信息"""
    print('例如：user,user2,user3')
    user_account = input('请输入要查看的用户名：>').strip()
    if not user_account.isdigit() and len(user_account) <= 5:
        path = os.path.join(settings.account_path, f"{user_account}.json")
        if os.path.isfile(path):
            user_data = json.load(open(path, 'r', encoding="utf-8"))
            print(user_data)
            logger.logger_manager.error(f"查看了{user_account}信息")
        else:
            print('----您输入的用户名有误----')
    else:
        print('\033[32;0m----您输入的用户名有误----\033[0m')



def add_account():
    print('\033[32;0m请依次输入name(规定不能是纯数字)，expire_date(格式)：2020-1-1,satus:0,balance:0,"credit_limit": 15000\033[0m')
    user_account = input("len(name)<=5 :>").strip()
    if not user_account.isdigit():
        if len(user_account) <= 5:
            path = os.path.join(settings.account_path, f"{user_account}.json")
            if not os.path.isfile(path):
                expire_date = input("expire_date:>").strip()
                status = int(input("status :>").strip())
                balance = int(input("balance:>").strip())
                credit_limit = int(input("credit_limit:>").strip())
                path = os.path.join(settings.account_path, f"{user_account}.json")
                add_data = {"expire_date":expire_date,  "status":status, "balance": balance, "credit_limit": credit_limit}
                json.dump(add_data,open(path, 'w', encoding="utf-8"))
                add_data = json.load(open(path, 'r', encoding="utf-8"))
                print(f"新添加的用户信息为{add_data}")
                logger.logger_manager.info(f"添加了名为{user_account}新用户")
            else:
                print('---您输入的用户已存在----')
        else:
            print('input wrong,please:len(name)<=5')
    else:
        print('\033[32;0m--------账户命名错误------------\033[0m')


def limit_balance():
    print('user,user2,user3')
    user_account = input('请选择要操作的用户名：>').strip()
    if not user_account.isdigit() and len(user_account) <= 5:
        path = os.path.join(settings.account_path, f"{user_account}.json")
        if os.path.isfile(path):
            user_data = json.load(open(path, 'r', encoding="utf-8"))
            while True:
                limit_money = input(f"""
            1.提高额度
            2.降低额度
            q.退出
            >""").strip()
                if limit_money == '1':
                    add_money = input('请输入提高额度：>').strip()
                    user_data['credit_limit'] = user_data['credit_limit'] + int(add_money)
                    json.dump(user_data,open(path,'w',encoding='utf-8'))
                    user_data = json.load(open(path, 'r', encoding="utf-8"))
                    print(f"提高额度{add_money},当前总额度{user_data['credit_limit']}")
                    logger.logger_manager.warning(f"给用户{user_account}信用卡提高额度{add_money}")
                elif limit_money == '2':
                    add_money = input('请输入降低的额度：>').strip()
                    user_data['credit_limit'] = user_data['credit_limit'] - int(add_money)
                    json.dump(user_data,open(path,'w',encoding='utf-8'))
                    user_data = json.load(open(path, 'r', encoding="utf-8"))
                    print(f"降低额度{add_money},当前总额度{user_data['credit_limit']}")
                    logger.logger_manager.warning(f"给用户{user_account}信用卡减低额度{add_money}")
                elif limit_money == 'q':
                    break
                else:
                    print('\033[32;0m----输入有误----\033[0m')
                    continue
        else:
            print('\033[32;0m----您输入的用户名有误----\033[0m')
    else:
        print('\033[32;0m----您输入的用户名有误----\033[0m')

def frozen_account():
    print('例如：user,user2,user3')
    user_account = input('请输入要冻结的用户名：>').strip()
    if not user_account.isdigit() and len(user_account) <= 5:
        path = os.path.join(settings.account_path,f"{user_account}.json")
        if os.path.isfile(path):
            user_data = json.load(open(path, 'r', encoding="utf-8"))
            user_data['status'] = 1
            json.dump(user_data,open(path, 'w', encoding="utf-8"))
            print(f"账户{user_account}已冻结")
            logger.logger_manager.error(f"账户{user_account}已冻结")
        else:
            print('----您输入的用户名有误----')
    else:
        print('\033[32;0m----您输入的用户名有误----\033[0m')