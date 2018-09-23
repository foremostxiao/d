import logging,os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings

#---------------------atm_user-------------------------
logger_user = logging.getLogger('atm_user')
# logger.setLevel()指定日志最低级别
logger_user.setLevel(level = logging.DEBUG)
#FileHandler()输出至文件
handler_user = logging.FileHandler(settings.atm_user_path,encoding='utf-8')
#指定被处理的信息最低级别 Handler.setLevel()
handler_user.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
handler_user.setFormatter(formatter)
logger_user.addHandler(handler_user)

#---------------------atm_manager------------------------
logger_manager = logging.getLogger('atm_manager')
logger_manager.setLevel(level = logging.DEBUG)
handler_manager = logging.FileHandler(settings.atm_manager_path,encoding='utf-8')
handler_manager.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler_manager.setFormatter(formatter)
logger_manager.addHandler(handler_manager)

#---------------------shopping----------------------------
logger_shopping = logging.getLogger('shopping')
logger_shopping.setLevel(level = logging.DEBUG)
handler_shopping = logging.FileHandler(settings.atm_shopping_path,encoding='utf-8')
handler_shopping.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler_shopping.setFormatter(formatter)
logger_shopping.addHandler(handler_shopping)



# handler = logging.FileHandler()
# handler.setLevel(logging.INFO)
# # 1 FileHandler()输出至文件
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.ERROR)
#
# # 2 StreamHandler()输出至屏幕
# console = logging.StreamHandler()
# console.setLevel(logging.ERROR)
#
# # 3 增加指定的文件或者控制台 Handler()
# logger.addHandler(handler)
# logger.addHandler(console)
#
# #formatter决定日志记录的最终输出格式。
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
