#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core import admin
from core import student
from core import teacher



entrance = {
    '1': student.student_entrance,
    '2': teacher.teacher_entrance,
    '3': admin.admin_entrance,
}


def run():
    while True:
        print('''
        1. 学生入口
        2. 讲师入口
        3. 管理入口
        ''')
        opt = input("请选择>>:").strip()
        if opt == 'q':break
        if opt not in entrance:continue
        entrance[opt]()



