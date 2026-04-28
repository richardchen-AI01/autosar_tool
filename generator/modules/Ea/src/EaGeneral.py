from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.Public import getSwitchValue
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum

class EaGeneral(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def EaDevErrorDetect(self):
        return getSwitchValue(self.getAttrValue(BP.Ea_EaDevErrorDetect))

    @property
    def EaVersionInfoApi(self):
        return getSwitchValue(self.getAttrValue(BP.Ea_EaVersionInfoApi))

    @property
    def EaPollingMode(self):
        return getSwitchValue(self.getAttrValue(BP.Ea_EaPollingMode))

    @property
    def EaVirtualPageSize(self):
        return self.getAttrValue(BP.Ea_EaVirtualPageSize)

    @property
    def EaMainFunctionPeriod(self):
        return float(self.getAttrValue(BP.Ea_EaMainFunctionPeriod))

    @property
    def EaNvmJobEndNotification(self):
        return self.getAttrValue(BP.Ea_EaNvmJobEndNotification)

    @property
    def EaNvmJobErrorNotification(self):
        return self.getAttrValue(BP.Ea_EaNvmJobErrorNotification)

    @property
    def EaHeaderFile(self):
        return self.getAttrValue(BP.Ea_EaHeaderFile)

    @property
    def EaMinimumReadPageSize(self):
        return int(self.getAttrValue(BP.Ea_EaMinimumReadPageSize))

    @property
    def EaBufferAlignmentValue(self):
        return self.getAttrValue(BP.Ea_EaBufferAlignmentValue) if self.getAttrValue(BP.Ea_EaBufferAlignmentValue) else 0
