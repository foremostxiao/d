# 练习一：在元类中控制把自定义类的数据属性都变成大写
# class Mymetaclass(type):
#     def __new__(cls, name,bases,attrs):
#         update_attrs = {}
#         for k,v in attrs.items():
#             if not callable(v) and not k.startswith('__'):
#                 update_attrs[k.upper()] = v
#             else:
#                 update_attrs[k] = v
#         return type.__new__(cls,name,bases,update_attrs)
#
# class Chinese(metaclass=Mymetaclass):
#     country = 'China'
#     tag = 'Legend of the Dragon'
#     def walk(self):
#         print(f"{self.name} is walking")
#
# print(Chinese.__dict__)

#----------------------------------------------------------
# class Demo(object):
#     def __init__(self):
#         print('__init__() called...')
#
#     def __new__(cls, *args, **kwargs):
#         print('__new__() - {cls}'.format(cls=cls))
#         return object.__new__(cls, *args, **kwargs)
#
# if __name__ == '__main__':
#     de = Demo()

#---------------------------练习二：在元类中控制自定义的类无需init方法-----------------------------------
class Mymetaclass(type):
    # def __new__(cls,name,bases,attrs):
    #     update_attrs={}
    #     for k,v in attrs.items():
    #         if not callable(v) and not k.startswith('__'):
    #             update_attrs[k.upper()]=v
    #         else:
    #             update_attrs[k]=v
    #     return type.__new__(cls,name,bases,update_attrs)

    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('must use keyword argument for key function')
        obj = object.__new__(self) #创建对象，self为类Foo

        for k,v in kwargs.items():
            obj.__dict__[k.upper()]=v
        return obj

class Chinese(metaclass=Mymetaclass):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)


p=Chinese(name='egon',age=18,sex='male')
print(p.__dict__)