import socket
import subprocess
import struct
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#如果在服务端关闭情况下 出现 8080端口被占用，是因为原先的端口系统还没有回收
phone.bind(('127.0.0.1',8080))
phone.listen(5)

print('---starting----')
# 没有实现并发，单实现了打开服务端，执行多个客户端，不能同时接受多个客户端单消息，只能一个个接受，比如，执行客户端1发送消息了，关闭1，然后执行客户端2，发送消息给服务端
while True:#链接循环
    conn,client_addr = phone.accept()
    print(client_addr)

    while True:
        try:
            # 1 收命令
            cmd = conn.recv(8096)
            if not cmd:break
            # 2 执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)#正确的给管道stdout，错误的给stderr
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3 执行命令，拿到结果，把命令的结果返回给客户端
            # 第一步： 制作固定长度的报头（固定长度）发生给客户端
            total_size = len(stdout) + len(stderr)
            header = struct.pack('i',total_size) # 打包

            # 第二步，把报头发送给客户端
            conn.send(header)
            # 优化如下：
            # 第三步：再发送真实第数据
            conn.send(stdout) # 时间短，数据小会产生粘包一起发送
            conn.send(stderr)

        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()
phone.close()