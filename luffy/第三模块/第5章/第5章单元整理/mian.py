import os
import pickle
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# data2 = {'aa': [1, 2.0, 3, 4+6j],
#          'bb': ('string', u'Unicode string'),
#          'cc': None}
#
# pkfile=open("testfile.txt",'ab')
# pickle.dump(data1,pkfile)
# pickle.dump(data2,pkfile)
# pkfile.close()


with open("testfile.txt",'rb') as f:
    while True:
        try:
            pkf=pickle.load(f)
            print(pkf)
        except Exception as e:
            print(e)
            break
# pkf1=pickle.load(pkfile2)


# print(pkf1)

