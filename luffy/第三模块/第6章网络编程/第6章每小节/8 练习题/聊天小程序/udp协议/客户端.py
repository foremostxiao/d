import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8081)

while True:
    msg = input('>>').strip()
    if not  msg:continue
    client.sendto(msg.encode('utf-8'),ip_port)
    data, addr_server = client.recvfrom(1024)
    print(data.decode('gbk'))