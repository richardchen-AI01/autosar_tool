from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from Ea.src.EaGeneral import *
from Ea.src.EaEepApi import *
from Ea.src.EaBlockConfiguration import *
from Ea.src.EaPublishedInformation import *
import uuid

class Ea:
    def __init__(self):
        tempEaGeneral = getBswContainerByEnum(BP.Ea_EaGeneral)
        self.EaGeneral=  EaGeneral(tempEaGeneral[0]) if tempEaGeneral else None

        tempEaBlockConfiguration = getBswContainerByEnum(BP.Ea_EaBlockConfiguration)
        self.EaBlockConfiguration = [EaBlockConfiguration(blockconfiguration) for blockconfiguration in tempEaBlockConfiguration] if tempEaBlockConfiguration else []

        tempEaEepApi = getBswContainerByEnum(BP.Ea_Ea_EepApi)
        self.EaEepApi = [EaEepApi(EaEepApiIdx) for EaEepApiIdx in tempEaEepApi] if tempEaEepApi else []
        for EaEepApiIndex in self.EaEepApi:
            EaEepApiArray.append(EaEepApiIndex.EaEepDeviceRef.shortName_)
            EaEepAddrOffsetArray.append(0)

        tempEaPublishedInformation = getBswContainerByEnum(BP.Ea_EaPublishedInformation)
        self.EaPublishedInformation = EaPublishedInformation(tempEaPublishedInformation[0]) if tempEaPublishedInformation else None

    @property
    def EaBlockNumber(self):
        return len(self.EaBlockConfiguration)

    @property
    def EaEepDeviceNumber(self):
        return len(self.EaEepApi)

    @property
    def maxEaBlockSize(self):
        maxBlockSize = 0
        for configuration in self.EaBlockConfiguration:
            maxBlockSize = max(maxBlockSize,int(configuration.EaBlockSize))
        return maxBlockSize - 14

    # @property
    # def EaGetuuid(self):
    #     return uuid.uuid4()