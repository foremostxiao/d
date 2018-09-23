# 1. 编写带参数装饰器auth，
# 装饰器参数engine='file'时，模拟用户名username='luffy',密码password='city'认证
# 装饰器参数engine='mysql'时，模拟用户名username='alex',密码password='3714'认证
# 错误达到三次时退出程序
data = {'file':{'username':'luffy','password':'city'},'mysal':{'username':'alex','password':'3714'}}
user_status = False
def auth(engine):
    def auth_type(func):
        if engine == 'file':
            username = 'luffy'
            password = 'city'
        if engine == 'mysql':
            username = 'alex'
            password = '123'
        def inner():
            global user_status
            if user_status == False:
                count = 3

                while count > 0:
                    user_name = input('name>').strip()
                    pass_word = input('password>').strip()
                    if user_name == username and pass_word == password:
                        print('welcome')
                        user_status = True
                        break
                    else:
                        count -= 1
                        if count == 0:
                            print('输错三次')
                            exit()
                        else:
                            print(f"您还有{count}次机会输入")
                            continue
            if user_status == True:
                func()
        return inner
    return auth_type
@auth('file')
def america():
    print('123')
@auth('mysql')
def japan():
    print('456')
america()
japan()

# 解释一下“w”和“wb”的区别（“r”和“rb”，“a”和“ab”） (口述)
# （1）“w”和“wb”  json 本质是一种文件组织方式，比如txt,csv,word
#  w 打开一个文件只写，并覆盖掉原内容，没有文件就创建
#  wb 二进制格式打开一个文件只写，并覆盖掉原内容，没有文件就创建
# （2）“r”和“rb” ：r只读方式打开文件指针在开头/rb 以二进制的格式打开一个文件只读
#  (3) “a”和“ab” : a 打开一个文件用于追加， 不存在文件就创建；ab以二进制的格式打开一个文件用于追加，不存在文件就创建
#3. 描述写硬盘的编码转变（UTF-8格式，系统格式GBK） (口述)
#系统文件先解码decode('utf-8')为Unicode，再编码encode为GBK的格式
