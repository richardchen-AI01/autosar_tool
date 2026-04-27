# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\utils\JsonUtil.py
import json, os
from Common.utils import DirUtils
dict_ValidationResult = {}

def addValidateInfo(moduleName, ruleId, path, message, level, jumpTargets, solve, pbName):
    """
    添加校验结果信息到字典中
    """
    listResult = dict_ValidationResult.get(moduleName, [])
    valResultInfo = {}
    valResultInfo["moduleName"] = moduleName
    valResultInfo["ruleId"] = ruleId
    valResultInfo["path"] = path
    valResultInfo["message"] = message
    valResultInfo["level"] = level
    valResultInfo["jumpTargets"] = jumpTargets
    valResultInfo["solve"] = solve
    valResultInfo["pbName"] = pbName
    if valResultInfo not in listResult:
        listResult.append(valResultInfo)
    dict_ValidationResult.update({moduleName: listResult})


def genJsonResultFile(output='output'):
    if not os.path.exists(output):
        os.mkdir(output)
    else:
        DirUtils.clear(output)
    if dict_ValidationResult:
        for key, value in dict_ValidationResult.items():
            with open((os.path.join(output, f"{key}.json")), "w", encoding="utf-8") as file:
                json.dump(value, file, ensure_ascii=False, indent=4)
