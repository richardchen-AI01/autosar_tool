from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP


class NvMDemEventParameterRefs(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def NVM_E_HARDWARE_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_HARDWARE)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_HARDWARE(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_HARDWARE)
        return temp if temp else None

    @property
    def NVM_E_INTEGRITY_FAILED_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_INTEGRITY_FAILED)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_INTEGRITY_FAILED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_INTEGRITY_FAILED)
        return temp if temp else None

    @property
    def NVM_E_LOSS_OF_REDUNDANCY_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_LOSS_OF_REDUNDANCY)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_LOSS_OF_REDUNDANCY(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_LOSS_OF_REDUNDANCY)
        return temp if temp else None

    @property
    def NVM_E_REQ_FAILED_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_REQ_FAILED)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_REQ_FAILED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_REQ_FAILED)
        return temp if temp else None

    @property
    def NVM_E_VERIFY_FAILED_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_VERIFY_FAILED)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_VERIFY_FAILED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_VERIFY_FAILED)
        return temp if temp else None

    @property
    def NVM_E_WRITE_PROTECTED_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_WRITE_PROTECTED)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_WRITE_PROTECTED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_WRITE_PROTECTED)
        return temp if temp else None

    @property
    def NVM_E_WRONG_BLOCK_ID_EABLED(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_WRONG_BLOCK_ID)
        return 'STD_ON' if temp else 'STD_OFF'

    @property
    def NVM_E_WRONG_BLOCK_ID(self):
        temp = self.getAttrValue(BP.NvM_NVM_E_WRONG_BLOCK_ID)
        return temp if temp else None

    @property
    def NvMAnyDemEabled(self):
        temp = len(self.NVM_E_HARDWARE_EABLED + self.NVM_E_REQ_FAILED_EABLED + self.NVM_E_LOSS_OF_REDUNDANCY_EABLED + self.NVM_E_WRITE_PROTECTED_EABLED + self.NVM_E_INTEGRITY_FAILED_EABLED + self.NVM_E_WRONG_BLOCK_ID_EABLED + self.NVM_E_VERIFY_FAILED_EABLED)
        return 'STD_OFF' if temp == 49 else 'STD_ON'
