#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
from conf import setting

def save_the_data(obj):
    '''
    obj.__class__.__name__   # 查看类的名字

    :param obj:
    :return:
    '''
    path = os.path.join(setting.BASE_DB,obj.__class__.__name__.lower())   # 目录路径
    if not os.path.isdir(path):  # 判断目录是否存在,不存在则创建
        os.mkdir(path)
    path_file = os.path.join(path,obj.name)
    with open(path_file,mode='wb') as f:
        pickle.dump(obj,f)
        f.flush()


def select_the_data(name,type):
    path = os.path.join(setting.BASE_DB,type)
    if not os.path.isdir(path):   # 判断目录是否存在
        os.mkdir(path)
    path_file = os.path.join(path,name)
    if os.path.exists(path_file):
        with open(path_file,mode='rb') as f:
            return pickle.load(f)
    else:
        return False


