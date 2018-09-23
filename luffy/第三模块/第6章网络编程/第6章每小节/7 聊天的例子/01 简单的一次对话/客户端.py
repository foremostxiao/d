import socket
HOST = 'localhost'
PORT = 50006
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
client.sendall(b'hello,python')
data = client.recv(1024)
print('Received',data)