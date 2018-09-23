import os,sys,json
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#找到路径
sys.path.append(BASE_DIR)
from atm.core import user_and_manager_main
from conf import settings

def to_auth():
    print('''\033[32;0m
------欢迎进入购物商城，请验证------
规定购物商城用户名必须有数字组成
帐号：123 密码：123
帐号：456 密码：456 >\033[0m''')
    # 购物商城账户认证
    user_and_manager_main.shopping_auth()


def shopping_center(account):
    shopping_car = []
    while True:
        print('-----------商品列表--------------')
        path = os.path.join(settings.account_path,"shopping_goods.json")
        data = json.load(open(path,'r',encoding='utf-8'))
        for index, good in enumerate(data):
            print((index, good["name"], good["price"]))
        choice = input('''
请选择上面的商品编号（或者a,q）
a 调用信用卡支付，
q 退出购物中心：>''''').strip()

        if choice.isdigit():
            choice = int(choice)
            if choice in range(0, len(data)):
                shopping_car.append(data[choice])
                print(f"当前购物车记录{shopping_car}")
                #日志                 #每个账户单独一个购物车
        elif choice == 'a':
            print(f"                \033[32;0m当前购物商城用户名为---------{account}------\033[0m")
            print('-----共选购如下商品------')
            price = 0
            for index, good in enumerate(shopping_car):
                print((index, good["name"], good["price"]))
                price = price +good["price"]
            print(f"所选商品总金额为{price}")
            path = os.path.join(settings.account_path,f"{account}_shop_car.json")
            json.dump(shopping_car,open(path,'w',encoding='utf-8'))
            print('''
请输入信用卡帐号密码用于支付
帐号：user 密码：abc
帐号：user2 密码：abc
帐号：user3 密码：abc''')
            user_and_manager_main.online()
            break
        elif choice == 'q':
            break
        else:
            print('----输入错误----')

#------------------------购物记录--------------------------------------

