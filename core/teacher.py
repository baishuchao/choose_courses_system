#!/usr/bin/env python
# -*- coding: utf-8 -*-
from interface import common_interface
from interface import teacher_interface
from interface import school_interface

login_info = {
    'name':None
}

def login_function():
    """
    登陆功能
    :return:
    """
    while True:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        status,mgs = common_interface.login_interface(username,password,'teacher')
        if status:
            print(mgs)
            login_info['name'] = username
            break
        else:
            print(mgs)


def select_teach_course():
    '''
    查看教授的课程
    :return:
    '''
    if not login_info['name']:
        print("请先登陆")
        return
    status,mgs = teacher_interface.select_teach_course_interface(login_info['name'])
    if status:
        for i in mgs:
            print(i)
    else:
        print(mgs)


def choose_teach_course():
    """
    选择教授的课程
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        status,mgs = school_interface.check_all_school_interface()
        if status:
            for i,school in enumerate(mgs):
                print(i,': ',school)
            opt = input("请选择校区:").strip()
            if opt == 'q':break
            opt = int(opt)
            course_list = school_interface.check_school_all_course_interface(mgs[opt])
            if course_list:
                for i,course in enumerate(course_list):
                    print(i,': ',course)
                opt = input("请选择课程:").strip()
                if opt == 'q':break
                opt = int(opt)
                status,mgs = teacher_interface.choose_course_interface(login_info['name'],course_list[opt])
                if status:
                    print(mgs)
                    break
                else:
                    print(mgs)

            else:
                print("本校区没有创建课程，请联系管理员")

        else:
            print(mgs)



def select_student_by_course():
    '''
    查看课程下的学生
    :return:
    '''
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        course_list = school_interface.check_teacher_all_course(login_info['name'])
        if course_list:
            for  i,course  in enumerate(course_list):
                print(i,": ",course)
            opt = input("请选择课程>>:").strip()
            if opt == 'q':break
            opt = int(opt)
            status,mgs = teacher_interface.check_student_by_course(course_list[opt])
            if status:
                for i in mgs:
                    print(i)
            else:
                print(mgs)
        else:
            print("你没有教授课程")


def change_student_score():
    '''
    更改学生成绩
    :return:
    '''
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        course_list = school_interface.check_teacher_all_course(login_info['name'])
        if course_list:
            for  i,course  in enumerate(course_list):
                print(i,": ",course)
            opt1 = input("请选择课程>>:").strip()
            if opt1 == 'q':break
            opt1 = int(opt1)
            status,mgs = teacher_interface.check_student_by_course(course_list[opt1])
            if status:
                for i,student in enumerate(mgs):
                    print(i,": ",student)
                opt = input("请选择学生:").strip()
                if opt == 'q':break
                opt = int(opt)
                score = input('请输入修改的分数：').strip()
                teacher_interface.change_score_by_student(mgs[opt],login_info['name'],course_list[opt1],score)
                print('成绩修改成功')
            else:
                print(mgs)
        else:
            print("你没有教授课程")

def change_password():
    """
    更改密码
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    old_pass = input("请输入旧密码:").strip()
    new_pass = input("请输入新密码:").strip()
    status, mgs = common_interface.login_interface(login_info['name'], old_pass, 'teacher')
    if status:
        common_interface.change_password_interface(login_info['name'], new_pass, 'teacher')
        print('更改成功')
    else:
        print(mgs)

function_dic = {
    '1': login_function,
    '2': select_teach_course,
    '3': choose_teach_course,
    '4': select_student_by_course,
    '5': change_student_score,
    '6': change_password,
}

def teacher_entrance():
    while True:
        print("""
        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩
        6、更改密码
        """)
        opt = input("请选择>>:").strip()
        if opt == 'q':break
        if opt not in function_dic:continue
        function_dic[opt]()


