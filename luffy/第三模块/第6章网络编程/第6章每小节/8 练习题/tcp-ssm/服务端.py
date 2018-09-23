import socket
import struct
import subprocess
# subprocess模块来实现对系统命令或脚本的控制
ip_port = ('127.0.0.1',8080)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(ip_port)
server_socket.listen(5)
while True:
    conn,addr = server_socket.accept()
    while True:
        client_data = conn.recv(1024).decode('utf-8')
        res = subprocess.Popen(client_data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # stdin标准输入；stdout输出，stderr错误句柄
        stdout = res.stdout.read()
        stderr = res.stderr.read()

        # print('stdout', stdout, type(stdout))  # b'' <class 'bytes'> 二进制模式
        # print('stderr', stderr, type(stderr))  #  b'' <class 'bytes'> 二进制模式

        # stdin = res.stdin.read()
        # 先发报头 ---- struct
        header = struct.pack('i',len(stdout+stderr))
        conn.send(header)
        conn.send(stdout)
        conn.send(stderr)
    conn.close()






