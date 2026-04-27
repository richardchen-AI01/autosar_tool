from Common.Context import ModuleContextBase
from MemIf.src.MemIf import MemIf

class MemIfContext(ModuleContextBase):
    def __init__(self, inputName) -> None:
        pass

    def postLoadArtopCache(self):
        self.MemIf = MemIf()
