# 原先的-----------面向过程程序设计---------------------
import os

# def data_backup(folder):
#     print(f"找到要备份的目录...{folder}",)
#     print("将备份文件打包，...")
#     zip_file = '/tmp/backup20181103.zip'
#     print(f"备份成功，文件为{zip_file}")
#     return zip_file
#
#
# def cloud_upload(file):
#     print("\nconnecting cloud storage center...")
#     print("cloud storage connected.")
#     print(f"upload file...xxx..to cloud...{folder}", )
#     link = '//http://www.xxx.com/bak/%s'%os.path.basename(file)
#     print('close connection.....')
#     return link
#
#
#
# def data_backup_test(link):
#    print(f'\n下载文件{link}')
#
# def main():
#     # 步骤一：本地数据打包
#     zip_file = data_backup("c:\\users\\alex\欧美100G高清无码")
#     # 步骤二：上传至云服务器
#     link = cloud_upload(zip_file)
#     # 步骤三：测试备份文件的可用性
#     data_backup_test(link)
# if __name__ == '__main__':
#     main()
#
# # 要修改的话------面向过程程序设计---------------
# import os
#
# def data_backup(folder):
#     print(f"找到要备份的目录...{folder}",)
#     print("将备份文件打包，...")
#     zip_file = '/tmp/backup20181103.zip'
#     print(f"备份成功，文件为{zip_file}")
#     return zip_file
# def cloud_upload(file):#加上异常处理，在出现异常的情况下，没有link返回
#     try:
#         print("\nconnecting cloud storage center...")
#         print("cloud storage connected.")
#         print(f"upload file...xxx..to cloud...{folder}", )
#         link = 'http://www.xxx.com/bak/%s' %os.path.basename(file)
#         print('close connection.....')
#         return link
#     except Exception:
#         print('upload error')
#     finally:
#         print('close connection.....')
# def data_backup_test(link):#加上对参数link的判断
#     if link:
#         print(f'\n下载文件{link}')
#     else:
#         print('\n链接不存在')
#
# def main():
#     # 步骤一：本地数据打包
#     zip_file = data_backup("c:\\users\\alex\欧美100G高清无码")
#     # 步骤二：上传至云服务器
#     link = cloud_upload(zip_file)
#     # 步骤三：测试备份文件的可用性
#     data_backup_test(link)
# if __name__ == '__main__':
#     main()

# 先定义类后产生对象
class OldboyStudent:
    school='oldboy'
    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')
# 后产生对象
stu1 = OldboyStudent()
stu2 = OldboyStudent()
stu3 = OldboyStudent()
print(stu1)
print(stu2)
print(stu3)
print(OldboyStudent.school) #查
OldboyStudent.school='Oldboy2' #改
print(OldboyStudent.school)
OldboyStudent.x=1 #增
print(OldboyStudent.x)
del OldboyStudent.x #删
print(OldboyStudent.x)


# 类的使用
# class OldboyStudent:
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#
# s1=OldboyStudent('李坦克','男',18) #先调用类产生空对象s1，然后调用OldboyStudent.__init__(s1,'李坦克','男',18)
# s2=OldboyStudent('王大炮','女',38)
# s3=OldboyStudent('牛榴弹','男',78)
# print(s1)
# print(s2)
# print(s3)



# 对象的使用
# class OldboyStudent:
#     school = 'oldboy'
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age = age
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
#
#     def sleep(self):
#         print('is sleeping')
#
# s1=OldboyStudent('李坦克','男',18) #先调用类产生空对象s1，然后调用OldboyStudent.__init__(s1,'李坦克','男',18)
# s2=OldboyStudent('王大炮','女',38)
# s3=OldboyStudent('牛榴弹','男',78)
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)
#
# # 查
# print(s2.name)
# print(s2.__dict__['name'])