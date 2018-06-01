#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import modles

def select_teach_course_interface(teacher_name):
    obj = modles.Teacher.select_data(teacher_name)
    course_list = obj.course_list
    if course_list:
        return True,course_list
    else:
        return False,"你没有教授的课程"


def choose_course_interface(teacher_name,course_name):
    obj = modles.Teacher.select_data(teacher_name)
    course_list = obj.course_list
    if course_name not in course_list:
        obj.add_course(course_name)
        return True,"选择成功"
    else:
        return False,"课程已选择"


def check_student_by_course(course_name):
    """
    查看某课程下的学生
    :param course_name:
    :return:
    """
    obj = modles.Course.select_data(course_name)
    student_list = obj.student_list
    if student_list:
        return False,student_list
    else:
        return False,"此课程没有学生"


def change_score_by_student(student_name,teacher_name,course_name,score):
    teacher = modles.Teacher.select_data(teacher_name)
    student = modles.Student.select_data(student_name)
    teacher.change_student_score(student, course_name, score)
