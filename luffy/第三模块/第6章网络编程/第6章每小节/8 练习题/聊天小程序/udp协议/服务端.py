import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8081)
server_socket.bind(ip_port)


while True:
    data, addr_client = server_socket.recvfrom(1024)
    print(data.decode('utf-8'))

    msg = input('>>').strip()
    if not msg:break
    server_socket.sendto(msg.encode('utf-8'),addr_client)
