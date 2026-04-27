from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Ea.src.EaGeneral import *
from Ea.src.EaBlockConfiguration import *
from Ea.src.EaPublishedInformation import *
import uuid

class EaEepApi(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def EepReadApi(self):
        temp = self.getAttrValue(BP.Ea_EepReadApi)
        return temp

    @property
    def EepWriteApi(self):
        temp = self.getAttrValue(BP.Ea_EepWriteApi)
        return temp

    @property
    def EepEraseApi(self):
        temp = self.getAttrValue(BP.Ea_EepEraseApi)
        return temp

    @property
    def EepCancelApi(self):
        temp = self.getAttrValue(BP.Ea_EepCancelApi)
        return temp

    @property
    def EepGetStatusApi(self):
        temp = self.getAttrValue(BP.Ea_EepGetStatusApi)
        return temp

    @property
    def EepGetJobResultApi(self):
        temp = self.getAttrValue(BP.Ea_EepGetJobResultApi)
        return temp

    @property
    def EaEepDeviceRef(self):
        temp = self.getAttrValue(BP.Ea_EaEepDeviceRef)
        return temp
