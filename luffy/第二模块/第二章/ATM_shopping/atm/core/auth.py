import json,datetime,time

import os
import sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
#找到路径
sys.path.append(BASE_DIR)

from conf import settings

def userjudge(data,user_entrance,account):
    count = 3
    while count > 0:
        password = input("Password:").strip()
        time_now = time.strftime('%Y-%m-%d')
        d1 = datetime.datetime.strptime(data['expire_date'], '%Y-%m-%d')
        d2 = datetime.datetime.strptime(time_now, '%Y-%m-%d')
        if d1 > d2:
            if password == data['password']:
                print('----登录成功-----')
                user_entrance["user_status"] = True  # 可以让认证后的用户，在user_entrance中体现出来
                user_entrance['data'] = data  # 将用户文件，添加到'data'当中
                break
            else:
                count -= 1
                print(f"密码错误，您还有{count}次机会输入")
                if count == 0:
                    data['status'] = 2
                    print(f"用户：{count}已锁定")
                    path = os.path.join(settings.account_path, f"{account}.json")
                    with open(path, 'w', encoding='utf-8') as f:
                        json.dump(data, f)
                        exit()
        else:
            print(f"用户：{account}已过期")
            exit()


