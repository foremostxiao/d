import socket
import time
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9903))



client.send('hello'.encode('utf-8'))

time.sleep(5)#如果间隔较长,

# 数据量少，时间间隔小，就会发生粘包

client.send('world'.encode('utf-8'))