# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\cache\InitArtopCache.py
import sys, uuid, os
from Common.Constant import COMMON_PATH
from Common.PerformanceMonitor import PM
from Common.Utils import copy_folder
from Common.arxmlparse.cache.ArtopRequiredCache import *
from Common.arxmlparse.artop import traverse_and_parse_dirs, uuid_elements, set_is_support_varianty

def runMethod(func, isRun: bool=True):
    new_uuid = uuid.uuid4()
    PM.start(new_uuid)
    if isRun:
        func()
    PM.stop_print_msg(new_uuid, f'runMethod:{func.__name__} {"finished" if isRun else "canceled"}')


def init_cache(inputName, dict_data: dict=None):
    if uuid_elements:
        return
    if inputName:
        if dict_data is None:
            dict_data = {'ECU_Extract': 1, 
             'bswmds': 1, 
             'STD': 1, 
             'ServiceComponents': 0}
        class_mapping = dict_data.get("class_mapping", None)
        dir_swc = []
        for key, value in dict_data.items():
            if value and key != "BSW_Builder":
                if key != "bswmds":
                    if key != "STD":
                        dir_swc.append(os.path.join(inputName, key))
                    else:
                        dir_from_std = os.path.join(COMMON_PATH, "arxmlparse", "arxml", "std")
                        dir_to_std = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "STD")
                        if not os.path.exists(dir_to_std):
                            os.mkdir(dir_to_std)
                        copy_folder(dir_from_std, dir_to_std)
                        dir_swc.append(dir_to_std)
                traverse_and_parse_dirs(dir_swc, class_mapping)
                dir_bswmd = [
                 os.path.join(inputName, "bswmds")]
                traverse_and_parse_dirs(dir_bswmd, class_mapping)
                set_is_support_varianty(True)
                dir_bsw = [os.path.join(inputName, "BSW_Builder")]
                traverse_and_parse_dirs(dir_bsw, class_mapping)
                set_is_support_varianty(False)

    put(uuid_elements)
