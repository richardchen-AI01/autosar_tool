from Common.BswBase import BswBase
from Common.Public import getSwitchValue,getApplicationIdByPartition
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from NvM.src import NvMBlockDescriptor

class NvMCommon(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def NvMApiConfigClass(self):
        temp = self.getAttrValue(BP.NvM_NvMApiConfigClass)
        return self.getAttrValue(BP.NvM_NvMApiConfigClass)

    @property
    def NvMMultiBlockCallback(self):
        return self.getAttrValue(BP.NvM_NvMMultiBlockCallback)

    @property
    def NvMBswMMultiBlockJobStatusInformation(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMBswMMultiBlockJobStatusInformation))

    @property
    def NvMCompiledConfigId(self):
        return hex(int(self.getAttrValue(BP.NvM_NvMCompiledConfigId)))

    @property
    def NvMCrcNumOfBytes(self):
        return hex(int(self.getAttrValue(BP.NvM_NvMCrcNumOfBytes)))

    @property
    def NvMDatasetSelectionBits(self):
        NvMBlockDescriptor.public_NvMDatasetSelectionBits = int(self.getAttrValue(BP.NvM_NvMDatasetSelectionBits))
        return hex(NvMBlockDescriptor.public_NvMDatasetSelectionBits)

    @property
    def NvMDevErrorDetect(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMDevErrorDetect))

    @property
    def NvMDrvModeSwitch(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMDrvModeSwitch))

    @property
    def NvMDynamicConfiguration(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMDynamicConfiguration))

    @property
    def NvMJobPrioritization(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMJobPrioritization))

    @property
    def NvMPollingMode(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMPollingMode))

    @property
    def NvMSetRamBlockStatusApi(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMSetRamBlockStatusApi))

    @property
    def NvMVersionInfoApi(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMVersionInfoApi))

    @property
    def NvMMainFunctionPeriod(self):
        return float(self.getAttrValue(BP.NvM_NvMMainFunctionPeriod))

    @property
    def NvMRepeatMirrorOperations(self):
        result = self.getAttrValue(BP.NvM_NvMRepeatMirrorOperations)
        if result:
            return hex(int(result))
        else:
            return 0

    @property
    def NvMSizeImmediateJobQueue(self):
        result = self.getAttrValue(BP.NvM_NvMSizeImmediateJobQueue)
        if result:
            return hex(int(result))
        else:
            return 0

    @property
    def NvMSizeStandardJobQueue(self):
        result = self.getAttrValue(BP.NvM_NvMSizeStandardJobQueue)
        if result:
            return hex(int(result))
        else:
            return 0

    @property
    def NvMCsmRetryCounter(self):
        return self.getAttrValue(BP.NvM_NvMCsmRetryCounter) if self.getAttrValue(BP.NvM_NvMCsmRetryCounter) else 0

    @property
    def NvMMasterEcucPartitionRef(self):
        return self.getAttrValue(BP.NvM_NvMMasterEcucPartitionRef)

    @property
    def NvMMasterEcucPartitionId(self):
        return getApplicationIdByPartition(self.getAttrValue(BP.NvM_NvMMasterEcucPartitionRef))

    @property
    def NvMEcucPartitionRef(self):
        result = 0
        for partition in self.getAttrValue(BP.NvM_NvMEcucPartitionRef):
            if partition:
                result = result + 1
        return result