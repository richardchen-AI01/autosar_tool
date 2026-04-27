# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\cache\BswModuleCache.py
from typing import TypeVar
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.artop import def_elements, path_elements
T = TypeVar("T")
dict_bsw_module_to_container = {}
dict_ea_to_list_imp = {}

def getBswContainerByEnum(enum_path: BP):
    """
    通过枚举类型路径找到container
    :param enum_path: 枚举类型路径
    :return:
    """
    path_def = enum_path.value
    return def_elements.get(path_def, [])


def getBswContainerByObj(path_obj):
    """
    通过def里的path找到container
    :param path_obj:对应数据库字段【containerPassFeatureShortName】
    :return:
    """
    dict_container = {}
    dict_container.update(path_elements.get("EcucModuleConfigurationValues", {}))
    dict_container.update(path_elements.get("EcucContainerValue", {}))
    return dict_container.get(path_obj, None)


def add_list(obj, list_result):
    if obj:
        list_result.append(obj)


def create_bsw_instance(clazz: T) -> list:
    """
    根据传入的bsw class生成实例对象列表
    """
    res_list = []
    if hasattr(clazz, "enum_path"):
        container_list = getBswContainerByEnum(clazz.enum_path)
        for container in container_list:
            res_list.append(clazz(container))

    return res_list


def initBswModuleCache():
    for key, value in def_elements.items():
        dict_bsw_module_to_container[key] = value
    else:
        list_imp = getBswContainerByEnum(enum_path=(BP.Rte_RteExclusiveAreaImplementation))
        for imp in list_imp:
            ref_ea = imp.getAttrValue(enum_path=(BP.Rte_RteExclusiveAreaRef))
            if ref_ea not in dict_ea_to_list_imp:
                dict_ea_to_list_imp[ref_ea] = [
                 imp]
            else:
                dict_ea_to_list_imp[ref_ea].append(imp)
