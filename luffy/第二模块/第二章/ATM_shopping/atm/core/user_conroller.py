import json
import os
import sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#找到路径
sys.path.append(BASE_DIR)
from conf import settings
from atm.core import logger


def view_account_info(account):
    """查看用户信息"""
    path = os.path.join(settings.account_path, f"{account}.json")
    user_data = json.load(open(path, 'r', encoding="utf-8"))
    logger.logger_user.debug(f"查看{account}信息 ")
    print(user_data)
# 提现
def with_draw(account):
    withdraw_money = int(input('\033[32;0m请输入提现金额：>\033[0m').strip())
    path = os.path.join(settings.account_path, f"{account}.json")
    user_data = json.load(open(path, 'r', encoding="utf-8"))  # 获取到用户信息
    if withdraw_money < int(user_data['balance']):
        user_data['balance'] = int(user_data['balance'] - withdraw_money - withdraw_money*0.05)
        json.dump(user_data,open(path, 'w', encoding="utf-8"))
        print(f"\033[31;1m提现成功提取{withdraw_money},余额{user_data['balance']}\033[0m")
        logger.logger_user.warning(f"{account}--账户取款{withdraw_money} ")
    else:
        print('\033[31;1m----提现超过信用卡余额额度----\033[0m')
# 还款
def pay_back(account):
    path = os.path.join(settings.account_path, f"{account}.json")
    user_data = json.load(open(path, 'r', encoding="utf-8"))  # 获取到用户信息
    print(f"\033[31;1m剩余余额额度{user_data['balance']},最高还款金额{user_data['credit_limit']-user_data['balance']}\033[0m")
    payback_money = int(input('请输入还款金额：>').strip())
    if payback_money > int(user_data['credit_limit']-user_data['balance']):
        print('\033[31;1m---------超出还款额度-------\033[0m')
    else:
        user_data['balance'] = int(user_data['balance']) + payback_money
        json.dump(user_data, open(path, 'w', encoding="utf-8"))
        user_data = json.load(open(path, 'r', encoding="utf-8"))
        print(f"\033[31;1m本次还款{payback_money},余额为{user_data['balance']},剩余还款{user_data['credit_limit']-user_data['balance']}\033[0m")
        logger.logger_user.warning(f"{account}--还款{payback_money}")
# 转账
def transfer(account):
        while True:
            transfer_account = input("""\033[31;1m
请输入对方账户：
q 退出
>\033[0m""").strip()
            if not transfer_account.isdigit():
                if len(transfer_account) <= 5:
                    if transfer_account == 'q':
                        break
                    f = os.path.join(settings.account_path, f"{transfer_account}.json")
                    if os.path.isfile(f):
                        path = os.path.join(settings.account_path, f"{account}.json")
                        if f == path:
                            print('\033[32;0m---您输入的是自己账户----\033[0m')
                        else:
                            user_data = json.load(open(path, 'r', encoding="utf-8"))  # 获取到用户信息
                            print(f"您的信用卡余额额度为{user_data['balance']}")
                            transfer_money = input("""
        请输入转账金额：
        q 退出
        >""").strip()
                            if transfer_money == 'q':
                                break
                            if int(transfer_money) < int(user_data['balance']):
                                transfer_data = json.load(open(f, encoding="utf-8"))  # 获取到用户信息
                                transfer_data['balance'] = transfer_data['balance'] + int(transfer_money)
                                json.dump(transfer_data, open(path, 'w', encoding="utf-8"))
                                print(f"转款成功{transfer_money}")
                                logger.logger_user.warning(f"{account}--转款给{transfer_account}-{transfer_money}")
                                #把信用卡余额再次写入文件
                                user_data['balance'] = user_data['balance'] - int(transfer_money)
                                json.dump(user_data, open(path, 'w', encoding="utf-8"))
                            else:
                                print('\033[32;0m----转款金额超出信用卡余额额度----\033[0m')
                    else:
                        print('\033[32;0m---该账户不存在----\033[0m')

                else:
                    print('\033[32;0m----输入非信用卡账户-----\033[0m')
            else:
                print('\033[32;0m----输入非信用卡账户-----\033[0m')
def purchase_history(account):
    path = os.path.join(settings.logs_path, 'shopping.log')
    path2 = os.path.join(settings.logs_path, 'atm_user.log')
    with open(path, 'r', encoding='utf-8') as f:
        file = f.readlines()
        for i in file:
            i.strip()
            i.split('--')
            if 'WARNING' in i and account in i:
                print("shopping:",i.strip())
    with open(path2, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
        for j in file2:
            j.strip()
            j.split('--')
            if 'WARNING' in j and account in j:
                print("atm_user:",j.strip())
#-------------------信用卡网上银行支付接口-------------------------------------


def inter_shopping(account):
    # account为信用卡账户
    path = os.path.join(settings.account_path, f"{account}.json")
    user_data = json.load(open(path, 'r', encoding="utf-8"))
    shop_car_account = input('请再次输入购物商城账户名：>')
    # shop_car_account 为购物商城账户
    path2 = os.path.join(settings.account_path, f"{shop_car_account}_shop_car.json")
    shop_car_data = json.load(open(path2,'r',encoding='utf-8'))
    shop_price = 0
    for shop_list in shop_car_data:
        shop_price = shop_price + shop_list["price"]
    if shop_price < int(user_data['balance']):
        user_data['balance'] = user_data['balance'] - shop_price
        json.dump(user_data, open(path, 'w', encoding="utf-8"))
        print(f"成功支付{shop_price},信用卡余额{user_data['balance']}")
        logger.logger_shopping.warning(f"{shop_car_data}--{account}--消费金额{shop_price}")
    else:
        print('----支付金额超过信用卡余额额度----')
