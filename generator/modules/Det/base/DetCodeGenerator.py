from Common.CodeGenerator import CodeGenerator

class DetCodeGenerator(CodeGenerator):
    def __init__(self) -> None:
        super().__init__()

    def generateCode(self):
        #调用基类generateCode函数
        incFileList = ['Det_Externals.c']
        super().generateCode(incFileList)