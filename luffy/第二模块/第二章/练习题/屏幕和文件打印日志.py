# 1、logging模块有几个日志级别？
# logging模块共有5个级别，分别是：
# DEBUG INFO WARNING ERROR CRITICAL
# logging的日志可以分为 debug(), info(), warning(), error() and critical()5个级别

#2 请配置logging模块，使其在屏幕和文件里同时打印以下格式的日志
#2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts

#将日志同时输出到屏幕和日志文件
# import logging
# #logger提供了应用程序可以直接使用的接口；
# logger = logging.getLogger('access')
# logger.setLevel(level = logging.INFO)
#
# #handler将(logger创建的)日志记录发送到合适的目的输出；
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
#
#
# logger.info("Start print log")
# logger.error("account [1234] too many login attempts")
# logger.warning("Something maybe fail.")
# logger.info("Finish")


# a = 123
# # 打印输出
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.WARNING,filemode='a')
# logging.warning(f'{a}is when this event was logged.')
# a = 123
# # 保存在文件中
# logging.basicConfig(filename='log.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.WARNING, filemode='a')
# logging.warning('how to use the python.')
#(3) 将日志同时输出文件和屏幕
import logging
logger = logging.getLogger('测试')
logger.setLevel(level=logging.INFO)
#输出至文件
file = logging.FileHandler('log.txt',encoding='utf-8')
file.setLevel(level=logging.INFO)
#输出至屏幕
stream = logging.StreamHandler()
stream.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
file.setFormatter(formatter)
stream.setFormatter(formatter)
logger.addHandler(file)
logger.addHandler(stream)
logger.info("Start print log")
logger.error("account [1234] too many login attempts")
logger.warning("Something maybe fail.")
logger.info("Finish")