from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP

class DetModule(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def DetModuleId(self):
        return self.getAttrValue(BP.Det_DetModuleId)

    @property
    def DetModuleInstance(self):
        temp = self.getSubContainer('DetModuleInstance')
        return [DetModuleInstance(detModuleInstance) for detModuleInstance in temp] if temp else None

class DetModuleInstance(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def DetInstanceId(self):
        return self.getAttrValue(BP.Det_DetInstanceId)
