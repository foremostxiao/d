import time
# print(time.time())
# print(time.localtime())
#
# a = time.localtime()
#
# print('%s-%s-%s-%s-%s-%s'%(a.tm_year,a.tm_mon,a.tm_mday,a.tm_hour,a.tm_min,a.tm_sec))
#
# print(time.gmtime())
#
# a = time.localtime()
# print(time.mktime(a))
import time
# print("Start:",time.ctime())
# time.sleep( 5 )
# print("End :",time.ctime())

# print(time.ctime(0))
# print(time.asctime())
#print(time.strftime('%Y-%m-%d %X %U %w'))

print(time.strptime('2017-10-3 17:54',"%Y-%m-%d %H:%M"))
#print(time.strptime())