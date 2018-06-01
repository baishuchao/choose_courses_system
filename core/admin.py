#!/usr/bin/env python
# -*- coding: utf-8 -*-
from interface import admin_interface
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
            status,mgs = admin_interface.registration_function_interface(username,password)
            if status:
                print(mgs)
                break
            else:
                print(mgs)
        else:
            print("两次密码输入不一致")





def login_function():
    """
    登陆功能
    :return:
    """
    while True:
        username = input("请输入账号:").strip()
        password = input("请输入密码:").strip()
        status,mgs = common_interface.login_interface(username,password,'admin')
        if status:
            print(mgs)
            login_info['name'] = username
            break
        else:
            print(mgs)


def create_school_function():
    '''
    创建学校功能
    :return:
    '''
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        school_name = input("请输入学校名字:").strip()
        school_address = input("请输入学校地址:").strip()
        status,mgs = admin_interface.create_school_function_interface(login_info['name'],school_name,school_address)
        if status:
            print(mgs)
            break
        else:
            print(mgs)



def create_teacher_function():
    """
    创建老师功能
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        username  = input("请输入讲师的名字:").strip()
        status,mgs = admin_interface.create_teacher_function_interface(login_info['name'],username)
        if status:
            print(mgs)
            break
        else:
            print(mgs)



def create_course_function():
    """
    创建课程功能
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        course_name  = input("请输入课程的名字:").strip()
        status,mgs = admin_interface.create_course_function(login_info['name'],course_name)
        if status:
            print(mgs)
            break
        else:
            print(mgs)

def courses_for_schools():
    """
    为校区添加课程
    :return:
    """
    if not login_info['name']:
        print("请先登陆")
        return
    while True:
        status, mgs = school_interface.check_all_school_interface()
        if status:
            for i, school in enumerate(mgs):
                print(i, ': ', school)
            opt_school = input("请选择校区:").strip()
            if opt_school == 'q':break
            opt_school = int(opt_school)
            course_list = school_interface.check_all_course()
            if course_list:
                for i,course in enumerate(course_list):
                    print(i,": ",course)
                opt_course = input("请选择课程:").strip()
                opt_course = int(opt_course)
                if opt_course == 'q':break
                status,mgs = admin_interface.courses_for_schools_interface(mgs[opt_school],course_list[opt_course])
                if status:
                    print(mgs)
                    break
                else:
                    print(mgs)
            else:
                print("请联系管理员创建课程")



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
    status, mgs = common_interface.login_interface(login_info['name'], old_pass, 'admin')
    if status:
        common_interface.change_password_interface(login_info['name'], new_pass, 'admin')
        print('更改成功')
    else:
        print(mgs)



function_dic = {
    '1': registration_function,
    '2': login_function,
    '3': create_school_function,
    '4': create_teacher_function,
    '5': create_course_function,
    '6': courses_for_schools,
    '7': change_password,
}

def admin_entrance():
    while True:
        print("""
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程
        6、为校区添加课程
        7、更改密码
        """)
        opt = input("请选择>>:").strip()
        if opt == 'q':break
        if opt not in function_dic: continue
        function_dic[opt]()

