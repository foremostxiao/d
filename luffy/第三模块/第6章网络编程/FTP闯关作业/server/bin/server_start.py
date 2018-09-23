import hashlib
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# pwd = 'xiao'
# m = hashlib.md5()
# m.update(b'pwd')
# print(m.hexdigest())
from core import main
if __name__ == '__main__':
    main.FTP().run()

