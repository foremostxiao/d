import sys
# 获取解释器默认编码
print(sys.getdefaultencoding())
# 标准输出
print(sys.stdout.write('dd'))

#标准输入
#print(sys.stdin.readline())

#sys.argv: 实现从程序外部向程序传递参数。
import sys
print(sys.argv)
if len(sys.argv) > 1:
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])
else:
    print("没有传递参数")

# print(sys.argv[0])
# print(sys.argv[1])


