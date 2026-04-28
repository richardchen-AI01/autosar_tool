def getModuleContext(inputProject):
    """
    - description:返回模块数据
    """
    from NvM.base.NvMContext import NvMContext
    return NvMContext(inputProject)

def getModuleCodeGenerator():
    """
    - description:返回模块代码生成器
    """
    from  NvM.base.NvMCodeGenerator import NvMCodeGenerator
    return NvMCodeGenerator()