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
2. 转账
""")
while True:

    choice = input("""
请选择如下序号：
1. 账户信息
2. 转账
q.退出
>
""")
    #  此题前提在luffy 下存入100万
    with open(file_path1, 'r', encoding='utf-8') as f:
        balance = json.load(f)
    if choice == '1':
            print(f'当前余额：{balance}万')
            continue
    if choice == '2':
        balance = balance - balance*0.05 - 75
        tesla_balance = 75
        print(f"购买tesla共花费{balance - balance*0.05 - 75},tesla账户增加{tesla_balance}")
        with open(file_path2,'w',encoding='utf-8') as f2:
           json.dump(tesla_balance,f2)
        with open(file_path1, 'w', encoding='utf-8') as f3:
           json.dump(balance, f3)
           continue

    elif choice == 'q':
        exit()
