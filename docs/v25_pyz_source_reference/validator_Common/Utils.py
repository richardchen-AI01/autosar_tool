# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\Utils.py
from hashlib import md5
from typing import List
import shutil, zipfile, os, copy, importlib
from collections import OrderedDict

def getMd5(file_path):
    with open(file_path, "rb") as f:
        md5_obj = md5()
        while True:
            data = f.read(4096)
            if not data:
                break
            md5_obj.update(data)

    md5_value = md5_obj.hexdigest()
    return md5_value


def unPackZip(zip_file, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    try:
        if os.name == "nt":
            zip_path = "\\\\?\\" + os.path.abspath(zip_file)
            extract_to = "\\\\?\\" + os.path.abspath(target_folder)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    except:
        pass


def listUnique(l: List) -> List:
    return list(OrderedDict.fromkeys(l))


def listExcept(l: List, arg) -> List:
    list_new = copy.deepcopy(l)
    try:
        list_new.remove(arg)
    except:
        pass
    else:
        return list_new


class DictToObject:

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)


def singletonFunc(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


def copy_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        destination_item = os.path.join(destination_folder, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)


def loadModule(fileName, filePath):
    spec = importlib.util.spec_from_file_location(fileName, filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
