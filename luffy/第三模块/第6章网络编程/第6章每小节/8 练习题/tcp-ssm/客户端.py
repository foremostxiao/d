import socket
import struct
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',8080)
client_socket.connect(ip_port)
while True:
    cmd = input('>>').strip()
    if not cmd:continue
    client_socket.send(cmd.encode('utf-8'))
    head = client_socket.recv(4)
    head_len = struct.unpack('i',head)[0]# 解包返回元祖（a,）
    recv_size = 0
    total_data = b''
    while recv_size < head_len:
        recv_data = client_socket.recv(1024)
        recv_size += len(recv_data)
        total_data += recv_data
    print("返回的消息：%s" % total_data.decode('gbk'))

