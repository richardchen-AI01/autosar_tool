# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\ArxmlValidator.py
import inspect, json, os, shutil, traceback
from Common import Constant, Public
from Common.ArgParser import RunArgParser
from Common.PerformanceMonitor import *

class ArxmlValidator:
    dict_message = {}
    dict_changeTarget = {}

    def __init__(self) -> None:
        self.moduleName = self.__class__.__name__.replace("ArxmlValidator", "")
        self._module = Public.getBswModule(self.moduleName)
        self._ArxmlValidator__output_path = Constant.OUTPUT_PATH
        if RunArgParser.outputPath:
            self._ArxmlValidator__output_path = RunArgParser.outputPath

    def createMessageData(self, dir_module):
        root_dir_name = os.path.basename(os.path.dirname(dir_module))
        file_json_outer = self.handle_rules_dir(dir_module, root_dir_name)
        with open(file_json_outer, "r", encoding="utf-8") as file:
            data = json.load(file)
            for dataItem in data:
                if dataItem["active"]:
                    message_key = dataItem["key"]
                    self.dict_message[message_key] = dataItem
                    list_key = dataItem["triggers"]
                    for changeTarge_key in list_key:
                        list_ruleId = self.dict_changeTarget.get(changeTarge_key, [])
                        if message_key not in list_ruleId:
                            list_ruleId.append(message_key)
                            self.dict_changeTarget[changeTarge_key] = list_ruleId

    def handle_rules_dir(self, dir_module, root_dir_name):
        dir_rules = os.path.join(Constant.EXE_RUN_PATH, f"rules_{root_dir_name}")
        if not os.path.exists(dir_rules):
            os.mkdir(dir_rules)
        file_name = f"{self.moduleName}Messages.json"
        file_json_inner = os.path.join(dir_module, file_name)
        file_json_outer = os.path.join(dir_rules, file_name)
        if not os.path.exists(file_json_outer):
            shutil.copy2(file_json_inner, file_json_outer)
        return file_json_outer

    def validateArxml(self, changeTargetDefPath: str):
        moduleName = self.moduleName
        fileName = f"{moduleName}.arxml"
        logger.info("[%s]: Start to validate arxml file:'%s'" % (moduleName, fileName))
        PM.start(fileName, f"{moduleName}_validatingfile")
        try:
            output = self.runRules(changeTargetDefPath)
        except Exception as e:
            try:
                logger.error("[%s]: Failed to validate arxml file(%s):%s" % (moduleName, fileName, traceback.format_exc()))
            finally:
                e = None
                del e

        else:
            PM.stop(fileName)
            logger.info("File:'%s' is validated, time consumed: %s" % (fileName, PM.getElapsed(fileName)))
        logger.info("[%s]: All Rules are executed, time consumed: %s" % (moduleName, PM.getNamespaceElapsed(f"{moduleName}_validatingfile")))

    def runRules(self, changeTargetDefPath: str):
        return

    def execute_method(self, ruleObject, changeTargetDefPath: str):
        """
        只执行Rule_开头的方法，如果有传入变化的目标def地址则只找指定的校验规则
        """
        for name, method in inspect.getmembers(ruleObject, predicate=(inspect.ismethod)):
            if not name.startswith("Rule_") or changeTargetDefPath is None or name in self.dict_changeTarget.get(changeTargetDefPath, []):
                method()
