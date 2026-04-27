def getModuleContext(inputProject):
    """
    - description:返回模块数据
    """
    from MemIf.base.MemIfContext import MemIfContext
    return MemIfContext(inputProject)

def getModuleCodeGenerator():
    """
    - description:返回模块代码生成器
    """
    from  MemIf.base.MemIfCodeGenerator import MemIfCodeGenerator
    return MemIfCodeGenerator()