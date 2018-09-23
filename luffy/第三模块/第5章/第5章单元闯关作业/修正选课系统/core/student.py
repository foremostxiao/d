import sys,os,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from core import main

class Student(main.Person,main.School):
    operate_lst = [
                   ('交学费', 'pay_tuition'),
                   ('选择班级', 'choice_class'),
                   ('查看可选课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('查看成绩', 'check_stu_score1'),
                   ('退出', 'exit')]

    def __init__(self, name):
        main.Person.__init__(self, name) # 继承父类的属性
        # self.name = name
        # self.sex = sex
        # self.age = age
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
            # with open(settings.path_student_info, 'rb') as f:
            #     while True:
            #         try:
            #             stu_obj = pickle.upload(f)
            #             if name == stu_obj.courses:
            #                 print(f"您选择了{name}课程")
            #                 print(f"您需要缴纳的金额{stu_obj.courses.price}")
            while True:
                money = int(input('请输入金额'))
                # if money == int(stu_obj.courses.price):
                print('缴费成功')
                status = '缴费成功'
                # stu_obj.course_money[name] = '学费缴清'
                # with open(settings.path_db + 'bak', 'ab+') as f2:
                #     pickle.dump(stu_obj, f2)
                pay_obj = main.pay_tuition(self.name,name,status)
                with open(settings.path_pay_tuition_info,'ab') as f:
                    pickle.dump(pay_obj,f)
                # break
                # elif money < int(stu_obj.courses.price):
                #     print('---缴费不成功，请重新输入金额----')
                # else:
                #     print('----缴费不成功，请重新输入金额----')


                # os.remove(settings.path_stu_score)
                # os.rename(settings.path_db + 'bak', settings.path_stu_score)


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
                    # print(self.__dict__)
                    # print()  # 对象的数据属性字典
                    # print(class_obj.__dict__)
                    class_obj.stu_name = self.__dict__['name']
                    # print(class_obj.__dict__)
                    # print(class_obj)
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
