#!/usr/bin/env python
# -*- coding: utf-8 -*-
from interface import student_interface
from interface import common_interface
from interface import school_interface

login_info = {
    'name':None
}


def registration_function():
    """
    注册功能
    :return:
    """
    if login_info['name']:
        print("登陆状态不能注册")
        return
    while True:
        username = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        conf_pass = input("请确认密码:").strip()
        if password == conf_pass:
            status,mgs = student_interface.registration_function_interface(username,password)
            if status:
                print(mgs)
                break
            else:
                print(mgs)
        else:
            print("两次输入不一致")




def student_login_function():
    """
    登陆功能
    :return:
    """

    while True:
        student_name =input("请输入名字:").strip()
        password = input("请输入密码:").strip()
        status,mgs = common_interface.login_interface(student_name,password,'student')
        if status:
            print(mgs)
            login_info['name'] = student_name
            break
        else:
            print(mgs)




def choose_school_function():
    """
    选择校区功能
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
            status,mgs = student_interface.choose_school_by_student_interface(login_info['name'],mgs[opt])
            if status:
                print(mgs)
                break
            else:
                print(mgs)
        else:
            print("没有校区，请联系管理员创建")



def choose_course_function():
    """
    选择课程功能
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        school = student_interface.check_school_by_student_interface(login_info['name'])
        if not school:
            print("请先选择校区")
            break

        course_list = school_interface.check_school_all_course_interface(school)
        if course_list:
            for i, course in enumerate(course_list):
                print(i, ': ', course)
            opt = input("请选择课程:").strip()
            if opt == 'q':break
            opt = int(opt)
            status,mgs = student_interface.choose_course_function_interface(login_info['name'],course_list[opt])
            if status:
                print(mgs)
                break
            else:
                print(mgs)


def select_score_function():
    """
    查看分数
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    score_list = student_interface.select_score_function_interface(login_info['name'])
    if score_list:
        for k,v in score_list:
            print(k,':',v)
    else:
        print("目前没有成绩")

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
    status, mgs = common_interface.login_interface(login_info['name'], old_pass, 'student')
    if status:
        common_interface.change_password_interface(login_info['name'], new_pass, 'student')
        print('更改成功')
    else:
        print(mgs)


function_dic = {
    '1': registration_function,
    '2': student_login_function,
    '3': choose_school_function,
    '4': choose_course_function,
    '5': select_score_function,
    '6': change_password,
}

def student_entrance():
    while True:
        print("""
        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩 
        6、更改密码
        """)
        opt = input("请选择>>:").strip()
        if opt == 'q':break
        if opt not in function_dic: continue
        function_dic[opt]()
