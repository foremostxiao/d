# 同时解决粘包问题
import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',8081)
MAX_RECV_SIZE = 1024
client_socket.connect(ip_port)
while True:
    msg = input('(q 退出)>>').strip()
    if not msg:continue
    if msg == 'q':
        exit()
    client_socket.send(msg.encode('utf-8'))
    data = client_socket.recv(MAX_RECV_SIZE)
    print(data.decode('utf-8'))
