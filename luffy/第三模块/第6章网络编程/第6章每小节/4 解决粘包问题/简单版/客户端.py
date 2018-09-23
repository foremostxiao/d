import socket
import struct
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))
while True:
    # 1 发命令
    cmd = input('>>>').strip()# 输入mingl
    if not cmd:continue
    phone.send(cmd.encode('utf-8')) # send 发给操作系统了
    # 2 拿命令的结果并打印
    # 第一步：先拿到固定长度的报头
    header = phone.recv(4)
    total_size =struct.unpack('i',header )[0]
    # 第二步：从报头中解析出对真实数据对描述信息（数据信息）  接收真实第数据

    # 第三步：接收真实第数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024) # 1024是个坑，有可能收到的超过1024，后续解决
        recv_data += res
        recv_size += len(res)
    # 一次收不完，分多次
    # 命名
    print(recv_data.decode('gbk'))
phone.close()