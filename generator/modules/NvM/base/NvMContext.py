from Common.Context import ModuleContextBase
from NvM.src.NvM import NvM

class NvMContext(ModuleContextBase):
    def __init__(self, inputName) -> None:
        pass

    def postLoadArtopCache(self):
        self.NvM = NvM()
