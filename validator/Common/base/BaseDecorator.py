# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\base\BaseDecorator.py
import functools, time
from Common import logger
from Common.ArgParser import RunArgParser
import Common.ArxmlValidator as ArxmlValidator
from Common.Public import getVariantValue
from Common.utils.JsonUtil import addValidateInfo

def RuleHandler(isPrintTime=False, isEasyModel=False):
    """
    处理校验结果的装饰器
    """

    def RuleHandlerInner(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            funcName = func.__name__
            data_msg = ArxmlValidator.dict_message.get(funcName, None)
            if data_msg is None or data_msg.get("active", False) is False:
                return
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            spendTime = "{:.3f}".format(end_time - start_time)
            validateResult = "NG" if result else "OK"
            argsInfo = f" [param={args},{kwargs}]" if isEasyModel else ""
            timeInfo = f", time consumed: {spendTime}(s)" if isPrintTime else ""
            logger.info(f"[RuleId={funcName}] --> {validateResult}{argsInfo}{timeInfo}")
            if result:
                for path, messageArgs, jumpTargets, pbKey in result:
                    if not funcName.startswith("Rule_BSW_CDD_"):
                        if funcName.startswith("Rule_BSW_Fee_") or funcName.startswith("Rule_BSW_EthTrcv_"):
                            moduleName = funcName.split("_")[2] + "_" + funcName.split("_")[3]
                    else:
                        moduleName = funcName.split("_")[2]
                    level = data_msg.get("level", 4)
                    message = (data_msg["message"].format)(*messageArgs)
                    message = f"[{funcName}] {message}"
                    solve = data_msg.get("solve", "")
                    variantValue = getVariantValue(pbKey)
                    pbName = "Common" if variantValue is None else variantValue
                    if pbName == "Common":
                        if RunArgParser.curVP != "None":
                            pbName = f"{RunArgParser.curVP}"
                    ruleId = funcName
                    addValidateInfo(moduleName, ruleId, path, message, level, jumpTargets, solve, pbName)

            return result

        return wrapper

    return RuleHandlerInner
