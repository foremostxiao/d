import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#如果在服务端关闭情况下 出现 8080端口被占用，是因为原先的端口系统还没有回收
phone.bind(('127.0.0.1',8080))
phone.listen(5)

print('---starting----')
conn,client_addr = phone.accept()
print(client_addr)
print(conn)

while True:
    try:
        data = conn.recv(1024)
        if not data:break
        print('客户端的数据',data)
        conn.send(data.upper())
    except ConnectionResetError: #适用于windows操作系统
        break
conn.close()
phone.close()