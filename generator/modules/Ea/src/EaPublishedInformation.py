from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP

class EaPublishedInformation(BswBase):
    def __init__(self,Container):
        super().__init__(Container)

    @property
    def EaBlockOverhead(self):
        return self.getAttrValue(BP.Ea_EaBlockOverhead)
    
    @property
    def EaPageOverhead(self):
        return self.getAttrValue(BP.Ea_EaPageOverhead)
    