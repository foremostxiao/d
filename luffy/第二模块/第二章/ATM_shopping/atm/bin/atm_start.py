
#添加环境变量
import os,sys
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# -------------------程序的入口---------------------------
if __name__ == '__main__':
    from core import user_and_manager
    user_and_manager.user_choice()

