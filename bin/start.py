#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from core import src

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)    # 添加环境变量

if __name__ == '__main__':
    src.run()


