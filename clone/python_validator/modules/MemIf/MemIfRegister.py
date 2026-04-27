import os.path

from Bsw.MemIf.MemIfRules import *
from Common.ArxmlValidator import ArxmlValidator


class MemIfArxmlValidator(ArxmlValidator):

    def __init__(self) -> None:
        super().__init__()
        dir_module = os.path.dirname(os.path.abspath(__file__))
        super().createMessageData(dir_module)

    def runRules(self, changeTargetDefPath: str):
        ruleR23 = RuleBSWMemIfR23()
        super().execute_method(ruleR23, changeTargetDefPath)
        pass


def getModuleArxmlValidator():
    """
    - description:返回模块arxml文件校验器
    """
    return MemIfArxmlValidator()
