import socket,os,sys
import struct,pickle
import subprocess
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
class ftp_server:
    ip_port = ('127.0.0.1',8080)
    RECV_MAX = 1024
    LISTEN_MAX = 5
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind(self.ip_port)
        self.server_socket.listen(self.LISTEN_MAX)
    def get(self,conn):
        """
        1 判断文件在服务器是否存在

                1.1存在下载,解决粘包问题
                    1.1.1.得到文件大小（字节为单位）file_size,发送报头给客户端
                1.2不存在 报错
        """

        file_path = os.path.join(BASE_DIR,'db',self.msg[1])
        if os.path.exists(file_path):
            header_dic = {
                'filename': 111,
                'file_md5': 111,
                'file_size': os.path.getsize(file_path)
            }
            header_bytes = pickle.dumps(header_dic)
            # 文件的大小以字节为单位

            head_size_len = struct.pack('i',len(header_bytes)) # 打 包成 四个字节
            conn.send(head_size_len)
            conn.send(header_bytes)
            self.handle_file(file_path,conn,1)
        else:
            print('文件不存在')
            head_size = struct.pack('i', 0)  # 打 包成 四个字节
            conn.send(head_size)


    def put(self,conn):
        """
        0.判断根据文件名判断，服务端是否已存在该文件
        1.存在----返回 0
        2.不存在---返回 1
            2.1.解压 报头 head


        """

        file_path = os.path.join(BASE_DIR, 'db',self.msg[1])
        if os.path.exists(file_path):
            file_exist = struct.pack('i', 0)  # 打 包成 四个字节
            conn.send(file_exist)
        else:
            file_exist = struct.pack('i', 1)  # 打 包成 四个字节
            conn.send(file_exist)
            file_size_len = struct.unpack('i',conn.recv(4))[0]
            # file_size = conn.recv(file_size_len)
            get_size = 0
            with open(file_path,'wb') as f:
                while True:
                    if get_size < file_size_len:
                        recv_size = conn.recv(1024)
                        f.write(recv_size)
                        get_size += len(recv_size)
                    else:
                        print('下载成功')
                        res = struct.pack('i', 0)  # 打 包成 四个字节
                        conn.send(res)
                        break

    @property
    def server_accept(self):
        conn, addr = self.server_socket.accept()
        try:
            self.handle(conn)
        except Exception as e:
            print(e)
            conn.close()
    def handle(self,conn):
        while True:
            try:
                cmd_data = conn.recv(self.RECV_MAX).decode('utf-8')
                if not cmd_data:break
                self.msg = cmd_data.split()
                cmd = self.msg[0]

                if hasattr(self,cmd):
                    getattr(self,cmd)(conn)
            except Exception as e:
                print(e)
                conn.close()
                break
    def handle_file(self,file_path,conn,num):
        if num == 1:
            with open(file_path,'rb') as f:
                while True:
                    data = f.read(1024)
                    if data:
                        conn.send(data)
                    else:
                        break


if __name__ == '__main__':
    obj = ftp_server()
    obj.server_accept