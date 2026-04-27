from Common.CodeGenerator import CodeGenerator

class MemIfCodeGenerator(CodeGenerator):
    def __init__(self) -> None:
        super().__init__()

    def generateCode(self):
        #调用基类generateCode函数
        super().generateCode()