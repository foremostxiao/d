#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 12:27
# @Author  : hyang
# @Site    : 
# @File    : staff_info_manage.py
# @Software: PyCharm

"""
简单的员工信息增删改查程序
表信息
1,Alex Li,22,13651054608,IT,2013‐04‐01
2,Jack Wang,28,13451024608,HR,2015‐01‐07
3,Rain Wang,21,13451054608,IT,2017‐04‐01

增加
add staff_table xiao Li,25,136435344,IT,2015-10-29
以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增

查询支持三种语法
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"

删除指定员工信息纪录
del from staff_table where dept = "IT"

更新记录
update staff_table set dept="Market" where dept = "IT"
update staff_table set age=25 where name = "Alex Li"
"""
from tabulate import tabulate
import os

# 存储信息的文件
DB_FILE = "staff.db"
COLUMN_NAME = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']

# 打印信息
def print_log(msg, log_type="info"):
    if log_type == 'info':
        print("\033[32;1m%s\033[0m" %msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m" %msg)


def load_db(DB_FILE):
    """
    载入员工信息
    :return: 
    """
    staff_data = {}
    # 构建字典空列表
    #{'id': [],'name':[],'age': [],'phone':[],'dept':[],'enrolled_date'[]
    for d in COLUMN_NAME:
        staff_data[d] = []

    with open(DB_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            staff_datas = line.split(",")
            # 构建员工信息字典
            for ind, d in enumerate(staff_datas):
                staff_data[COLUMN_NAME[ind]].append(d.strip())  # 去掉末尾回车

    return staff_data


# match_data = op_compare(q_name.strip(), q_cond.strip(),op_key)#age 22
def op_compare(q_name, q_cond, compare_str):
    """
    #                age 22 >
    解析where 语句的操作符
    :param q_name: 
    :param q_cond: 
    :param compare_str: 
    :return: 
    """
    match_data = []
    if compare_str == "=":
        compare_str = "=="
    for ind, val in enumerate(STAFF_INFO[q_name]):
        if compare_str != "like" and q_cond.isdigit():
            # 数字比较
            exp_str = "%d%s%d" % (int(val), compare_str, int(q_cond))
        elif compare_str != "like" and not q_cond.isdigit():
            # 转换操作符两边字符串
            # 把val两边加上'val'或"val" ,与输入字符串比较 'Sales' = 'Sales' or "Sales" = "Sales"
            if q_cond.find("'") != -1:
                val = "'"+val+"'"
            elif q_cond.find("\"") != -1:
                val = "\"" + val + "\""
            else:
                val = "'" + val + "'"
                q_cond = "'" + q_cond + "'"
            # 字符比较
            exp_str = "%s%s%s" % (val, compare_str, q_cond)
            # print_log(exp_str)
        else:
            # if compare_str = like then compare_str = ' in  '
            op_str = ' in '
            if q_cond.find("'") != -1:
                val = "'" + val + "'"
            elif q_cond.find("\"") != -1:
                val = "\"" + val + "\""
            else:
                val = "'" + val + "'"
                q_cond = "'" + q_cond + "'"
            # 字符比较
            "'2015' in '2016-02-01'"
            # print(q_cond,val)
            exp_str = "%s%s%s" % (q_cond, op_str, val)
            # print_log("in="+exp_str)

        # print_log(exp_str)
        if eval(exp_str):
            row_data = []
            for col in COLUMN_NAME:
                row_data.append(STAFF_INFO[col][ind])
            match_data.append(row_data)
    # print(tabulate(match_data, headers=COLUMN_NAME, tablefmt="grid"))
    return match_data

# match_data = syntax_where(where_clause.strip())
def syntax_where(where_clause):
    """
    解析where条件 
    where age > 22
    :param where_clause: 
    :return: 
    """
    # 操作字符
    op_list = [">", "<", "=", "like"]

    for op_key in op_list:
        if op_key in where_clause:
            q_name, q_cond = where_clause.split(op_key)#符号为分隔符 例如左边是age 右边为22
            if q_name.strip() in COLUMN_NAME and q_cond.strip() != "":
                match_data = op_compare(q_name.strip(), q_cond.strip(),op_key)
                return match_data
            else:
                if not q_name.strip() in COLUMN_NAME:
                    error_str = "语法错误,字段%s不存在" % q_name
                else:
                    error_str = "条件值为空"
                print_log(error_str, "error")
                return False

    else:
        print_log("语法错误,符号不在[<,>,=,like]中","error")
        return False


def syntax_del(dataset, query_clause):
    """
     解析删除语句
     del from staff_table where id=3
    :param dataset: 
    :param query_clause: 
    :return: 
    """
    for row in dataset:
        staff_id = row[0]  # 得到id值
        staff_index = STAFF_INFO['id'].index(staff_id)  # 得到id值在STAFF_INFO[id]的索引
        # print_log(staff_index)
        for col in COLUMN_NAME:
            STAFF_INFO[col].remove(STAFF_INFO[col][staff_index])  # 修改col_name值

    save_db()
    print_log("成功删除%s条纪录" % len(dataset))


def syntax_add(dataset, query_clause):
    """
    解析增加语句
     add staff_table Alex Li,25,134435344,IT,2015-10-29
    :param dataset:  dataset = [[1,Alex Li,18,13651054608,开发,2013-04-01]]
    :param query_clause: 
    :return: 
    """
    # 得到增加的值列表
    add_data = [col.strip() for col in query_clause.split("staff_table")[-1].split(',')]
    phone_ind  = COLUMN_NAME.index("phone") # 得到手机所在列
    if(len(COLUMN_NAME) - 1 == len(add_data)):
        # 得到最后一行数据，自增长最后一行数据Id最大
        max_id = dataset[-1][0]
        # 自增长ID
        max_id = int(max_id) + 1
        # 把ID插入到第一列
        add_data.insert(0,str(max_id))
        # 得到手机号
        phone_val = add_data[phone_ind]
        # 判断手机号是否重复
        if not (phone_val in STAFF_INFO["phone"]):
            # 把数据插入到STAFF_INFO
            for index, col in enumerate(COLUMN_NAME):
                STAFF_INFO[col].append(add_data[index])

            print(tabulate(STAFF_INFO, headers=COLUMN_NAME))
            save_db()
            print_log("成功添加1条纪录到staff_table表")
        else:
            print_log("手机号%s重复" %phone_val ,'error')

    else:
        print_log("语法错误，列数不对,必须字段%s："% COLUMN_NAME[1:], "error")



def syntax_update(dataset, query_clause):
    """
    修改语句 update staff_table set age=25 where name='Alex Li'
    :param dataset: 
    :param query_clause: 
    :return: 
    """
    if "set" in query_clause:
        formula_str = query_clause.split("set")
        col_name, new_val = formula_str[-1].strip().split('=')
        # print(col_name, new_val)
        # STAFF_INFO[col_name]
        if new_val.find("'") == 0:
            new_val = new_val.replace("'", "")
        elif new_val.find("\"") == 0:
                new_val = new_val.replace("\"", "")
        for row in dataset:
            staff_id = row[0]  # 得到id值
            staff_index = STAFF_INFO['id'].index(staff_id)  # 得到id值在STAFF_INFO[id]的索引
            STAFF_INFO[col_name][staff_index] = new_val  # 修改col_name值
        # print_log(STAFF_INFO)
        save_db()
        print_log("成功修改了%s条数据!" % len(dataset))
    else:
        print_log("语法错误，未检测到set", "error")

def save_db():
    """
    #把修改的数据保存到硬盘上
    :return: 
    """
    f = open("%s.new"%DB_FILE, "w",encoding="utf-8")
    # for k in COLUMN_NAME:
    #     row = []
    #     row = STAFF_INFO[k]
    for ind, val in enumerate(STAFF_INFO["id"]):
        row = []
        for col in COLUMN_NAME:
           row.append(STAFF_INFO[col][ind])# id ==0 mame == 0 age== 0 的所有项放在一排
        w_data = ",".join(row)# 1,Alex Li,25,13651054608,IT,2013-04-01
        # print_log(w_data)
        f.write(w_data+"\n")
    f.close()

    os.remove(DB_FILE)
    os.rename("%s.new"%DB_FILE, DB_FILE)  # 回写原来的文件


#开头syntax_parser(input_str)
def syntax_parser(input_sql):
    """
    解析sql语句并执行
    :param input_sql: 
    :return: 
    """
    # print_log("syntax_parser sql star")
    syntax_list ={
        'find': syntax_find,
        'del': syntax_del,
        'add': syntax_add,
        'update': syntax_update
    }

    # 转换为小写
    if input_sql.split()[0] in syntax_list.keys() and 'staff_table' in input_str.split():
        if 'where' in input_sql.split():
            query_clause, where_clause = input_sql.split("where")#以where为切割符左边赋值给query_clause，右边赋值给where_clause
            # print_log(query_clause + where_clause)
            # 执行where条件
            match_data = syntax_where(where_clause.strip())
            input_action = query_clause.split()[0]
            # 执行不同的action
            syntax_list[input_action](match_data, query_clause)
        else:
            match_data = []
            for ind, val in enumerate(STAFF_INFO["id"]):
                row = []
                for col in COLUMN_NAME:
                    row.append(STAFF_INFO[col][ind])
                match_data.append(row)
            syntax_list[input_sql.split()[0]](match_data, input_sql.strip())

    else:
        print_log("语法错误，find/del/add/updata name,age from [staff_table] [where] age [<,>,=,like][1]", 'error')

def syntax_find(dataset, query_clause):
    """
    查询语句解析
    :param dataset: 
    :param query_clause: 
    :return: 
    """
    query_col = query_clause.split("from")[0][4:].split(',')  # 得到name,age
    filter_col = [col.strip() for col in query_col]  # 去除col中的空格
    # print(query_col)
    reformat_dataset = []
    if '*' in filter_col:  # 输出所有列
        print(tabulate(dataset, headers=COLUMN_NAME, tablefmt="grid"))
        print_log("匹配到%s条数据!" % len(dataset))
    else:
        for row in dataset:  # 筛选列
            filter_val = []
            for col in filter_col:
                index = COLUMN_NAME.index(col)
                filter_val.append(row[index])
            reformat_dataset.append(filter_val)
        print(tabulate(reformat_dataset, headers=COLUMN_NAME, tablefmt="grid"))
        print_log("匹配到%s条数据!" % len(reformat_dataset))

if __name__ == '__main__':
    """
    用户信息查询
    """
    STAFF_INFO = load_db(DB_FILE)
    while True:
        input_str = input("[staff db:]").strip()
        if not input_str : continue
        syntax_parser(input_str)

