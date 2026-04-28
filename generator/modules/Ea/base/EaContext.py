from Common.Context import ModuleContextBase
from Ea.src.Ea import Ea

class EaContext(ModuleContextBase):
    def __init__(self, inputName) -> None:
        pass

    def postLoadArtopCache(self):
        self.Ea = Ea()
