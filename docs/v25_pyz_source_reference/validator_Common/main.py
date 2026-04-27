# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\main.py
import os, sys, traceback
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from Common import Constant
from Common import Public
from Common import logger
from Common.utils.JsonUtil import genJsonResultFile
from Common.PerformanceMonitor import PM
from Common.ArgParser import RunArgParser
from Common.arxmlparse.artop import all_objects

def checkValidateModules():
    """
    检查输入的模块参数中是否有对应的校验器
    """
    for module in RunArgParser.listModule:
        path = os.path.join(Constant.PROJ_ROOT, "Bsw", module)
        if not os.path.exists(path):
            logger.error("[%s] Failed to find module: %s" % (module, path))
            return             return False
        return True


def loadModules():
    modules = []
    from Common import Utils
    for module in RunArgParser.listModule:
        fileName = f"{module}Register.py"
        filePath = os.path.join(Constant.PROJ_ROOT, "Bsw", module, fileName)
        if os.path.exists(filePath):
            modules.append((module, Utils.loadModule(fileName, filePath)))
        return modules


def registValidators(modules):
    moduleValidators = []
    for module, pModule in modules:
        try:
            moduleValidators.append((module, pModule.getModuleArxmlValidator()))
        except:
            logger.error("[%s] Failed to register moduleValidator:\n%s" % (module, traceback.format_exc()))

    else:
        return moduleValidators


def loadArtopCache(inputProject, vp=None):
    from Common.arxmlparse.cache.InitArtopCache import init_cache
    try:
        init_cache(inputProject, vp)
        if RunArgParser.isAllModule():
            list_module = all_objects.get("EcucModuleConfigurationValues", [])
            RunArgParser.listModule = [moduleObj.shortName_ for moduleObj in list_module if moduleObj.shortName_ is not None]
    except Exception as e:
        try:
            logger.critical("Failed to initialize cache from arxml:\n%s" % traceback.format_exc())
        finally:
            e = None
            del e


def main():
    logger.setupLogger()
    if not RunArgParser.checkSelf(logger):
        return
    logger.info("Validator is starting")
    if RunArgParser.isDebugMode:
        logger.debug(f"Constant.PROJ_ROOT={Constant.PROJ_ROOT}")
        logger.debug(f"Constant.COMMON_PATH={Constant.COMMON_PATH}")
        logger.debug(f"Constant.EXE_RUN_PATH={Constant.EXE_RUN_PATH}")
        for root, dirs, files in os.walk(Constant.PROJ_ROOT):
            for file in files:
                file_path = os.path.join(root, file)
                logger.debug(file_path)

        else:
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                logger.debug(dir_path)

    changeTargetDefPath = RunArgParser.target
    loadedModules = loadModules()
    listModules = []
    for moduleName, pModule in loadedModules:
        listModules.append(moduleName)
    else:
        ecuName = Public.getEcuName()
        logger.info(f"MCU Name = [{ecuName}]")
        for variantValue in RunArgParser.listVP:
            vpValue = "None" if not variantValue else variantValue
            RunArgParser.curVP = vpValue
            PM.start(f"ArxmlParse(v={vpValue})", "SV")
            loadArtopCache(RunArgParser.inputProject, variantValue)
            PM.stop(f"ArxmlParse(v={vpValue})")

        for module, moduleValidator in registValidators(loadedModules):
            try:
                moduleValidator.validateArxml(changeTargetDefPath)
            except:
                logger.error("[%s] Failed to Rule Validate:\n%s" % (module, traceback.format_exc()))

        else:
            genJsonResultFile(RunArgParser.outputPath)
            logger.info("Rule Validation is complete")
            for variantValue in RunArgParser.listVP:
                vpValue = "None" if not variantValue else variantValue
                logger.info(f"Arxml Parse (v={vpValue}), time consumed: %s" % PM.getElapsed(f"ArxmlParse(v={vpValue})"))
            else:
                logger.info("SingletonValidator ran for total: %s" % PM.getNamespaceElapsed("SV"))
                logger.countShow()


def start():
    main()
