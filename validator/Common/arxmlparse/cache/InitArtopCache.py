# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\cache\InitArtopCache.py
import uuid, os
from Common import logger
from Common.Constant import COMMON_PATH, EXE_RUN_PATH
from Common.PerformanceMonitor import PM
from Common.arxmlparse.cache.ArtopRequiredCache import *
from Common.arxmlparse.artop import traverse_and_parse_dirs, uuid_elements, clearDictData, set_is_support_varianty
from Common.utils.DirUtils import copy_file_if_not_exists
local_variant = None

def runMethod(func, isRun: bool=True):
    new_uuid = uuid.uuid4()
    PM.start(new_uuid)
    if isRun:
        func()
    PM.stop_print_msg(new_uuid, f'runMethod:{func.__name__} {"finished" if isRun else "canceled"}')


def set_local_variant(value):
    global local_variant
    local_variant = value


def init_cache(inputName, vp=None):
    if inputName:
        clearDictData()
        dir_swc = []
        dir_swc.append(os.path.join(inputName, "ECU_Extract"))
        dir_swc.append(os.path.join(inputName, "bswmds"))
        dir_from_std = os.path.join(COMMON_PATH, "arxmlparse", "arxml", "std")
        dir_to_std = os.path.join(EXE_RUN_PATH, "STD")
        if not os.path.exists(dir_to_std):
            os.mkdir(dir_to_std)
        for root, dirs, files in os.walk(dir_from_std):
            for fileName in files:
                absolute_path = os.path.abspath(os.path.join(root, fileName))
                copy_file_if_not_exists(absolute_path, dir_to_std)
            else:
                break

        else:
            dir_swc.append(dir_to_std)
            if vp:
                set_is_support_varianty(True)
            else:
                set_is_support_varianty(False)
            set_local_variant(vp)
            traverse_and_parse_dirs(directories=dir_swc, vp=vp)
            dir_bsw = [
             os.path.join(inputName, "BSW_Builder")]
            traverse_and_parse_dirs(directories=dir_bsw, vp=vp)
            logger.info(f"Parsing folders : {dir_swc + dir_bsw}")

    put(uuid_elements)
