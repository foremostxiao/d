# 修改个人信息程序
#
# 在一个文件里存多个人的个人信息，如以下
#
# username password  age position department
# alex     abc123    24   Engineer   IT
# rain     df2@432    25   Teacher   Teching
# ....
# 1.输入用户名密码，正确后登录系统 ，打印
#
# 1. 修改个人信息
# 2. 打印个人信息
# 3. 修改密码
# 2.每个选项写一个方法
#
# 3.登录时输错3次退出程序

user_info = {'alex':{'user_name':'alex','pass_word':'abc123','age':'24','position':'Engineer','department':'IT'},
             'rain':{'user_name':'rain','pass_word':'efg123','age':'25','position':'Teacher','department':'Teching'}
             }
# 假设每个人用户名固定不变




def modify_info():
    while True:

        choice = input(f"""
        请输入需要修改的对象：{'user_name','pass_word','age','position','department'}:
        是否退出：(按q退出)
        >""").strip()
        # choice == 'q':必须在下面复制之前，否者choice==q 赋值给后面的值发生错误
        if choice == 'q':
            with open('user_information.txt', 'w', encoding='utf-8') as f1:
                f1.write(str(dict_file))
                break
        dict_file[username][choice] = input(f"""
        请输入修改后的值：
        是否退出：(按q退出)
        >""").strip()



def display_info():

    print(f"""
    -------------个人信息----------------
        username:{dict_file[username]['user_name']}
        password:{dict_file[username]['pass_word']}
        age:{dict_file[username]['age']}
        position:{dict_file[username]['position']}
        department:{dict_file[username]['department']}
                    """)
def modify_password():
    while True:
        choice3 = input("请输入修改后的密码：(按q退出)>").strip()
        if choice3 == 'q':
            with open('user_information.txt', 'w', encoding='utf-8') as f2:
                f2.write(str(dict_file))
                break
        dict_file[username]['pass_word'] = choice3
while True:
    original_info = input(f"""
    是否录入原始值，请选择:
    (首次登陆必须选择 y )：y or n
    >""").strip()
    if original_info == 'y':
        # ---------------------首次登陆 把原始信息写入文件中----------------------------
        file_info = open('user_information.txt', 'a', encoding='utf-8')
        with open('user_information.txt', 'r+', encoding='utf-8') as f:
            f.write(str(user_info))
            break
    if original_info == 'n':
        break

exit_flag = False
count = 3
while not exit_flag :
    username = input('name:>').strip()
    password = input('password:>').strip()
    with open('user_information.txt', 'r+', encoding='utf-8') as f:
        file = f.read()
        #print(file)
        #print(type(file))
        dict_file = eval(file) # 字符串转为字典
        #print(type(dict_file))
        #print(dict_file[username])
        if username not in user_info or password != dict_file[username]['pass_word']:
            count -= 1
            print(f"输错3次退出,您还有{count}次机会输入")
            if count == 0:
                exit_flag = True
        else:

            print('welcome')
            while True:
                choice2 = input("""
                请选择下列序号：
                1 修改个人信息
                2 打印个人信息
                3 修该密码
                q 退出
                >""")
                if choice2 == '1':
                    modify_info()
                if choice2 == '2':
                    display_info()
                if choice2 == '3':
                    modify_password()
                if choice2 == 'q':
                    # exit_flag = True
                    # break
                    exit()








