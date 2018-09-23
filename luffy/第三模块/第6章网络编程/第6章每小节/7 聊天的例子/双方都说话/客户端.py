import socket
HOST = 'localhost'
PORT = 50000
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
while True:
    cmd = input('>>').strip()
    if not cmd:break
    client.send(cmd.encode('utf-8'))

    data = client.recv(1024)
    print('Received',data.decode('utf-8'))