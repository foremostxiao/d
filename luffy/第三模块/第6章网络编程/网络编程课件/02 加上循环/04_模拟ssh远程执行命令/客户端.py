import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',9901))

while True:
    #1、发命令
    cmd=input('>>: ').strip() #ls /etc
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    #2、拿命令的结果，并打印
    data=phone.recv(1024)
    print(data.decode('gbk'))

phone.close()


