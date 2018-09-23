import logging
# logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")
#看一下这几个日志级别分别代表什么意思
# logging.basicConfig(filename='example.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
#
#
#
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
#
# logger = logging.getLogger('mysql')
# logger.setLevel(level=logging.DEBUG)
# logger.addFilter()

# 将日志写入文件
# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# 将日志同时输出到屏幕和日志文件
import logging
#logger提供了应用程序可以直接使用的接口；
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
#handler将(logger创建的)日志记录发送到合适的目的输出；
# FileHandler()输出至屏幕
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
#formatter决定日志记录的最终输出格式。
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# StreamHandler()输出至屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
#增加指定的Handler
logger.addHandler(handler)
logger.addHandler(console)

#logger.info("Start print log")
logger.debug("account [1234] too many login attempts")
#logger.warning("Something maybe fail.")
#logger.info("Finish")


# _*_coding:utf-8_*_
# created by Alex Li on 10/19/17


import logging
from logging import handlers


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return  "db backup" in record.getMessage()
#引入日志模块
import logging
#1.生成 logger 对象
logger =logging.getLogger("web")
#每个程序在输出信息之前都要获得一个Logger。
# Logger通常对应了程序的模块名，比如聊天工具的图形界面模块可以这样获得它的Logger：
#LOG=logging.getLogger(”chat.gui”)
# 2 logger.setLevel()指定日志最低级别
logger.setLevel(logging.DEBUG)

#1.1 把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

#2. 生成 handler对象
ch = logging.StreamHandler()
#ch.setLevel(logging.INFO)

#fh = logging.FileHandler("web.log")
#fh = handlers.RotatingFileHandler( "web.log",maxBytes=10,backupCount=3)
fh = handlers.TimedRotatingFileHandler( "web.log",when="S",interval=5,backupCount=3)
#fh.setLevel(logging.WARNING)

#2.1 把 handler对象 绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

#3.生成formatter 对象
#3.1 把formatter 对象 绑定handler对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



logger.warning("test log ")
logger.info("test log 2")
logger.debug("test log 3")
logger.debug("test log db backup 3")

#console : INFO
#global : DEBUG  default level : warning
#file :Warning

#全局设置为DEBUG后， console handler 设置为INFO, 如果输出的日志级别是debug, 那就不会在屏幕上打印