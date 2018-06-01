#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import modles
from conf import setting
import os
from db import modles


def check_all_school_interface():
    """
    查看所有校区
    :return:
    """
    BASE = os.path.join(setting.BASE_DB,'school')
    school_list = os.listdir(BASE)
    if school_list:
        return True,school_list

    else:
        return False,"还没有校区，请联系管理员创建"

def check_school_all_course_interface(school_name):
    '''
    查看某学校的课程
    :param school_name:
    :return:
    '''
    obj = modles.School.select_data(school_name)
    return obj.course_list

def check_teacher_all_course(teacher_name):
    """
    查看某老师下的课程
    :param teacher_name:
    :return:
    """
    obj = modles.Teacher.select_data(teacher_name)
    return obj.course_list


def check_all_course():
    BASE = os.path.join(setting.BASE_DB,'course')
    course_list = os.listdir(BASE)
    return course_list
