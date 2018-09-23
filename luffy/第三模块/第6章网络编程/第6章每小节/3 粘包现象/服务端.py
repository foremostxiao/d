import socket
import subprocess
import time
# 粘包现象 多个包粘到一起 TCP ，在管道里面流 应该怎么解决：
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9903))
server.listen(5)

print('-------start--------')
conn,client_addr = server.accept()


res1 = conn.recv(1)
print('第一次',res1)
time.sleep(6)
# 数据量少，时间间隔小，就会发生粘包,6s 很长不会发生粘包
res2 = conn.recv(1024)
print('第2次',res2) #第2次 b'elloworld'

# 客户端、服务端都可能发生粘包
