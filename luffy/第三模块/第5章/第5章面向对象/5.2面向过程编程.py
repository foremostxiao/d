import json
# 新用户注册
def interactive():
    name = input('>>').strip()
    password = input('>>').strip()
    return {
        'name':name,
        'password':password
    }
def check(user_data):
   is_valid = True
   if len(user_data['name']) == 0:
       print('用户名不能为空')
       is_valid = False
   if len(user_data['password']) < 6:
       print('密码不能小于6位')
       is_valid = False
   return {'is_valid':is_valid,
           'user_data':user_data
           }

def register(check_info):
    if check_info['is_valid']:
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(check_info['user_data'],f)
def main():
    user_data = interactive()
    check_info = check(user_data)
    register(check_info)
if __name__ == '__main__':#快捷键输入 直接输入 main 会出现提示
    main()
