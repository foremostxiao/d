import socket
ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024
udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    MSG = input('>>').strip()
    udp_client.sendto(MSG.encode('utf-8'),ip_port)
    back_msg,addr = udp_client.recvfrom(BUFSIZE)
    print(back_msg.decode('utf-8'))
udp_client.close()