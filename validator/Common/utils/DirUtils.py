# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\utils\DirUtils.py
import os, shutil, stat

def clear(targetDir: str) -> None:
    """
    清空目录, 保留根
    :param targetDir: 目标目录
    :return: None
    """
    for filename in os.listdir(targetDir):
        filepath = os.path.join(targetDir, filename)
        if os.path.isfile(filepath):
            os.chmod(filepath, stat.S_IWRITE)
            os.remove(filepath)
        elif os.path.isdir(filepath):
            clear(filepath)
            os.rmdir(filepath)


def copy_file_if_not_exists(source_file, target_directory):
    """

    """
    target_file = os.path.join(target_directory, os.path.basename(source_file))
    if not os.path.exists(target_file):
        shutil.copy2(source_file, target_file)
