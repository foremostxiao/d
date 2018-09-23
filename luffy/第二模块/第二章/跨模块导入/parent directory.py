import sys
import os
sys.path.append('D:\Pycharm\demo\LuFei\第二模块\第二章')
import subdirectory
subdirectory.fun()
from 跨模块包 import settings
settings.cousin()

print(os.path.abspath("settings.py"))
print(os.path.dirname(os.path.abspath("settings.py")))