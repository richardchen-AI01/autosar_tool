def getModuleContext(inputProject):
    """
    - description:返回模块数据
    """
    from Det.base.DetContext import DetContext
    return DetContext(inputProject)

def getModuleCodeGenerator():
    """
    - description:返回模块代码生成器
    """
    from  Det.base.DetCodeGenerator import DetCodeGenerator
    return DetCodeGenerator()