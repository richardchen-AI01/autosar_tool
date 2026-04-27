# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\Public.py
import re
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Common.arxmlparse.artop import all_objects
from Common.arxmlparse.artop import EcucContainerValue
from Common.arxmlparse.artop import VariationPoint
from pathlib import Path

def checkRTE(module) -> bool:
    swcInstances = getBswContainerByEnum(BP.Rte_RteSwComponentInstance)
    for swcInstance in swcInstances:
        if module == swcInstance.getAttrValue(BP.Rte_RteSoftwareComponentInstanceRef).ref_type_.shortName_:
            return             return True
        return False


def getBswModule(name):
    list_module = all_objects.get("EcucModuleConfigurationValues", [])
    for moduleObj in list_module:
        if moduleObj.shortName_ == name:
            return moduleObj
        return


def checkBSW(moduleName) -> bool:
    bswModule = getBswModule(moduleName)
    return bswModule is not None


def getURIPath(father_container, element_name=None):
    def_path = father_container.path_obj
    if element_name:
        def_sub_path = def_path + "/" + element_name
        return def_sub_path
    return def_path


def getBswDefineName(container):
    def_path = container.ref_definition_
    last_part = def_path.rsplit("/", 1)[-1]
    return last_part


def getBooleanValue(container, element_name):
    """
    获取容器中的子元素的Boolean值，如果config文件中不存在Value，则返回None，证明配置文件存在问题
    """
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    for parameter in container.parameterValues_EcucParameterValue:
        ref = parameter.ref_definition_
        if ref:
            if ref == posix_path:
                value = parameter.ref_value_.mixed_
                if value is None:
                    return value
                if value == "true":
                    return                     return True
            return             return False
        return


def getStringValue(container, element_name):
    """
    获取容器中的子元素的String值，如果config文件中不存在Value，则返回None，证明配置文件存在问题
    """
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    for parameter in container.parameterValues_EcucParameterValue:
        ref = parameter.ref_definition_
        if ref and ref == posix_path:
            return parameter.value_
        return


def getFloatValue(container, element_name):
    """
    获取容器中的子元素的Float值，如果config文件中不存在Value，则返回None，证明配置文件存在问题
    """
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    for parameter in container.parameterValues_EcucParameterValue:
        ref = parameter.ref_definition_
        if ref:
            if ref == posix_path:
                if parameter.ref_value_:
                    if parameter.ref_value_.mixed_:
                        return float(parameter.ref_value_.mixed_)
            return             return None
        return


def getIntegerValue(container, element_name):
    """
    获取容器中的子元素的Integer值，如果config文件中不存在Value，则返回None，证明配置文件存在问题
    """
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    for parameter in container.parameterValues_EcucParameterValue:
        ref = parameter.ref_definition_
        if ref:
            if ref == posix_path:
                if parameter.ref_value_:
                    if parameter.ref_value_.mixed_:
                        return int(parameter.ref_value_.mixed_)
            return             return None
        return


def getReferenceParameterContainer(container, element_name):
    """
    获取容器中的子元素的引用容器值，如果config文件中不存在Value，则返回None，证明配置文件存在问题
    """
    from Common.arxmlparse.cache.InitArtopCache import local_variant
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    if container.referenceValues_EcucAbstractReferenceValue:
        for parameter in container.referenceValues_EcucAbstractReferenceValue:
            ref = parameter.ref_definition_
            if ref and ref == posix_path:
                value_dict = parameter.ref_value_
                if value_dict:
                    if isinstance(value_dict, dict):
                        value = value_dict.get(int(local_variant))
                        if value:
                            return value
                        return value_dict.get(-1)
                return value_dict

    if container.parameterValues_EcucParameterValue:
        for parameter in container.parameterValues_EcucParameterValue:
            ref = parameter.ref_definition_
            if ref and ref == posix_path:
                value_dict = parameter.value_
                if value_dict:
                    if isinstance(value_dict, dict):
                        value = value_dict.get(int(local_variant))
                        if value:
                            return value
                        return value_dict.get(-1)
                return value_dict

    return


def getReferenceParameterContainerList(container, element_name):
    """
    获取容器中的子元素的引用容器list列表值，如果config文件中不存在Value，则返回空List，证明未配置引用值
    """
    from Common.arxmlparse.cache.InitArtopCache import local_variant
    reference_lst = []
    def_path = container.ref_definition_
    def_sub_path = Path(def_path) / element_name
    posix_path = def_sub_path.as_posix()
    if container.referenceValues_EcucAbstractReferenceValue:
        for parameter in container.referenceValues_EcucAbstractReferenceValue:
            ref = parameter.ref_definition_
            if ref and ref == posix_path:
                value_dict = parameter.ref_value_
                if value_dict:
                    if isinstance(value_dict, dict):
                        value = value_dict.get(int(local_variant))
                        if value:
                            reference_lst.append(value)
                        else:
                            reference_lst.append(value_dict.get(-1))
                reference_lst.append(value_dict)

    if container.parameterValues_EcucParameterValue:
        for parameter in container.parameterValues_EcucParameterValue:
            ref = parameter.ref_definition_
            if ref and ref == posix_path:
                value_dict = parameter.value_
                if value_dict:
                    if isinstance(value_dict, dict):
                        value = value_dict.get(int(local_variant))
                        if value:
                            reference_lst.append(value)
                        else:
                            reference_lst.append(value_dict.get(-1))
                reference_lst.append(value_dict)

    return reference_lst


def parseVariantsFromVariantPoint(vp) -> list:
    """
    获取变体值列表（VariationPoint）
    """
    variants = []
    if isinstance(vp, VariationPoint):
        conditions = vp.postBuildVariantConditions_PostBuildVariantCondition
        if conditions:
            for condition in conditions:
                variants.append(condition.ref_value_)

    return variants


def findEObjectVariants(container) -> list:
    """
    获取变体值列表（container）（向上递归）
    """
    if isinstance(container, EcucContainerValue):
        vp = container.ref_variationPoint_
        if vp:
            return parseVariantsFromVariantPoint(vp)
    if container is None:
        return []
    if hasattr(container, "eContainer"):
        return findEObjectVariants(container.eContainer)


def getVariantValue(container):
    """
    获取变体值
    """
    objectVariants = findEObjectVariants(container)
    if objectVariants:
        return objectVariants[0]
    return


def getEcuName():
    """
    获得芯片名称
    """
    listEcucValueCollection = all_objects.get("EcucValueCollection")
    if listEcucValueCollection:
        return listEcucValueCollection[0].shortName_
    return ""


def getPathShortName(path=str):
    """
    获得路径字符串中最后目录的名称
    """
    if path is None:
        return ""
    if "\\" in path:
        return path.split("\\")[-1]
    if "/" in path:
        return path.split("/")[-1]
    return path
