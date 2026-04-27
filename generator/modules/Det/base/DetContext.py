from Common.Context import ModuleContextBase
from Det.src.Det import Det

class DetContext(ModuleContextBase):
    def __init__(self, inputName) -> None:
        pass

    def postLoadArtopCache(self):
        self.Det = Det()
