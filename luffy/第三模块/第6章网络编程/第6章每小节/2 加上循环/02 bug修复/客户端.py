import socket

# 变量名可以不同，只要socket.socket(socket.AF_INET,socket.SOCK_STREAM)，connect(('127.0.0.1',8080))
phone1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone1.connect(('127.0.0.1',8080))
while True:
    msg = input('>>>').strip()
    if not msg:continue
    phone1.send(msg.encode('utf-8')) # send 发给操作系统了


    data = phone1.recv(1024)
    print(data.decode('utf-8'))
phone1.close()