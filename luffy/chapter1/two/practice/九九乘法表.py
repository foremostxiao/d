
# for i in range(1,10):
#     for j in range(i,10):
#         print(f"{i}*{j}={i*j}")
#     print('\t')
#

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end='\t')
    print()

# 将[1,3,2,7,6,23,41,24,33,33,85,56]从小到大排序（冒泡法）
# BubbleSort
a = [1,3,2,7,6,23,41,24,33,33,85,56]
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j] > a[j+1]:
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b
print(a)
