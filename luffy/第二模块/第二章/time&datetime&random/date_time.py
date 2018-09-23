#import datetime
# from datetime import datetime
#
# print(datetime.now())
# # starttime = datetime.datetime.now()
# # endtime = datetime.datetime.now()
# # print(endtime - starttime)
# print(type(datetime))
# # import datetime
# # print(datetime.__file__)
# print(datetime.timedelta(1))
#print(datetime.datetime.now() + datetime.timedelta(4))
# print(datetime.time)
# import time
# print(time.time())
# from datetime import datetime
# d = datetime.now()
# print(d.replace(year=2017))

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(4))#当前时间加4天
# print(datetime.datetime.now()+datetime.timedelta(hours=4))#当前时间+4个小时

import datetime,time,os,sys

time_now = time.strftime('%Y-%m-%d')
print(time_now,type(time_now))
d1 = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
d2 = datetime.datetime.strptime(time_now, '%Y-%m-%d')
delta = d1 - d2
print(delta.days)

# d =datetime.datetime.now()
# print(time.gmtime())
# print(datetime.date(year=2018,month=8,day=18))
# print(datetime.time(hour=1,minute=20))
# print(datetime.timedelta(2018,2017))
# d =datetime.datetime.now()
# print(d.replace(year=2999,month=12))
# print(os.name)
# print(sys.version)

s='1'
print(type(s))