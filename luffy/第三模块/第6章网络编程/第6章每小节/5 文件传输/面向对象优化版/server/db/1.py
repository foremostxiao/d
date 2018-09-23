import socket,os,sys
import struct,pickle
import subprocess
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
pt_path = os.path.join(BASE_DIR,'a.txt')
file_size = os.path.getsize(pt_path)
print(file_size,type(file_size))
#290 <class 'int'>