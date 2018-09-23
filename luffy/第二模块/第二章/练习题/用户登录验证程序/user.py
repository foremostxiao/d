import json,time,datetime
username = 'user.json'
#首次登入将数据写入文件
# data = {"expire_date": "2020-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# with open('user.json','r+',encoding='utf-8') as f:
#     file = json.dump(data,f)
with open('user.json', 'r+', encoding='utf-8') as f2:
    file2 = json.load(f2)

print('请登录用户名、密码进行验证：')

count = 3
while count > 0:
    user_name = input('name:>').strip()
    pass_word = input('password:>').strip()
    if file2['status'] == 1:
        print('该用户已锁定')
        exit()
    else:
        time_now = time.strftime('%Y-%m-%d')
        d1 = datetime.datetime.strptime(file2['expire_date'], '%Y-%m-%d')
        d2 = datetime.datetime.strptime(time_now, '%Y-%m-%d')
        if d1 > d2:
            if user_name == username:
                if pass_word == file2['password']:
                    print('登录成功')
                    exit()
                else:
                    count -= 1
                    print(f"您还有{count}次机会输入")
                    if count == 0:
                        file2['status'] = 1
                        with open('user.json', 'w', encoding='utf-8') as f3:
                            json.dump(file2,f3)
                            break

            else:
                print('用户名不存在：')
                continue

        else:
            print('已过期')
            break