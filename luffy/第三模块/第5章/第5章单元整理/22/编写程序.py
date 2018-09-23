import pickle,json,time
# 用json写入文件
# dict = {'egon':{'password':'123','status':'False','timeout':0},
#         'alex':{'password':'456','status':'False','timeout':0}
#         }
# with open('account','a+',encoding='utf-8') as f:
#     json.dump(dict,f)

class People:
    def __init__(self):
        # self.name = name
        # self.password = password
        # self.status = status
        # self.timeout = timeout
        pass
    @property   #特性
    def db(self):
        with open('account', 'r+', encoding='utf-8') as f:
             return json.load(f)

    def exit(self):
        choice = input('''
选择 1 退出登录     
选择 其它 继续
>''')
        if choice == '1':
            if dict[name]['status'] == True:
                dict[name]['status'] = False
                exit()
            else:
                exit()

        else:
            pass

    def start_time(self):
        dict[name]['timeout'] = time.time()
        with open('account','w+',encoding='utf-8') as f:
            json.dump(dict,f)
    def rewrite_time(self):
        dict[name]['timeout'] = 0
        with open('account', 'w+', encoding='utf-8') as f:
            json.dump(dict, f)


if __name__ == '__main__':
    obj = People()
    dict = obj.db
    count = 3
    while count > 0:
        name = input('name:').strip()
        password = input('password：').strip()
        if name in dict:
            if password == dict[name]['password']:
                if dict[name]['timeout']!=0: #这一步很关键
                    if time.time() - dict[name]['timeout'] <= 10:
                        print('-----welcome-----')
                        dict[name]['status'] = True
                        obj.rewrite_time()
                        obj.exit()
                        break
                    else:
                        print('锁定时间超过10秒，不允许用户再次登录，请联系管理员')
                        break
                else:
                    print('-----welcome-----')
                    dict[name]['status'] = True
                    obj.exit()
                    break
            else:
                count -= 1
                if count == 0:
                    print('----密码输错三次账户锁定-----')
                    obj.start_time()
                    obj.exit()
                    break
                else:
                    print(f'-----密码输入错误，您还有{count}次机会------')
                    obj.exit()
                    continue
        else:
            print('----您输入的用户不存在------')

