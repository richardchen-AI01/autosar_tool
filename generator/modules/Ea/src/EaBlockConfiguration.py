from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.Public import getBooleanValue
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from operator import attrgetter

EaEepApiArray = []
EaEepAddrOffsetArray = []

class EaBlockConfiguration(BswBase):
    def __init__(self, Container):
        super().__init__(Container)

    @property
    def EaStartAddress(self):
        addr = None
        index = self.EaDeviceIndex
        eepref = getBswContainerByEnum(BP.Eep_62_EepInitConfiguration)
        for EepInitConfiguration in eepref:
            tempdev = EepInitConfiguration.getParentContainer()
            if (tempdev.shortName_ == EaEepApiArray[index]):
                if (EaEepAddrOffsetArray[index] == 0):
                    addr = EepInitConfiguration.getAttrValue(BP.Eep_62_EepBaseAddress)
                    EaEepAddrOffsetArray[index] += self.EaBlockSize
                    break
                else:
                    Baseaddr = int(EepInitConfiguration.getAttrValue(BP.Eep_62_EepBaseAddress))
                    addr = Baseaddr + EaEepAddrOffsetArray[index]
                    EaEepAddrOffsetArray[index] += self.EaBlockSize
        return addr

    @property
    def EaBlockNumber(self):
        return hex(int(self.getAttrValue(BP.Ea_EaBlockNumber)))

    @property
    def EaBlockSize(self):
        result = int(self.getAttrValue(BP.Ea_EaBlockSize))
        return result + 14

    @property
    def EaImmediateData(self):
        return getBooleanValue(self.getAttrValue(BP.Ea_EaImmediateData))

    @property
    def EaNumberOfWriteCycles(self):
        return self.getAttrValue(BP.Ea_EaNumberOfWriteCycles)

    @property
    def EaDeviceIndex(self):
        result = None
        index = 0
        temp = self.getAttrValue(BP.Ea_EaDeviceIndex)
        for name in EaEepApiArray:
            if (temp.shortName_ == name):
                result = index
                break
            else:
                index += 1
        return result

    @property
    def EaMemAccAddressArea(self):
        return self.getAttrValue(BP.Ea_EaMemAccAddressArea)
