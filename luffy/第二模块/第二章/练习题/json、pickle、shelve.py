#3 json、pickle、shelve三个区别是什么？
# 首先，这三个模块都是序列化工具。
# 1.
# json是所有语言的序列化工具, 优点跨语言、体积小.只能序列化一些基本的数据类型。int\str\list\tuple\dict
# pickle是python语言特有序列化工具，所有数据都能序列化。只能在python中使用，存储数据占空间大.
# shelve模块是一个简单的k, v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式。
# 2.
# 使用方式，json和pickle用法一样，shelve是f = shelve.open('shelve_test')

#序列化 dumps dump

#去序列化 upload loads
