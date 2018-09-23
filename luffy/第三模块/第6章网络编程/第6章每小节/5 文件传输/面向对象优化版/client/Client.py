import socket
import struct
import subprocess,os,sys,pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

class ftp_client:
    ip_port = ('127.0.0.1',8080)
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def get(self):
        """"
        0.判断指令是否正确
        1.客户端判断文件是否存在
                1.1、存在---输出该文件已存在
                1.2、不存在：执行下载功能
                    1.2.1.解压，服务端传来的文件报头长度-file_size_len,
                        1.2.1.1.如果file_size_len==0,需要下载的文件不存在
                        1.2.1.2.file_size_len!=0, handle_file进行写入文件
                        1.2.1.3.接受文件大小file_size
        """
        if len(self.cmd)>1:
            file_path = os.path.join(BASE_DIR,self.cmd[1])
            if os.path.exists(file_path):
                print('----该文件已存在----')
            else:
                file_size_len = struct.unpack('i',self.client_socket.recv(4))[0] #数据的总长度，以字节为单位
                if file_size_len == 0:
                    print('----需要下载的文件不存在----')
                #接收数据
                else:
                    recv_size = 0
                    header_bytes = self.client_socket.recv(file_size_len) # 字节大小
                    head_dic = pickle.loads(header_bytes)
                    file_size = head_dic['file_size']

                    self.handle_file(file_path,file_size)
        else:
            print('没有输入文件名')



    def put(self):
        """
        0.判断指令是否正确
        1.判断文件是否存在
            1.客户端存在
                1.2.判断服务端是否已存在该文件
                    1.2.1.存在  服务器返回------服务端已存在该文件----
                    1.2.2.不存在 发送报头的长度，再发送报头

        """
        if len(self.cmd)>1:
            file_path = os.path.join(BASE_DIR, self.cmd[1])

            if os.path.exists(file_path):
                # file_name = struct.pack('i',self.cmd[1]) # 打包成了字节模式
                # self.client_socket.send(file_name)
                """判断服务端是否存在该文件"""
                file_exist=struct.unpack('i',self.client_socket.recv(4))[0]
                if file_exist == 0:
                    print('----服务端已存在该文件----')

                else:
                    self.handle_file(file_path,1)
                    #上传的结果反馈
                    res = struct.unpack('i',self.client_socket.recv(4))[0]
                    if res == 0:
                        print('put sucess')
            else:
                print('该文件不存在')

        else:
            print('没有输入文件名')
    @property
    def handle(self):
        while True:
            msg = input('>>').strip()
            if not msg:continue
            self.client_socket.send(msg.encode('utf-8')) #发送完整的指令给服务端口
            self.cmd = msg.split()
            if hasattr(self,self.cmd[0]):
                getattr(self,self.cmd[0])()



    def handle_file(self,file_path,file_size):
        if self.cmd[0] == 'get':

            with open(file_path,'wb') as f:
                get_size = 0
                while True:
                    if get_size < file_size:
                        file_bytes = self.client_socket.recv(1024)# 收到的是字节
                        f.write(file_bytes)
                        get_size += len(file_bytes)
                        # self.progress_bar(1, get_size, file_size)
                    else:
                        print('下载成功')
                        break
        if self.cmd[0] == 'put':
            file_size2 = os.path.getsize(file_path)# 文件的大小本质上就是指字节的长度
            # head_dic间接封装报头的长度
            # head_dic={'filename':self.cmd[1],
            #           'file_md5':'aaaa',
            #           'file_size':file_size2
            #           }
            # head_pickle = pickle.dumps(head_dic)

            file_bytes = struct.pack('i', file_size2)#直接封装报头的长度
            self.client_socket.send(file_bytes) # 发送报头长度
            with open(file_path,'rb') as f:
                while True:
                    data = f.read(1024)
                    if data:
                        self.client_socket.send(data)
                    else:
                        break
    @property
    def connect(self):
        self.client_socket.connect(self.ip_port)
        self.handle

    def progress_bar(self,num,get_size, file_size):
        pass

if __name__ == '__main__':
    obj = ftp_client()
    obj.connect