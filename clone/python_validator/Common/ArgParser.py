# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\ArgParser.py
import argparse, os.path
from Common.Utils import singletonFunc

@singletonFunc
class ArgParser:
    inputProject = ""
    listModule = []
    isDebugMode = False
    target = None
    outputPath = "output"
    listVP = []
    curVP = "None"

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--input", type=str, help="folder name of input project", required=True)
        parser.add_argument("-m", "--module", type=str, help="module name list of validate target", required=False)
        parser.add_argument("-d", "--debug", help="debug", action="store_true", required=False)
        parser.add_argument("-t", "--target", type=str, help="def path of changed config item", required=False)
        parser.add_argument("-o", "--output", type=str, help="output path", required=False)
        parser.add_argument("-vp", "--variantPoint", type=str, help="variant point", required=False)
        args = parser.parse_args()
        if args.input:
            self.inputProject = args.input.strip()
        elif args.module:
            self.listModule.extend(args.module.split(","))
        if args.debug:
            self.isDebugMode = True
        if args.target:
            self.target = args.target
        if args.output:
            self.outputPath = args.output.strip()
        if args.variantPoint:
            self.listVP.extend(args.variantPoint.split(","))
        else:
            self.listVP = [
             None]

    def __str__(self):
        toString = "ArgParser Info:\n"
        toString += f"  inputProject = [{self.inputProject}]\n"
        toString += f"  listModule   = [{self.listModule}]\n"
        toString += f"  isDebugMode  = [{self.isDebugMode}]\n"
        toString += f"  target       = [{self.target}]\n"
        toString += f"  outputPath   = [{self.outputPath}]\n"
        toString += f"  listVP       = [{self.listVP}]"
        return toString

    def checkSelf(self, logger):
        """
        检查参数是否符合要求
        """
        logger.info("Checking Parameters Start")
        logger.info(self.__str__())
        msgEnd = "Checking Parameters End -> "
        if os.path.exists(self.inputProject):
            logger.info(f"{msgEnd}Parameters OK")
            return True
        logger.error(f"{msgEnd}Please check input parameters")
        return False

    def isAllModule(self):
        """
        判断是否校验输入工程里的全部模块
        """
        return len(self.listModule) == 0

    def isTimeMode(self):
        """
        判断是否开启实时校验模式
        """
        return self.target is not None


RunArgParser = ArgParser()
