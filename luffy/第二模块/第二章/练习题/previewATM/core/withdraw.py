import json,os,sys

#取出当前文件的父目录，
print(__file__)
dir = os.path.abspath(__file__)
dir2 = os.path.dirname(os.path.dirname(dir))
# 取出json文件的绝对路径
file_path1 = dir2 + "\\" + "account" + "\\" + "luffy.json"
file_path2 = dir2 + "\\" + "account" + "\\" + "tesla.json"
print("""
------- Luffy Bank ---------
1. 账户信息
2. 提现
""")
data = {'balance': 100, 'credit': 50}
with open(file_path1, 'w', encoding='utf-8') as f:
    json.dump(data,f)
while True:

    choice = input("""
请选择如下序号：
1. 账户信息
2. 提现
q.退出
>
""")
    #  此题前提在luffy 下存入data字典信息
    #data = {'balance': 100, 'credit': 50}
    with open(file_path1, 'r', encoding='utf-8') as f:
        #json.dump(data,f)
        balance = json.load(f)
    if choice == '1':

        print(f"当前余额：{balance['balance']}万，信用额度：{balance['credit']}万")
        continue
    if choice == '2':
        withdraw_money = int(input('请输入提现金额：').strip())
        if withdraw_money > balance['credit']:
            print(f"提现金额超过信用额度：{balance['credit']}万，请重新输入")
        else:
            balance['balance'] = balance['balance'] - withdraw_money - withdraw_money*0.05
            print(f"剩下余额{ balance['balance']}")
        with open(file_path1, 'w', encoding='utf-8') as f2:
           json.dump(balance, f2)
           continue

    elif choice == 'q':
        exit()
