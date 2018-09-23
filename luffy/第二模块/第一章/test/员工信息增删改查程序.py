
def all_need():
    global file
    file = open('restaff_table.txt', 'r+', encoding='utf-8')
    f = file.readlines()
    global  data_list
    data_list = []
    for i in f:
        i = i.strip()
        data_list.append(i.split(','))
        #[[],[],[],[],[]]

def rewrite():
    file.seek(0)
    file.truncate()
    #file.close()
    for line in data_list:
        str = ','.join(line)
        file2 = open('restaff_table.txt', 'a', encoding='utf-8')
        file2.write(str+'\n')
        # 不加会显示错误，，数字不对
        file2.close()

def find_info():
    while True:
        choice2 = input("""
(请选择查询序号)：
1 find name,age from staff_table where age > 22
2 find * from staff_table where dept = "IT"
3 find * from staff_table where enroll_date like "2013"
q 退出
>""").strip()
        all_need()
        count = 0
        if choice2 == 'q':
            file.close()
            break
        if choice2 not  in ['1','2','3']:
            print('\033[31m input wrong \033[0m ')
        for i in range(0, len(data_list)):
            if choice2 == '1':
                if int(data_list[i][2]) > 22:
                    data_str = ' '.join(data_list[i][1:3]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
            if choice2 == '2':
                if data_list[i][4] == 'IT':
                    data_str = ' '.join(data_list[i]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
            if choice2 == '3':
                if '2013' in data_list[i][5]:
                    data_str = ' '.join(data_list[i]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
        print(f"\033[31m 查询结束，符合条件数为{count} \033[0m")
#以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
def add_info():
    count1 = 0
    while True:
        count = 0
        choice3 = input("""
(请选择序号)：
1 (录入员工信息:)
q 退出
>""").strip()
        if choice3 == '1':
            all_need()
            new_staff_info = input('''
请按如下顺序输入：
name,age,phone,dept,enroll-date
>''').strip()
            new_staff_list = new_staff_info.split(',')
            new_staff_id = str(len(data_list)+1)
            new_staff_list.insert(0,new_staff_id)
            if len(new_staff_list) != 6:
                print('\033[31m 输入信息不完整，请重新输入 \033[0m')
                continue
            else:
                for i in range(0, len(data_list)):
                    if data_list[i][3] == new_staff_list[3]:
                        print('\033[31m 已存入该员工信息！\033[0m')
                        count += 1
                        break
            if count == 0:
                new_staff_str = ','.join(new_staff_list).strip()
                file2 = open('restaff_table.txt', 'a+', encoding='utf-8')
                file2.write('\n'+new_staff_str)
                file2.close()
                #count += 1
                count1 += 1
                print(f"\033[31m 新添加的员工信息为：{new_staff_list}\033[0m ")
        if choice3 not in ['1','q']:
            print('\033[31m 输入有误，请选择 1 或者 q \033[0m')
        if choice3 == 'q':
            print(f"\033[31m 添加结束，共添加{count1}个员工信息\033[0m")
            break

def del_info():
    count = 0
    while True:
        all_need()
        id_list = []
        for index in range(0,len(data_list)):
            id_list.append(data_list[index][0])
        print(f'\033[31m id的取值范围为\033[0m {id_list}')
        staff_id = input("""        
\033[31m 请输入需要删除的员工id\033[0m
id：delete from staff_table where staff_id = 3
q：退出
>""").strip()
        if staff_id =='q':
            print(f"\033[31m  删除结束，共删除{count}个员工 \033[0m")
            break
        if staff_id not in id_list:
            print('\033[31m  输入无效id \033[0m')
            continue
        for j in reversed(range(0,len(data_list))):

            if data_list[j][0] == staff_id:
                del data_list[j]
                print(f'\033[31m 已删除id为{staff_id}的员工信息 \033[0m')
                rewrite()
        count += 1
def modify_info():
    while True:
        modify = input("""
请选择下列序号：
1 把所有dept=IT的纪录的dept改成Market
2 把name=Alex Li的纪录的年龄改成25
q 退出
>""").strip()
        all_need()
        if modify == 'q':
            break

        count = 0
        for i in range(0, len(data_list)):
            if modify == '1':
                if data_list[i][4] == 'IT':
                    data_list[i][4] = 'Market'
                    rewrite()
                    count += 1
            if modify == '2':
                if data_list[i][1] == "Alex Li":
                    data_list[i][2] = '25'
                    rewrite()
                    count += 1

        print(f"\033[31m共改动{count}处信息\033[0m")
        if modify not in ['1','2','q']:
            print('输入错误，请重新输入')
            continue

#---------------主函数----------------------
print('-----欢迎登陆员工管理系统------')
file1 = open('staff_table.txt', 'r', encoding='utf-8')  # 要去掉空行的文件

file2 = open('restaff_table.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
try:
    for line in file1.readlines():
        # 判断是否为空行
        if line == '\n':
            line = line.strip("\n")
        # 读出来的时候每一行自带一个换行符号
        file2.write(line)
finally:
    file1.close()
    file2.close()
while True:
    choice = input("""
请选择下列序号：
1 查询 
2 增
3 删
4 改
q 退出
>""").strip()
    if choice == '1':
        find_info()
    if choice == '2':
        add_info()
    if choice == '3':
        del_info()
    if choice == '4':
        modify_info()
    if choice == 'q':
        exit()
