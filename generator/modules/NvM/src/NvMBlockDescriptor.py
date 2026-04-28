from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.Public import getSwitchValue,getApplicationIdByPartition
import re

public_NvMDatasetSelectionBits = 0
public_NvMCipherName = []

class NvMBlockDescriptor(BswBase):
    __Header = None
    __IncludeHeader = []

    def __init__(self, Container):
        super().__init__(Container)

    @property
    def NvMBswMBlockStatusInformation(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMBswMBlockStatusInformation))

    @property
    def NvMBlockUseCrc(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMBlockUseCrc))

    @property
    def NvMRamBlockDataBufferAutoFillEabled(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMRamBlockDataBufferAutoFill))

    @property
    def NvMBlockUseSyncMechanism(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMBlockUseSyncMechanism))
 
    def get_numbers_after(self, s, symbol):
        pattern = f"{symbol}(1000|[1-9]?[0-9]?)"
        match = re.search(pattern, s)
        return match.group(1) if match else None
    
    def remove_symbol_after(self, s, symbol):
        parts = s.split(symbol, 1)
        return parts[0] if len(parts) > 1 else s

    @property
    def NvMRamBlockDataAddress(self):
        value = self.getAttrValue(BP.NvM_NvMRamBlockDataAddress)
        if value == 'DemEventRelateInformationStorage' or value == 'DemOBDDataStorage':
            return '&' + value
        else:
            symbol = '_'
            new_value = self.remove_symbol_after(value, symbol)
            if new_value == 'DemPrimaryMemory' or new_value == 'DemPermanentMemory':
                index = self.get_numbers_after(value, symbol)
                return '&' + new_value + '[' + str(index) + ']'
            else:
                return value

    @property
    def NvMRomBlockDataAddress(self):
        return self.getAttrValue(BP.NvM_NvMRomBlockDataAddress)

    @property
    def NvMNvBlockLength(self):
        return int(self.getAttrValue(BP.NvM_NvMNvBlockLength))

    @property
    def NvMWriteVerificationDataSize(self):
        return int(self.getAttrValue(BP.NvM_NvMWriteVerificationDataSize))

    @property
    def NvMBlockJobPriority(self):
        return int(self.getAttrValue(BP.NvM_NvMBlockJobPriority))

    @property
    def NvMNvramDeviceId(self):
        return int(self.getAttrValue(BP.NvM_NvMNvramDeviceId))

    @property
    def NvMRomBlockNum(self):
        return int(self.getAttrValue(BP.NvM_NvMRomBlockNum))

    @property
    def NvMMaxNumOfWriteRetries(self):
        return int(self.getAttrValue(BP.NvM_NvMMaxNumOfWriteRetries))

    @property
    def NvMMaxNumOfReadRetries(self):
        return int(self.getAttrValue(BP.NvM_NvMMaxNumOfReadRetries))

    @property
    def NvMBlockManagementType(self):
        return self.getAttrValue(BP.NvM_NvMBlockManagementType)

    @property
    def NvMBlockCrcType(self):
        return self.getAttrValue(BP.NvM_NvMBlockCrcType)

    @property
    def NvMNvBlockBaseNumber(self):
        # get blocknumber
        result = 0
        temp = 0
        if self.getSubContainer('NvMTargetBlockReference'):
            if self.getSubContainer('NvMTargetBlockReference')[0].getSubContainer('NvMFeeRef'):
                temp = self.getSubContainer('NvMTargetBlockReference')[0].getSubContainer('NvMFeeRef')[0].getAttrValue(BP.NvM_NvMNameOfFeeBlock)
                if(temp.getParentContainer().shortName_ == 'Fee_62'):
                    temp = int(temp.getAttrValue(BP.Fee_62_FeeBlockNumber))
                else:
                    temp = int(temp.getAttrValue(BP.Fee_FeeBlockNumber))
            else:
                if self.getSubContainer('NvMTargetBlockReference')[0].getSubContainer('NvMEaRef'):
                    temp = self.getSubContainer('NvMTargetBlockReference')[0].getSubContainer('NvMEaRef')[0].getAttrValue(BP.NvM_NvMNameOfEaBlock)
                    temp = int(temp.getAttrValue(BP.Ea_EaBlockNumber))
        # caculate basebumber according to selectbit
        result = temp >> public_NvMDatasetSelectionBits
        return result

    @property
    def NvMNvBlockNum(self):
        result = 2 if self.NvMBlockManagementType == 'NVM_BLOCK_REDUNDANT' else 1
        if self.NvMBlockManagementType == 'NVM_BLOCK_DATASET':
            result = int(self.getAttrValue(BP.NvM_NvMNvBlockNum))
        return result
    
    @property
    def NvMBlockHeaderInclude(self):
        value = self.getAttrValue(BP.NvM_NvMBlockHeaderInclude)
        if value:
            if value in self.__IncludeHeader:
                if self.__Header is None:
                    return None
                else:
                    self.__Header = None
            else:
                self.__IncludeHeader.append(value)
                self.__Header = value
        return value

    @property
    def NvMNvramBlockIdentifier(self):
        return self.getAttrValue(BP.NvM_NvMNvramBlockIdentifier)

    @property
    def NvMBlockUsePort(self):
        return getSwitchValue(self.getAttrValue(BP.NvM_NvMBlockUsePort))

    @property
    def NvMInitBlockCallback(self):
        return self.getSubContainer('NvMInitBlockCallback')

    @property
    def NvMInitBlockCallbackFnc(self):
        result = None
        if self.NvMRomBlockDataAddress is None and self.NvMInitBlockCallback:
            result = self.NvMInitBlockCallback[0].getAttrValue(BP.NvM_NvMInitBlockCallbackFnc)
        return result

    @property
    def NvMSingleBlockCallback(self):
        return self.getSubContainer('NvMSingleBlockCallback')

    @property
    def NvMSingleBlockCallbackFnc(self):
        result = None
        if self.NvMSingleBlockCallback:
            result = self.NvMSingleBlockCallback[0].getAttrValue(BP.NvM_NvMSingleBlockCallbackFnc)
        return result

    @property
    def NvMReadRamBlockFromNvCallback(self):
        result = self.getAttrValue(BP.NvM_NvMReadRamBlockFromNvCallback)
        return result if result else 'NULL_PTR' 

    @property
    def NvMWriteRamBlockToNvCallback(self):
        result = self.getAttrValue(BP.NvM_NvMWriteRamBlockToNvCallback)
        return result if result else 'NULL_PTR' 

    @property
    def NvMBlockFlagGroup(self):
        result = 0
        # bit14
        if self.getAttrValue(BP.NvM_NvMBlockUseCompression) == 'true':
            result = result + 1
        result = result << 1
        # bit13
        if self.getAttrValue(BP.NvM_NvMSelectBlockForFirstInitAll) == 'true':
            result = result + 1
        result = result << 1
        # bit12
        if self.getAttrValue(BP.NvM_NvMBswMBlockStatusInformation) == 'true':
            result = result + 1
        result = result << 1
        # bit11
        if self.getAttrValue(BP.NvM_NvMBlockUseSyncMechanism) == 'true':
            result = result + 1
        result = result << 1
        # bit10
        if self.getAttrValue(BP.NvM_NvMBlockUseSetRamBlockStatus) == 'true':
            result = result + 1
        result = result << 1
        # bit9
        if self.getAttrValue(BP.NvM_NvMBlockUseCRCCompMechanism) == 'true':
            result = result + 1
        result = result << 1
        # bit8
        if self.getAttrValue(BP.NvM_NvMBlockUseAutoValidation) == 'true':
            result = result + 1
        result = result << 1
        # bit7
        if self.getAttrValue(BP.NvM_NvMWriteVerification) == 'true':
            result = result + 1
        result = result << 1
        # bit6
        if self.getAttrValue(BP.NvM_NvMStaticBlockIDCheck) == 'true':
            result = result + 1
        result = result << 1
        # bit5
        if self.getAttrValue(BP.NvM_NvMSelectBlockForWriteAll) == 'true':
            result = result + 1
        result = result << 1
        # bit4
        if self.getAttrValue(BP.NvM_NvMSelectBlockForReadAll) == 'true':
            result = result + 1
        result = result << 1
        # bit3
        if self.getAttrValue(BP.NvM_NvMResistantToChangedSw) == 'true':
            result = result + 1
        result = result << 1
        # bit2
        if self.getAttrValue(BP.NvM_NvMCalcRamBlockCrc) == 'true':
            result = result + 1
        result = result << 1
        # bit1
        if self.getAttrValue(BP.NvM_NvMBlockWriteProt) == 'true':
            result = result + 1
        result = result << 1
        # bit0
        if self.getAttrValue(BP.NvM_NvMWriteBlockOnce) == 'true':
            result = result + 1
        return hex(result)

    @property
    def NvMBlockCipheringRef(self):
        result = self.getAttrValue(BP.NvM_NvMBlockCipheringRef)
        if result:
            for index in range(len(public_NvMCipherName)):
                if result.shortName_ == public_NvMCipherName[index]:
                    return '&' + 'NvMBlockCiphering' + '[' + str(index) + ']'
        else:
            return 'NULL_PTR'

    @property
    def NvMBlockEcucPartitionId(self):
        return getApplicationIdByPartition(self.getAttrValue(BP.NvM_NvMBlockEcucPartitionRef))

    @property
    def NvMBlockUseCompression(self):
        return self.getAttrValue(BP.NvM_NvMBlockUseCompression)

    @property
    def NvMWriteVerification(self):
        return self.getAttrValue(BP.NvM_NvMWriteVerification)

    @property
    def NvMStaticBlockIDCheck(self):
        return self.getAttrValue(BP.NvM_NvMStaticBlockIDCheck)

    @property
    def NvMDataSetTypeNvNum(self):
        return self.NvMNvBlockNum + self.NvMRomBlockNum
