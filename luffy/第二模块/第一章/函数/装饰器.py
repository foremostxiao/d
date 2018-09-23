# 1 装饰器的简单应用
# exit_flag = False
# def login(fun):
#     def inner():
#         user_info = {'alex':'abc'}
#         global exit_flag
#
#         if exit_flag == False:
#             username = input('username:>').strip()
#             password = input('password:>').strip()
#             if username in user_info and password == user_info[username]:
#                 print('welcome login...')
#                 exit_flag = True
#
#             else:
#                 print('username or password is wrong')
#         if exit_flag == True:
#             fun()
#     return inner
#
#
# @login
# def america():
#     print('welcome to the america')
# @login
# def japan():
#     print('welcome to the japan')
# @login
# def china():
#     print('welcome to the china')
#
# america()
# japan()
# china()

# 2 加多层需求认证  带一次参数
#
# exit_flag = False
# def login(fun):
#     def inner(*args,**kwargs):  # 必须和 实参带参数保持一致   america('kfc')
#         user_info = {'alex':'abc'}
#         global exit_flag
#
#         if exit_flag == False:
#             username = input('username:>').strip()
#             password = input('password:>').strip()
#             if username in user_info and password == user_info[username]:
#                 print('welcome login...')
#                 exit_flag = True
#
#             else:
#                 print('username or password is wrong')
#         if exit_flag == True:
#             fun(*args,**kwargs) # 这里要加非固定参数
#     return inner
#
#
# @login
# def america(s):
#     print('welcome to the america')
# @login
# def japan(s):
#     print('welcome to the japan')
# @login
# def china(s):
#     print('welcome to the china')
#
# america('kfc') #带参数
# japan('daoguo')
# china('beautiful')



# 在上一个的基础之上加一个，qq验证的功能  ,相对应的多加一层 函数
exit_flag = False
def login(f):
    def outer(fun):
        def inner(*args):  # 必须和 实参带参数保持一致   america('kfc')

            if f == 'qq':
                user_info = {'alex':'abc'}
                global exit_flag
                if exit_flag == False:
                    username = input('username:>').strip()
                    password = input('password:>').strip()
                    if username in user_info and password == user_info[username]:
                        print('welcome login...')
                        exit_flag = True

                    else:
                        print('username or password is wrong')
                if exit_flag == True:
                    fun(*args)
        return inner
    return outer
@login('qq')
def america(*args):
    print('welcome to the america')
@login('qq')
def japan(*args):
    print('welcome to the japan')
@login('qq')
def china(*args):
    print('welcome to the china')
america('kfc') #带参数
japan('daoguo')
china('beautiful')


# 两个参数
# def w1(func):
#     print('---正在装饰--')
#     def inner():
#         print('---正在验证权限1--')
#         func()
#     return inner
#
#
# def w2(func):
#     print('---正在装饰2--')
#     def inner():
#         print('---正在验证权限2--')
#         func()
#     return inner
#
# # 只要python解释器执行到了这个代码,那么就会自动的进行装饰,而不是等到调用的时候才装饰的
# @w2
# @w1
# def f1():
#     print('---f1')
#
# f1()