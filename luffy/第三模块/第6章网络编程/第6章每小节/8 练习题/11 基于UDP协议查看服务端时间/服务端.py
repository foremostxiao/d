# UDP协议的两个主要方法sendto和recvfrom详解
# TypeError: sendto() takes 2 or 3 arguments (1 given)
import socket
import os,json,time
ip_port = ('127.0.0.1',8081)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ip_port)
# udp 不需要 监听listen ,不需要接收 accept
while True:
    msg,addr= server.recvfrom(1024)
    if msg.decode('utf-8') == 'time':
        server_time = time.strftime("%Y-%m-%d %X",time.localtime())
        server.sendto(server_time.encode('utf-8'),addr)
        # print(server_time)
server.close()