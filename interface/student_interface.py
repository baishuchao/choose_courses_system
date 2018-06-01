#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import modles

def registration_function_interface(name,password):
    obj = modles.Student.select_data(name)
    if not obj:
        modles.Student(name,password)
        return True,"创建成功"
    else:
        return False,"用户已存在"




def choose_school_by_student_interface(student_name,school_name):
    obj = modles.Student.select_data(student_name)
    if not obj.school:
        obj.choose_school(school_name)
        return True,"选择成功"
    else:
        return False,"校区已选择"


def check_school_by_student_interface(student_name):
    """
    查看学生是那个校区的
    :param student_name:
    :return:
    """
    obj = modles.Student.select_data(student_name)
    return obj.school


def choose_course_function_interface(student_name,course_name):
    obj = modles.Student.select_data(student_name)
    if course_name not in obj.course_list:
        obj.choose_course(course_name)
        return True,"选课成功"
    else:
        return False,"此课程已选，不能再次选择"




def select_score_function_interface(student_name):
    obj  = modles.Student.select_data(student_name)
    return obj.scores






