#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: Sol_Huang
@E-mail: szhuang2021@gamil.com
@Time: 2021/04/15 10:48
@Description: path util
"""

import os


class PathUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def get_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    print(PathUtil.get_root())
