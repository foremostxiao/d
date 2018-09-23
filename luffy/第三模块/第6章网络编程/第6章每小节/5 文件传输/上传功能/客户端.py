import socket
import struct
import json
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from db import settings

def run():
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    phone.connect(('127.0.0.1',9900))
    while True:
        # 1、发命令
        cmd = input('>>: ').strip()  # get 3.jpeg
        if not cmd: continue
        cmds = cmd.split()
        filename = cmds[1]
        try:
            header_dic = {
                'filename': filename,
                'md5': 'xxdxxx',
                'file_size': os.path.getsize(os.path.join(settings.path_client, filename))
            }

            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')
            phone.send(struct.pack('i', len(header_bytes)))  # len(header_bytes)发送信息给客户端的字节长度
            phone.send(header_bytes)  # 客户端发两次
            with open(os.path.join(settings.path_client, filename), 'rb') as f:
                for line in f:
                    phone.send(line)
        except ConnectionResetError:  # 适用于windows操作系统
            break
    phone.close()


if __name__ == '__main__':
    run()