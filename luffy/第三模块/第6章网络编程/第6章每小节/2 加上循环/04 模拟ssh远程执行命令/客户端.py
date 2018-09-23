import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
while True:
    # 1 发命令
    cmd = input('>>>').strip()# 输入mingl
    if not cmd:continue
    phone.send(cmd.encode('utf-8')) # send 发给操作系统了
    # 2 拿命令的结果并打印
    data = phone.recv(1024) # 1024是个坑，有可能收到的超过1024，后续解决
    print(data.decode('gbk'))
phone.close()