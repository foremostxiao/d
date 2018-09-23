import shelve

s = shelve.open('test_shelf.db') #打开文件
print(s['kk'],type(s['kk'])) #访问数据
s.close()
