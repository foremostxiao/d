import sys,os,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from core.main import School,Person,Student_score

class Teacher(School):
    operate_lst = [('管理班级', 'manage_class'),
                   # ('查看班级学员列表', 'check_student'),
                   # ('创建学生成绩', 'create_stu_score'),
                   # ('查看学生成绩', 'check_stu_score'),
                   ('退出','exit')

                   ]

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
                        # print(self.__dict__)
                        # print(class_obj.__dict__)
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
        # print('查看班级学员列表')
        # print('请选择班级')

        # self.show_class()
        # class_name = input('请输入班级名>>>')
        # # count = 1
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

