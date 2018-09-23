import os,sys
import logging
from logging import handlers
# 路径设置
ATM_shopping_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# 获取程序的绝对路径
#print(ATM_shopping_path)

atm_path = os.path.join(ATM_shopping_path,"atm")# 指定目录和文件名
#print(atm_path)

conf_path = os.path.join(ATM_shopping_path,"db")
#print(conf_path)

db_path = os.path.join(ATM_shopping_path,"db")
account_path = os.path.join(db_path,"account")
#print(account_path)
user_path = os.path.join(account_path,"user.json")

user2_json_path = os.path.join(account_path,"user2.json")


logs_path = os.path.join(ATM_shopping_path,"logs")
atm_user_path =  os.path.join(logs_path,"atm_user.log")
atm_manager_path =  os.path.join(logs_path,"manager_user.log")
atm_shopping_path =  os.path.join(logs_path,"shopping.log")

