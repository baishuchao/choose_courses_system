#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db import modles


def login_interface(name,password,type):
    if type == 'admin':
        obj = modles.Admin.select_data(name)
        if obj:
            if obj.password == password:
                return True,"登陆成功"
            else:
                return False,"密码错误"
        else:
            return False,"用户不存在"

    if type == 'teacher':
        obj = modles.Teacher.select_data(name)
        if obj:
            if obj.password == password:
                return True,"登陆成功"
            else:
                return False,"密码错误"
        else:
            return False,"用户不存在"
    if type == 'student':
        obj = modles.Student.select_data(name)
        if obj:
            if obj.password == password:
                return True,"登陆成功"
            else:
                return False,"密码错误"
        else:
            return False,"用户不存在"



def change_password_interface(name,new_password,type):
    if type == 'teacher':
        obj = modles.Teacher.select_data(name)
        obj.change_password(new_password)

    elif type == 'student':
        obj = modles.Student.select_data(name)
        obj.change_password(new_password)

    elif type == 'admin':
        obj = modles.Admin.select_data(name)
        obj.change_password(new_password)


