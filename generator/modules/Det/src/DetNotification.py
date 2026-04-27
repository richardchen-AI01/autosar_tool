from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP

class DetNotification(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def DetErrorHook(self):
        return self.getAttrValue(BP.Det_DetErrorHook)

    @property
    def DetReportRuntimeErrorCallout(self):
        return self.getAttrValue(BP.Det_DetReportRuntimeErrorCallout)

    @property
    def DetReportTransientFaultCallout(self):
        return self.getAttrValue(BP.Det_DetReportTransientFaultCallout)
