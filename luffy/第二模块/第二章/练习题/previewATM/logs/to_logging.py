import json,os,sys

#取出当前文件的父目录，
print(__file__)
dir = os.path.abspath(__file__)
dir2 = os.path.dirname(os.path.dirname(dir))
# 取出json文件的绝对路径
file_path1 = dir2 + "\\" + "account" + "\\" + "luffy.json"
file_path2 = dir2 + "\\" + "account" + "\\" + "tesla.json"
#bank.logs绝对路径
file_path3 = os.path.dirname(dir)+"\\" + "bank.log"


global withdraw,transfer

#日志
# 将日志同时输出到屏幕和日志文件
import logging
#logger提供了应用程序可以直接使用的接口；
logger = logging.getLogger('wed')
logger.setLevel(level = logging.INFO)
#handler将(logger创建的)日志记录发送到合适的目的输出；1
# FileHandler()输出至屏幕
handler = logging.FileHandler(file_path3)
handler.setLevel(logging.INFO)
#formatter决定日志记录的最终输出格式。
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# StreamHandler()输出至屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
#增加指定的Handler
logger.addHandler(handler)
logger.addHandler(console)


print("""
------- Luffy Bank ---------
1. 账户信息
2. 提现
""")
# data = {'balance': 100, 'credit': 50}
# with open(file_path1, 'w', encoding='utf-8') as f:
#     json.dump(data,f)
user_status = False
def login(fun):
    def inner(*args,**kwargs):
        user_name = 'xiao'
        pass_word = '123'
        global user_status
        if user_status == False:
            username = input('user:>').strip()
            password = input('password:>').strip()
            if username == user_name and pass_word == password:
                logger.info('----登录-----')
                print('welcome login...')
                user_status = True
            else:
                print('wrong username or passerword')
        if user_status == True:
            return fun(*args,**kwargs)
    return inner

@login
def transfer():
    tesla_balance = 75
    balance['balance'] = balance['balance'] - tesla_balance * 0.05 - 75

    print(f"购买tesla共花费{tesla_balance * 0.05 + 75},tesla账户增加{tesla_balance}")
    with open(file_path2, 'w', encoding='utf-8') as f2:
        json.dump(tesla_balance, f2)
    with open(file_path1, 'w', encoding='utf-8') as f3:
        json.dump(balance, f3)
@login
def withdraw():
    withdraw_money = int(input('请输入提现金额：').strip())
    if withdraw_money > balance['credit']:
        print(f"提现金额超过信用额度：{balance['credit']}万，请重新输入")
    else:
        balance['balance'] = balance['balance'] - withdraw_money - withdraw_money*0.05
        print(f"剩下余额{ balance['balance']}")
    with open(file_path1, 'w', encoding='utf-8') as f2:
       json.dump(balance, f2)


while True:
    choice = input("""
请选择如下序号：
1. 账户信息
2. 提现
3.转账
q.退出
>
""")
    #  此题前提在luffy 下存入data字典信息
    # data = {'balance': 100, 'credit': 50}
    with open(file_path1, 'r', encoding='utf-8') as f:
        # json.dump(data,f)
        balance = json.load(f)
    if choice == '1':
        logger.info('----显示账户信息-----')
        print(f"当前余额：{balance['balance']}万，信用额度：{balance['credit']}万")
        continue

    if choice == '2':
        logger.info('----提现-----')
        print()
        withdraw()
        continue

    if choice == '3':
        logger.info('----转账-----')
        transfer()
        continue
    elif choice == 'q':
        exit()