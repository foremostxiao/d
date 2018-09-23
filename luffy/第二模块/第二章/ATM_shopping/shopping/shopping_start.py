import os,sys
BASE_DIR =os.path.dirname(os.path.abspath(__file__))#找到路径
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    import shopping_main
    shopping_main.to_auth()
