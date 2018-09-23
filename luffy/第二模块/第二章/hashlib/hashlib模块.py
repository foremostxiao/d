import hashlib
m = hashlib.md5()
#m.update(b'Hello')
# m.update(b"It's me")
# print(m.hexdigest())#16进制格式hash
# print(m.digest())#二进制的hash

#m.update(b"It's been a long time since last time we....")
#print(m.digest())#二进制的hash
#print(len(m.hexdigest()))
#http://blog.51cto.com/1inux/2108959

m = hashlib.md5()
m.update(b'xiao&@,12')
print(m.hexdigest())

hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())#输出16进制