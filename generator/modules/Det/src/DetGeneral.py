from Common.BswBase import BswBase
from Common.Public import getSwitchValue
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP

class DetGeneral(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def DetForwardToDlt(self):
        return getSwitchValue(self.getAttrValue(BP.Det_DetForwardToDlt))

    @property
    def DetVersionInfoApi(self):
        return getSwitchValue(self.getAttrValue(BP.Det_DetVersionInfoApi))

    @property
    def DetRamLogBufferSize(self):
        return self.getAttrValue(BP.Det_DetRamLogBufferSize)

    @property
    def DetHeaderFile(self):
        return self.getAttrValue(BP.Det_DetHeaderFile)
