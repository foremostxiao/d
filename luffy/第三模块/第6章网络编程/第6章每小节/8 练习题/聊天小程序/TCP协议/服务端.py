import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port = ('127.0.0.1',8081)
MAX_RECV_SIZE = 1024
server_socket.bind(ip_port)
server_socket.listen(5)
while True :
    conn, client_addr = server_socket.accept()
    while True:
        data = conn.recv(MAX_RECV_SIZE).decode('utf-8')
        print(data)
        msg = input('(q 退出)>>').strip()
        if not  msg:break
        if msg == 'q':
            exit()
        conn.send(msg.encode('utf-8'))