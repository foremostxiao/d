








# 占硬盘的读取方式 排除由于人为因素出现空行对读取造成的干扰
f = open('staff_table.txt','r',encoding='utf-8')
f2 = open('restaff_table.txt','w',encoding='utf-8')
file = f.readlines()
for i in file:
    if i == '\n':
        i = i.strip('\n')
    f2.write(i)
f.close()
f2.close()
#-----------------------------------------------------------
# 从 文件读取
data = {'staff_id':[],'name':[],'age':[],'phone':[],'dept':[],'enroll_date':[]}
f2 = open('restaff_table.txt','r',encoding='utf-8')
file2 = f2.readlines()
for i in file2:
    i = i.strip()
    i = i.split(',')
    data['staff_id'].append(i[0])
    data['name'].append(i[1])
    data['age'].append(i[2])
    data['phone'].append(i[3])
    data['dept'].append(i[4])
    data['enroll_date'].append(i[5])

#print(data)

#------------------写入------------------













condition = ['find','add','del','UPDATE','q']
cmd = input('请输入查询语法：').strip()
cmd = cmd.split()
count = 0
if cmd[0] in condition and 'where' or 'WHERE' in cmd:
    if 'age' in cmd:
        for i in data['age']:
            if i > cmd[-1]:
                count += 1
        print(f"共有{count}个员工年龄大于{cmd[-1]}")