import socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#如果在服务端关闭情况下 出现 8080端口被占用，是因为原先的端口系统还没有回收
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8080))
phone.listen(5)

print('---starting----')
# 没有实现并发，但实现了打开服务端，服务端只能同时服务一个客户端，不能同时接受多个客户端单消息
# ，比如，执行客户端1发送消息了，关闭1，然后执行客户端2，发送消息给服务端
while True:#链接循环
    conn,client_addr = phone.accept()
    print(client_addr)
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