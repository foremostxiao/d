# dumps仅转化成字符串

#json只产生str对象，不支持bytes对象，所以fp.write()必须支持str输入
import json
# data = {'k1':123,'k2':'hello'}
# d = json.dumps(data)
# d1 = json.loads(d)
# print('序列化',d,type(d))
# print('反序列化d1',d1,type(d1))



#转化为字符并写入文件dump
data2 ={'a1':123,'b1':456}
with open('test序列.py','a+',encoding='utf-8') as f:
    f1 = json.dump(data2,f)
    print('序列化dump:',f1,type(f1))

#反序列化：
import json
with open('test序列.py','r') as f2:
    file = json.load(f2)
    print('反序列化load:',file,type(file))


# 2 pickle模块：
# import pickle
# # data = {'k1':123,'k2':'abc'}
# # d = pickle.dumps(data)
# # d2 = pickle.loads(d)
# # print('序列化',d,type(d))
# # print('反序列化d1',d2,type(d2))
#
# f = open('test1.txt','r+')
# data = {'k1':123,'k2':'abc'}
# f1 = pickle.dump(data,f)    #序列化对象到文件
# print('pickle.dump(data,f):',f1,type(f1))
# f = open('test1.txt','rb')
# red = pickle.upload(f)   #从文件中反序列化对象
# print('pickle.upload(f)',red,type(red))