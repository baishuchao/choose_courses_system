#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import modles

def registration_function_interface(name,password):
    obj = modles.Admin.select_data(name)
    if not obj:
        obj = modles.Admin()
        obj.registration(name,password)
        return True,"注册成功"
    else:
        return False,"用户已存在"


def create_school_function_interface(admin_name,name,school_address):
    obj = modles.School.select_data(name)
    if not obj:
        admin = modles.Admin.select_data(admin_name)
        admin.create_school(name,school_address)
        return True,"创建成功"
    else:
        return False,"学校已存在"


def create_teacher_function_interface(admin_name,name,password='123'):
    obj = modles.Teacher.select_data(name)
    if not obj:
        admin = modles.Admin.select_data(admin_name)
        admin.create_teacher(name,password)
        return True,"讲师创建成功"
    else:
        return False,"用户已存在"


def create_course_function(admin_name,course_name):
    obj = modles.Course.select_data(course_name)
    if not obj:
        admin = modles.Admin.select_data(admin_name)
        admin.create_course(course_name)
        return True,"课程创建成功"
    else:
        return False,"课程已存在"


def courses_for_schools_interface(school_name,course_name):
    obj = modles.School.select_data(school_name)
    if course_name not in obj.course_list:
        obj.add_course(course_name)
        return True,"添加成功"
    else:
        return False,"课程已存在"