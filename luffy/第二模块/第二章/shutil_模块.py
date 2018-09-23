# 全部copy内容
# import shutil
# f1 = open('os_模块.py','r',encoding='utf-8')
# f2 = open('for_test.py','w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)

# shutil.copyfile(文件1，文件2)：不用打开文件，直接用文件名进行覆盖copy。
import shutil
# f1 = open('os_模块.py','r',encoding='utf-8')
# f2 = open('for_test.py','w',encoding='utf-8')
shutil.copyfile('os_模块.py','for_test.py')