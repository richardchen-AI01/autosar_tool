from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Common.Public import getSwitchValue

class MemIfGeneral(BswBase):

    def __init__(self, Container):
        super().__init__(Container)
        
    @property
    def MemIfDevErrorDetect(self):
        return getSwitchValue(self.getAttrValue(BP.MemIf_MemIfDevErrorDetect))
    
    @property
    def MemIfNumberOfDevices(self):
        return int(self.getAttrValue(BP.MemIf_MemIfNumberOfDevices))
    
    @property
    def MemIfVersionInfoApi(self):
        return getSwitchValue(self.getAttrValue(BP.MemIf_MemIfVersionInfoApi))
    

    
class MemIf:
    
    def __init__(self):
        tempMemIfGeneral = getBswContainerByEnum(BP.MemIf_MemIfGeneral)
        self.MemIfGeneral = MemIfGeneral(tempMemIfGeneral[0]) if tempMemIfGeneral else None
    
    @property
    def checkFee(self):
        for NvMBlockDescriptor in getBswContainerByEnum(BP.NvM_NvMBlockDescriptor):
            NvMTargetBlockReference = NvMBlockDescriptor.getSubContainer('NvMTargetBlockReference')
            NvMFeeRef = NvMTargetBlockReference[0].getSubContainer('NvMFeeRef')
            if NvMFeeRef:
                return True
        return False
    
    @property
    def checkEa(self):
        for NvMBlockDescriptor in getBswContainerByEnum(BP.NvM_NvMBlockDescriptor):
            NvMTargetBlockReference = NvMBlockDescriptor.getSubContainer('NvMTargetBlockReference')
            NvMEaRef = NvMTargetBlockReference[0].getSubContainer('NvMEaRef')
            if NvMEaRef:
                return True
        return False
    
    
    
    
    
    