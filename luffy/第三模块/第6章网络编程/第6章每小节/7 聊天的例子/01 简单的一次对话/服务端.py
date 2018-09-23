import socket
HOST = ''
PORT = 50006
sock_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_server.bind((HOST,PORT))
sock_server.listen(1)
conn,addr = sock_server.accept()

while True:
    data =conn.recv(1024)
    if not data:break
    conn.send(data)
