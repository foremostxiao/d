import logging

# logging.warning('Watch out!')  # 消息会被打印到控制台上
# logging.info('I told you so')  # 这行不会被打印，因为级别低于默认级别warning
#
# #引入日志模块
# import logging
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")
#
#
# logger_user =logging.getLogger("web")
# #每个程序在输出信息之前都要获得一个Logger。
# # Logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的Logger：
# #LOG=logging.getLogger(”chat.gui”)
# # 2 logger.setLevel()指定日志最低级别
# logger_user.setLevel(logging.DEBUG)
#
# # 3 FileHandler()输出至文件
# logger_file= logging.FileHandler('文件path',encoding='utf-8')
#
# # 4 指定被处理的信息最低级别 Handler.setLevel()
# logger_file.setLevel(logging.DEBUG)
#
# # 5 给这个输出设定一个格式
# formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
# logger_file.setFormatter(formatter)

#引入日志模块
# import logging
#
# #1 生成 logger 对象
# logger_user = logging.getLogger('atm_user')
#
# #每个程序在输出信息之前都要获得一个Logger。
# # Logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的Logger：
# #LOG=logging.getLogger(”chat.gui”)
#
# # 2 logger.setLevel()指定日志最低级别
# logger_user.setLevel(level = logging.DEBUG)
#
# # 3 FileHandler()日志输出至文件
# handler_user = logging.FileHandler('test.log',encoding='utf-8')
#
# # handler对象负责发送相关的信息到指定目的地
# # 4 指定被处理的信息最低级别 Handler.setLevel()
# handler_user.setLevel(logging.DEBUG)
#
# # 5 给这个输出设定一个格式
# formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
# handler_user.setFormatter(formatter)
#
# # 6 增加指定的文件
# logger_user.addHandler(handler_user)
#
# # 2 StreamHandler()输出至屏幕
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#
# # 3 增加指定的文件  Handler()
# logger_user.addHandler(handler_user)
# #或者控制台 Handler()
# logger_user.addHandler(console)
# #------------------------------------------------
# logger_user.info("Start print log")
# logger_user.debug("Do something")
# logger_user.warning("Something maybe fail.")
# logger_user.info("Finish")




# import logging
# logging.basicConfig(level = logging.INFO,
#                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     filename='test2.log',
#
#
#                     )
#
# logger_user = logging.getLogger('user')
#
# logger_user.info("Start print log")
# logger_user.debug("Do something")
# logger_user.warning("Something maybe fail.")
# logger_user.info("Finish")

# import  logging
# # class IgnoreBackupLogFilter(logging.Filter):
# #     def filter(self, record):
# #         return  'fail' not in record.getMessage()
import logging

# filter 过滤
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return "db backup"  in record.getMessage()
        #return "WARNING" in record.name



# 1.生成logging对象
logger = logging.getLogger('web')
logger.setLevel(logging.INFO)  # 设置日志等级
# 1.1 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())


# 2。生成hander对象
ch = logging.StreamHandler()   # 终端打印
ch.setLevel(logging.DEBUG)     # 终端打印 日志等级
fh = logging.FileHandler('web.log')  # 文件保存
fh.setLevel(logging.WARNING)   # 文件保存 日志等级

# 2.1把hander对象绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)


# 3.生成formatter 对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 3.1把formatter对象绑定到hander对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.debug("test ....")
logger.info("test info ....")
logger.warning("start to run db backup job ....")
logger.warning("start to run db backup job 1....")
logger.warning("start to run db backup job 2....")
logger.error("test error ....")

