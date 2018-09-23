import struct
#struct 模块

res=struct.pack('i',1230) # pack 打包 ----字节长度  1230
print(res,type(res),len(res))

#
#
#client.recv(4)
obj=struct.unpack('i',res)
print(obj)
print(obj[0])



# res=struct.pack('i',12300000000)
#
# res=struct.pack('l',111232301212312312312312000000)
# print(res,len(res))