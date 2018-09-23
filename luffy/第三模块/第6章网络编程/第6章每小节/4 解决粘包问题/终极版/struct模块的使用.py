import struct
import json


# res=struct.pack('i',1230)
# print(res,type(res),len(res))
#
#
# #client.recv(4)
# obj=struct.unpack('i',res)
# print(obj[0])



# res=struct.pack('i',12300000000)

# res=struct.pack('l',111232301212312312312312000000)
# print(res,len(res))


header_dic = {
    'filename': 'a.txt',
    'md5': 'xxdxxx',
    'total_size': 33333333333333123123123123123333333333234239487239047902384729038479023874902387409237848902374902837490238749082374908237492837498023749082374902374890237498237492837409237409237402397420398749203742093749230749023874902387492083749023874029837420893479072839048723980472390874
}

# 1 序列化 成str
header_json = json.dumps(header_dic)
print(type(header_json))

# 2 把 str ---变成---bytes
header_bytes=header_json.encode('utf-8')
print(type(header_bytes))

print(len(header_bytes))

# 3 打包
res = struct.pack('i',len(header_bytes))
print(res,len(res))

#-----------------------------客户端-----------------------------------
# obj = phone.recv(4)
header_size = struct.unpack('i', res)[0]  # 解包--得到服务端传给客户端的字节长度

# 第二步：再收报头
header_bytes = header_json.encode('utf-8')

# 第三步：从报头中解析出对真实数据的描述信息
header_json = header_bytes.decode('utf-8')  # class---> str类型
header_dic = json.loads(header_json)  # 反序列化 服务端原先的 字典
print(header_dic)
total_size = header_dic['total_size']

# i 和 l