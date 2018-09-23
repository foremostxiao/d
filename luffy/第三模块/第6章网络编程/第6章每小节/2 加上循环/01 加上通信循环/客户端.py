import socket

# 1 买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#(sock_stream 流)

# 2 拨号，127.0.0.1是回送地址，指本地机，一般用来测试使用。客户端、服务端在一台主机上
phone.connect(('127.0.0.1',8081))# 端口 0-65535：0-1024给操作系统使用

# 3 发、收 消息
while True:
    msg = input('>>').strip()
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data)
# 4 关闭
phone.close()