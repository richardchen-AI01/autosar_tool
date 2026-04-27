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

def getBswContainerByEnum(enum_path: BP, variant_value=None):
    """
    通过枚举类型路径找到container
    :param enum_path: 枚举类型路径
    :return:
    """
    from Common.Public import checkBSW
    path_def = enum_path.value
    if path_def.startswith(BP.Rte_Rte.value):
        if not checkBSW(BP.Rte_Rte.shortName):
            path_def = path_def.replace(BP.Rte_Rte.value, BP.iRte_iRte.value)
    list_res = []
    list_def_elem = def_elements.get(path_def, [])
    for def_elem in list_def_elem:
        if variant_value is None:
            list_res.append(def_elem)
        elif def_elem.v_id == -1:
            list_res.append(def_elem)
        else:
            if def_elem.v_id == variant_value:
                list_res.append(def_elem)
            return list_res


def getBswContainerByObj(path_obj, variant_value=None):
    """
    通过def里的path找到container
    :param path_obj:对应数据库字段【containerPassFeatureShortName】
    :return:
    """
    res1 = path_elements.get("EcucModuleConfigurationValues", {}).get(path_obj, None)
    res2 = res1 if res1 else path_elements.get("EcucContainerValue", {}).get(path_obj, None)
    if res2 is not None:
        if variant_value != None:
            res2.get(variant_value, None)
        else:
            return list(res2.values())[0]


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
