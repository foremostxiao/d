import shelve

s = shelve.open('test_shelf.db','w')
try:
    s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
    s['MM'] = [1, 2, 3]
finally:
    s.close()