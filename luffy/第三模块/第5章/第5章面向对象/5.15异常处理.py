# s1 = 'hello'
# try:
#     int(s1)
# # except IndexError as e:
# #     print(e)
# # except KeyError as e:
# #     print(e)
# # 在不知道异常类型的情况下：写Exception
# except Exception as e:
#     print(e)
# finally:
#     print('无论异常与否，都会执行该模块，通常是进行清理工作')
#


# # 主动出发异常
# print('-------------------------------')
# try:
#     raise TypeError('类型错误')
# except Exception as e:
#     print(e)
# print('------------------------------')


# 自定义异常
# class EgonException(BaseException):
# #     def __init__(self,msg):
# #         self.msg = msg
# #     def __str__(self):
# #         return  self.msg
# # try:
# #     raise EgonException('错误类型')
# # except Exception as e:
# #     print(e)
