import sys,os,pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from core import main,teacher,student


class Admin(main.Person,main.School):
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
        main.Person.__init__(self,name) # 继承 重用父类函数属性

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
        teacher_obj = teacher.Teacher(teacher_name)
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
        school_obj = student.School(name,address)
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
        stu_obj = student.Student(name)
        stu_obj.school.append(name_school)

        with open(settings.path_account, 'a', encoding='utf-8') as f:
            f.write(stu_auth)

        # with open(settings.path_student_info, 'ab+') as f:
        #     pickle.dump(stu_obj, f)
        print(f"\033[0;32;40m学员 {stu_obj.name} 创建成功\033[0m ")
        print('\033[0;32;40m-----为学员选择班级-----\033[0m')
        self.show_class()
        # with open(settings.path_class_info,'rb') as f:
        #     while True:
        #         try:
        #             class_obj = pickle.upload(f)
        #             print(f"班级信息：{ class_obj.name}")
        #         except EOFError:
        #             break

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
