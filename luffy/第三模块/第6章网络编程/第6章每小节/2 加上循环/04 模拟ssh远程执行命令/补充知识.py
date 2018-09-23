# 命令
# --------window-------
# dir ：查看某一个文件下的子文件名
# ipconfig  查看本地网卡的ip信息
# tasklist 查看运行的进程

#-------linux-------
# ls
# ifconfig
# ps aux

# 如何在系统上执行系统命令,并拿到命令的结果
# import os
# os.system('dir')
#
# res = os.system('dir')
# print(res) #输出0

# 运行管道的概念
# import subprocess
# obj = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)#正确的给管道stdout，错误的给stderr
# print(obj)
# print('stdout 1--->',obj.stdout.read())
# print('stdout 2--->',obj.stdout.read().decode('gbk')) # 管道只能取一次第二次不能

#-------
import subprocess
# 文件的错误的情况下，传值给错误的管道
obj = subprocess.Popen('xxxxdir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)#正确的给管道stdout，错误的给stderr
print(obj)
print('stdout 1--->',obj.stdout.read()) #正确管道没有值
print('stdout 2--->',obj.stdout.read().decode('gbk')) # 管道只能取一次第二次不能
print('stdout 1--->',obj.stderr.read()) # 错误管道有值