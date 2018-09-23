import socket

# 1 买手机
# phone 为套接字对象
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#(sock_stream 流)
# 2 绑定手机卡，127.0.0.1是回送地址，指本地机，一般用来测试使用。客户端、服务端在一台主机上
phone.bind(('127.0.0.1',8081))# 端口 0-65535：0-1024给操作系统使用

# 3 开机
phone.listen(5)# 5 代表最多挂机数

# 4 等电话连接 # 在同一个IDE上执行客户端、服务端，，先执行服务端后，在执行客户端
# 直接执行客户端会发生错误
print('------starting-------')
conn,client_addr = phone.accept() # accept（）对于 connect（）做的3次握手
# print('==========>')
# print(res)

# 5 收、发消息
data = conn.recv(1024) # 1024个字节 代表接受数据最大数，，单位bytes字节
print('客户端数据',data)

conn.send(data.upper()) # 服务端回数据给客户端
# 6 挂电话
conn.close()

# 7 关机
phone.close()