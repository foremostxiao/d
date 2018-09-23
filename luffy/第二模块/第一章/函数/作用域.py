

age = 18
def func1():
    age =73
    def fun2():
        print(age)
    return  fun2
val = func1()  # val = fun2
val()  # val() == fun2()
