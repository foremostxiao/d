import socket
import time
import json
ip_port = ('127.0.0.1',8081)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    cmd = input('>>').strip()
    if not cmd:continue
    client.sendto(cmd.encode('utf-8'),ip_port)
    server_time,addr = client.recvfrom(1024)

    print('服务端的时间',server_time.decode('utf-8'))
