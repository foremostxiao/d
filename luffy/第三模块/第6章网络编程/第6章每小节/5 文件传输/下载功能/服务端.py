import socket
import subprocess
import struct
import json

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from db import settings


phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',9909)) # 0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=phone.accept()
    print(client_addr)

    while True: #通信循环
        try:
            #1、收命令
            res=conn.recv(8096) # b'get 3.jpeg'
            if not res:break #适用于linux操作系统

            #2、解析命令，提取相应的命令参数
            cmds = res.decode('utf-8').split()
            filename = cmds[1]

            #3、以读取方式打开文件，读取文件内容 发给客户端

            #第一步：制作固定长度的报头
            header_dic={
                'filename':filename,
                'md5':'xxdxxx',
                'file_size': os.path.getsize(os.path.join(settings.path_server,filename))
            }

            header_json=json.dumps(header_dic)

            header_bytes=header_json.encode('utf-8')

            #第二步：先发送报头的长度
            conn.send(struct.pack('i',len(header_bytes))) # len(header_bytes)发送信息给客户端的字节长度

            #第三步：再发报头
            conn.send(header_bytes)  # 客户端发两次
            with open(os.path.join(settings.path_server,filename),'rb') as f:
                for line in f:
                    conn.send(line)


            #第四步：再发送真实的数据

        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()

phone.close()


