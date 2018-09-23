import sys,os,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teacher = []
        self.student = []
        self.course = []


    def show_class(self):
        with open(settings.path_class_info, 'rb+') as f:
            count = 0
            while True:
                try:
                    count += 1
                    class_obj = pickle.load(f)
                    print(f"{count}班级信息：{class_obj.__dict__}")

                except EOFError:
                    break


    def create_class(self):
        print('创建班级')
        name = input('class_name:').strip()
        course = input('course:').strip()
        time = input('class_time:').strip()
        period = input('class_period:').strip()
        class_teacher = input('class_teacher:').strip()
        class_obj = ForClass(name, course, time, period)
        class_obj.teacher.append(class_teacher)
        with open(settings.path_class_info, 'ab') as f:
            pickle.dump(class_obj, f)
        print(f"\033[0;32;40m班级{class_obj.name}创建成功\033[0m")

    def create_course(self):
        print('\033[1;31;44m  创建课程\033[0m ')
        name = input('course_name(python/linux/go):').strip()
        price = input('course_price:').strip()
        period = input('course_period:').strip()
        city = input('city：linux/py在北京，go在上海>').strip()
        course_obj = Course(name, price, period, city)
        with open(settings.path_course_info, 'ab') as f:
            pickle.dump(course_obj, f)  # pickle和json进文件是自动换行
        print(f"\033[32;0m---课程{course_obj.name}创建成功---\033[0m")


class Person:
    def __init__(self, name):
        self.name = name
        # self.sex = sex
        # self.age = age

    def show_courses(self):
        print('查看可选课程')
        with open(settings.path_course_info, 'rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    course_obj = pickle.load(f)
                    print(count, course_obj.name, course_obj.price, course_obj.period,course_obj.city)
                except EOFError:
                    break



class Course:
    def __init__(self,name,price,period,city):
        self.name = name
        self.price = price
        self.period = period
        self.city = city
        self.student = []
        self.teacher = []


class ForClass:
    def __init__(self,name,course,time,period):
        self.name = name
        self.course = course
        self.time = time
        self.period = period
        self.student = []
        self.teacher = []
class pay_tuition:
    def __init__(self,name,course_name,status):
        self.name = name
        self.course_name =course_name
        self.status = status

class Student_score:
    def __init__(self,class_name,stu_name,stu_test,stu_test_score):
        self.class_name = class_name
        self.stu_name = stu_name
        self.stu_test = stu_test
        self.stu_test_score = stu_test_score
        self.score = []  # 用于保存学生的成绩
class Student(Person,School):
    operate_lst = [
                   ('交学费', 'pay_tuition'),
                   ('选择班级', 'choice_class'),
                   ('查看可选课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('查看成绩', 'check_stu_score1'),
                   ('退出', 'exit')]

    def __init__(self, name):
        Person.__init__(self, name) # 继承父类的属性
        self.courses = [] # 班级名，学校名
        self.classes = []
        self.course_money = {}
        self.school = []
        self.score = []

    def pay_tuition(self):
        print('交学费,根据所选课程交学费')
        print('查看已选课程')
        with open(settings.path_student_info, 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if self.name in stu_obj.name:
                        if len(stu_obj.courses) == 0:
                            print('----您没有添加课程----')
                            exit()
                        else:
                            for obj in stu_obj.courses:
                                print(obj.__dict__)
                                # 输出{'name': 'python', 'price': '18000', 'period': '5个月', 'city': '北京', 'student': [], 'teacher': []}
                except EOFError:
                    break
            name = input('请输入课程名>>>')
            while True:
                money = int(input('请输入金额'))
                print('缴费成功')
                status = '缴费成功'
                pay_obj = pay_tuition(self.name,name,status)
                with open(settings.path_pay_tuition_info,'ab') as f:
                    pickle.dump(pay_obj,f)

    def choice_class(self):
        print('选择班级')
        # 查看班级
        self.show_class()
        num = int(input('请选择序号：num>>>'))
        count = 1
        with open(settings.path_class_info, 'rb') as f:
            while True:
                try:
                    class_obj = pickle.load(f)
                    class_obj.stu_name = self.__dict__['name']
                    if count == num:
                        # self.classes.append(class_obj)
                        print(f"------您选择了班级{class_obj.name}----------")
                        print()

                        with open(settings.path_student_info, 'wb+') as f2:
                            # stu_obj = pickle.upload(f)
                            self.classes.append(class_obj.name)
                            pickle.dump(self, f2)#----------------------不知道行不行------刚开始管理员创建用户是否生成了对象
                        break
                    count += 1
                except EOFError:
                    print('没有您选择的班级')
                    break

    def select_course(self):
        print('选择课程')
        self.show_courses()
        num = int(input('请选择序号num>>>'))
        count = 1
        with open(settings.path_course_info, 'rb') as f:
            while True:
                try:
                    course_obj = pickle.load(f)
                    # print(course_obj.__dict__)#对象的数据属性字典
                    if count == num:
                        # self.courses.append(course_obj)
                        print(f"您选择了{course_obj.name}")

                        # 把学生选择的课程写入学生对象中
                        with open(settings.path_student_info,'wb+') as f:
                            # stu_obj = pickle.upload(f)
                            self.courses.append(course_obj)
                            pickle.dump(self,f)
                        print()
                        # with open(settings.path_course_selected_info, 'ab') as f2:
                        #     pickle.dump(course_obj, f2)
                        break
                    count += 1  # 循环的次数-----》文件中的行数

                except EOFError:
                    print('没有您选择的课程')
                    break

    def check_selected_course(self):
        print('查看已选课程')
        with open(settings.path_student_info, 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == self.name:
                        if len(stu_obj.courses) == 0:
                            print('----您没有添加课程----')
                            break
                        else:
                            for obj in stu_obj.courses:
                                print(obj.__dict__)
                except Exception:
                    print('没有这个学生')
                    break
    def check_stu_score1(self):

        with open(settings.path_stu_score,'rb') as f:
            while True:
                try:
                    stu_score = pickle.load(f)
                    if stu_score.stu_name == self.name:
                        print(stu_score.__dict__)

                except Exception:
                    print('没有这个学生')
                    break


    def exit(self):
        exit()

    @staticmethod
    def init(name):
        # 返回一个学生对象
        # 在学生对象文件中找
        with open(settings.path_student_info, 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == name:
                        return stu_obj
                except Exception:
                    print('没有这个学生')
                    break


class Teacher(School):
    operate_lst = [('管理班级', 'manage_class'),
                   ('退出','exit')]

    def __init__(self, name):
        Person.__init__(self,name)
        # self.name_school = name_school
        # self.city_school = city_school
        self.classs = []
        self.course = []
        self.school = []


    def manage_class(self):
        print('请选择班级')
        self.show_class()
        num = int(input('请选择序号num>>>：'))
        count = 1
        with open(settings.path_class_info, 'rb') as f:
            while True:
                try:
                    class_obj = pickle.load(f)
                    # print(course_obj.__dict__)#对象的数据属性字典
                    if count == num:
                        print(f"----您选择了class_name:{class_obj.name}----")
                        choice = input("""
请选择序号操作：                        
1查看班级学员列表
2创建学生成绩
3查看学生成绩
4修改学生成绩
5退出
>>""")
                        while True:
                            if choice == '1':
                                self.check_student(class_obj.name)#传参优化代码
                                break
                            elif choice == '2':
                                self.create_stu_score(class_obj.name)
                                print()
                                break
                            elif choice == '3':
                                self.check_stu_score(class_obj.name)
                                break
                            elif choice == '4':
                                self.modify_stu_score(class_obj.name)
                                break
                            elif choice == '5':
                                break
                            else:
                                continue
                        break
                    count += 1
                    # 循环的次数-----》文件中的行数
                except EOFError:
                    print('没有您选择的班级')
                    break

    def check_student(self,class_name):#上面传参class_name优化代码
        with open(settings.path_student_info, 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if class_name in stu_obj.classes:
                        print(f"学生名单：{stu_obj.name}")
                except EOFError:
                    break

    def create_stu_score(self,class_name):
        self.check_student(class_name)
        # class_name = input('class_name:>').strip()
        while True:
            stu_name = input('请输入需要创建成绩的学生姓名stu_name:>(q,退出)').strip()
            if stu_name == 'q':
                break
            stu_test = input('考试名称stu_test:>').strip()
            stu_test_score = input('stu_test_score').strip()
            stu_score_object = Student_score(class_name, stu_name, stu_test, stu_test_score)
            with open(settings.path_stu_score, 'ab') as f:
                pickle.dump(stu_score_object, f)
                print(f"学生{stu_name}成绩创建成功")
                print('---------------------')
    def check_stu_score(self,class_name):
        print('-----查看所选班级学生成绩-------')
        with open(settings.path_stu_score, 'rb') as f:
            while True:
                try:
                    stu_score_object = pickle.load(f)
                    if class_name == stu_score_object.class_name:
                        print(f"学生成绩单：{stu_score_object.stu_name}"
                              f",{stu_score_object.stu_test},"
                              f"{stu_score_object.stu_test_score}")
                except EOFError:
                    break

    def modify_stu_score(self,class_name):
        self.check_stu_score(class_name)
        with open(settings.path_stu_score, 'rb+') as f:
            obj = []
            student_name = input('修改学生成绩，请输入姓名(q退出):>').strip()
            modify_score = input(' modify_test_score(0-100)').strip()
            while True:
                try:

                    stu_score_object = pickle.load(f)#每次反序列化一个对象
                    if student_name == stu_score_object.stu_name:
                        stu_score_object.stu_test_score = modify_score
                        obj.append(stu_score_object)
                        print('分数修改成功')
                    else:
                        obj.append(stu_score_object)

                except EOFError:

                    break
        with open(settings.path_stu_score, 'ab+') as f2:
            f2.seek(0)
            f2.truncate()
            for i in obj:
                pickle.dump(i, f2)
            print(f"{student_name}成绩修改成功")
            #占内存的修改方式
        # with open(settings.path_db, 'ab+') as f2:
            # -----这里有问题------多次dump,多次loap

    def exit(self):
        exit()

    @classmethod
    def init(cls, name):
        return cls(name)


class Admin(Person,School):
    operate_lst = [('创建课程','create_course'),
                   ('创建班级','create_class'),
                   ('查看班级','show_class'),
                   ('创建讲师','create_teacher'),
                   ('查看所有课程','show_courses'),
                   ('创建校区','create_school'),
                   ('创建学员','create_stu'),
                   ('查看学生','show_students'),
                   ('退出','exit')]
    def __init__(self,name):
        Person.__init__(self,name)#继承 重用父类函数属性

    def create_teacher(self):
        print('\033[1;31;44m创建讲师\033[0m')
        teacher_name = input('teacher name:').strip()
        teacher_password = input('teacher password:').strip()
        # sex = input('sex:').strip()
        # age = input('age:').strip()

        with open(settings.path_school_info,'rb') as f:
            while True:
                try:
                    school_obj = pickle.load(f)

                    print(f"已创建的学校名单：{school_obj.name}")
                except EOFError:
                    break

        tea_school = input('school（上海 or 北京）:').strip()
        teacher_auth = f"\n{teacher_name}|{teacher_password}|Teacher"
        teacher_obj = Teacher(teacher_name)
        teacher_obj.school.append(tea_school)
        with open(settings.path_teacher_info,'ab')as f:
            pickle.dump(teacher_obj,f)
            print(f'-----讲师{teacher_name}创建成功------')

        with open(settings.path_account, 'a', encoding='utf-8') as f:
            f.write(teacher_auth)

    def create_school(self):
        print('\033[1;31;44m创建校区\033[0m')
        name = input('name：(北京 or 上海):>').strip()
        address = input('address：北京市 or 上海市>').strip()
        school_obj = School(name,address)
        with open(settings.path_school_info, 'ab') as f:
            pickle.dump(school_obj, f)
        print(f"\033[1;42;40m学校{school_obj.name}在{school_obj.address}创建成功\033[0m")

    def create_stu(self):
        print('\033[1;31;44m创建学员\033[0m')
        name = input('student name:').strip()
        password = input('student password:').strip()
        # sex = input('sex:').strip()
        # age = input('age').strip()
        print('\033[0;32;40m----为学员选择学校----\033[0m')
        with open(settings.path_school_info, 'rb') as f:
            while True:
                try:
                    school_obj = pickle.load(f)

                    print(f"已创建的学校信息：{school_obj.name}")
                except EOFError:
                    break

        name_school = input('请为学员选择学校，school_name:>').strip()
            # city_school = input('school_city:>').strip()
        stu_auth = f"\n{name}|{password}|Student"
        stu_obj = Student(name)
        stu_obj.school.append(name_school)
        with open(settings.path_account, 'a', encoding='utf-8') as f:
            f.write(stu_auth)

        print(f"\033[0;32;40m学员 {stu_obj.name} 创建成功\033[0m ")
        print('\033[0;32;40m-----为学员选择班级-----\033[0m')
        self.show_class()
        class_name = input(' class_name:>').strip()
        stu_obj.classes.append(class_name)
        with open(settings.path_student_info, 'ab+') as f:
            pickle.dump(stu_obj, f)
            print(f'\033[0;32;40m------学员{name}信息创建成功-----\033[0m')

    def show_students(self):
        with open(settings.path_student_info,'rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    course_obj = pickle.load(f)
                    print(count,course_obj.name)
                except EOFError:
                    break
            print()

    def exit(self):
        exit()

    @classmethod
    def init(cls,name):
        return cls(name)


def login():
    print('\033[32;1m----欢迎登入选课系统----\033[0m')
    name =input('username:>').strip()
    password = input('password:>').strip()
    with open(settings.path_account ,'r',encoding='utf-8') as f:
        for line in f:
            user_name,pass_word,identify = line.strip().split('|')
            if user_name == name and password == pass_word:
                return {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}

#-------------------------------主程序---------------------------
ret = login()
if ret['result']:
    print(f"\033[1;31;40m---{ret['id']},登录成功----\033[0m")
    while True:
        # 当前内存空间有，充分的利用  反射
        if hasattr(sys.modules[__name__],ret['id']):
            cls = getattr(sys.modules[__name__],ret['id'])
            obj = cls.init(ret['name']) #例如 Student(student)
            # obj =cls(ret['name'])
            for id,item in enumerate(cls.operate_lst,1):
                print(id,item[0])
            func_str =cls.operate_lst[int(input('>>>'))-1][1]
            if hasattr(obj,func_str):
                getattr(obj,func_str)()
else:
    print('----输入错误，请重新输入-----')
    ret = login()



# ret = login()
# if ret['result']:
#     print('登录成功')
#     if ret['id'] == 'Admin':
#         obj = admin.Admin(ret['name'])
#         for id, item in enumerate(admin.Admin.operate_lst, 1):
#             print(id, item[0])
#         func_str = admin.Admin.operate_lst[int(input('>>>')) - 1][1]
#         if hasattr(obj, func_str):
#             getattr(obj, func_str)()
#     elif ret['id'] == 'Student':
#         obj = student.Student(ret['name'])
#         for id, item in enumerate(student.Student.operate_lst, 1):
#             print(id, item[0])
#         func_str = student.Student.operate_lst[int(input('>>>')) - 1][1]
#         if hasattr(obj, func_str):
#             getattr(obj, func_str)()
#     elif ret['id'] == 'Teacher':
#         obj = teacher.Teacher(ret['name'])
#         for id, item in enumerate(teacher.Teacher.operate_lst, 1):
#             print(id, item[0])
#         func_str = teacher.Teacher.operate_lst[int(input('>>>')) - 1][1]
#         if hasattr(obj, func_str):
#             getattr(obj, func_str)()
#     else:
#         print('----输入错误-----')
#
#
# else:
#     print('----输入错误，请重新输入-----')
#     ret = login()
#


