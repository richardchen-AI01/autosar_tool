from Common.BswBase import BswBase
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP

def getCsmJobRef(job):
    csmjobid = getBswContainerByEnum(BP.Csm_CsmJobs)
    for csmref in csmjobid:
        temp = csmref.getSubContainer('CsmJob')
        for result in temp:
            if result.shortName_ == job.shortName_:
                result = result.getAttrValue(BP.Csm_CsmJobId)
                return result
    return None

class NvMBlockCiphering(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def NvMNvBlockNVRAMDataLength(self):
        return int(self.getAttrValue(BP.NvM_NvMNvBlockNVRAMDataLength))

    @property
    def NvMCsmDecryptionJobReference(self):
        temp = self.getAttrValue(BP.NvM_NvMCsmDecryptionJobReference)
        return getCsmJobRef(temp)
    

    @property
    def NvMCsmEncryptionJobReference(self):
        temp = self.getAttrValue(BP.NvM_NvMCsmEncryptionJobReference)
        return getCsmJobRef(temp)
    

