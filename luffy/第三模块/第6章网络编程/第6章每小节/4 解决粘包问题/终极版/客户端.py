import socket
import struct
import json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',9909))
while True:
    #1、发命令
    cmd=input('>>: ').strip() #ls /etc
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))

    #2、拿命令的结果，并打印

    #第一步：先收报头的长度
    obj=phone.recv(4)  #接收服务端传来的  struct.pack('i',len(header_bytes))

    header_size=struct.unpack('i',obj)[0] # 解包--得到服务端传给客户端   header_dic字典字节的长度

    #第二步：再收报头
    header_bytes=phone.recv(header_size) #   header_size为上一步已经算好的字典字节长度
    # header_bytes 为 接收客户端第二次发过来的header_dic字典转化的成的字节数据

    #第三步：从报头中解析出对真实数据的描述信息
    header_json=header_bytes.decode('utf-8') # class---> str类型
    header_dic=json.loads(header_json)   # 反序列化 服务端原先的 字典
    print(header_dic)
    total_size=header_dic['total_size'] # 服务端的执行后返回给客户端的字节流长度

    #第四步：接收真实的数据
    recv_size=0
    recv_data=b''
    while recv_size < total_size:
        res=phone.recv(1024) #1024是一个坑
        recv_data+=res
        recv_size+=len(res)

    print(recv_data.decode('gbk'))

phone.close()


