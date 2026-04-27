# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop.py
from Common.arxmlparse.artop_R19.all_class_mulit import *
from Common.arxmlparse.artop_R19.entity import *
from Common.arxmlparse.artop_R19.parse_file import *
from Common.arxmlparse.constant.ArtopParseConstant import all_class_mulit_temp

def updateAllClassMulti(dict_param):
    all_class_mulit.clear()
    all_class_mulit.update(dict_param)


updateAllClassMulti(all_class_mulit_temp)
