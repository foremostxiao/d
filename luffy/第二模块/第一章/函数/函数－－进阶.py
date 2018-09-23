
# 名称空间
#
level = 'L0'
n = 22
def func():
    level = 'L1'
    n = 33
    print(locals())

    def outer():
        n = 44
        level = 'L2'
        print(locals(),n)

        def inner():
            level = 'L3'
            print(locals(),n) # 此处打印的n是多少 ？
        inner()
    outer()

func()

# 闭包

# def  outer():
#     name = 'alex'
#     def inner():
#         print("在inner里打印外层函数的变量",name)
#     return  inner
# f = outer()
# f()