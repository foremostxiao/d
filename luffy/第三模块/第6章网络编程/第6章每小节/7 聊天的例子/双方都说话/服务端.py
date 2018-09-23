import socket
HOST = ''
PORT = 50000
sock_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_server.bind((HOST,PORT))
sock_server.listen(1)


while True:
    conn, addr = sock_server.accept()
    while True:
        data =conn.recv(1024)
        print(f"收到客户端的的数据：>{data.decode('utf-8')}")
        if not data:break
        response = input('回复客户端>>').strip()
        conn.send(response.encode('utf-8'))

