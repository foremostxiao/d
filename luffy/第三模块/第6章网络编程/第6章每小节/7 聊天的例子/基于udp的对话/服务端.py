import socket
ip_socket =('127.0.0.1',9000)
BUFSIZE = 1024
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind((ip_socket))

while True:
    msg,addr = udp_server.recvfrom(BUFSIZE)
    print(msg.decode('utf-8'),addr)
    response = input('>>').strip()
    udp_server.sendto(response.encode('utf-8'),addr)

udp_server.close()
