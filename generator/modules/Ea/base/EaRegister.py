def getModuleContext(inputProject):
    """
    - description:返回模块数据
    """
    from Ea.base.EaContext import EaContext
    return EaContext(inputProject)

def getModuleCodeGenerator():
    """
    - description:返回模块代码生成器
    """
    from  Ea.base.EaCodeGenerator import EaCodeGenerator
    return EaCodeGenerator()