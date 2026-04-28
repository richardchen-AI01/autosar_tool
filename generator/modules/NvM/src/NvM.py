from Common.BswBase import BswBase
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.arxmlparse.cache.BswModuleCache import getBswContainerByEnum
from NvM.src.NvMCommon import *
from NvM.src.NvMBlockDescriptor import *
from NvM.src.NvMDemEventParameterRefs import *
from NvM.src.NvMBlockCiphering import *
from Common.Public import checkRTE
import uuid

class NvM:
    __checkRTE = None

    def __init__(self):
        tempNvMCommon = getBswContainerByEnum(BP.NvM_NvMCommon)
        self.NvMCommon = NvMCommon(tempNvMCommon[0]) if tempNvMCommon else None

        tempNvMDemEventParameterRefs = getBswContainerByEnum(BP.NvM_NvmDemEventParameterRefs)
        self.NvMDemEventParameterRefs = NvMDemEventParameterRefs(tempNvMDemEventParameterRefs[0]) if tempNvMDemEventParameterRefs else None

        tempNvMBlockDescriptor = getBswContainerByEnum(BP.NvM_NvMBlockDescriptor)
        self.NvMBlockDescriptor = [NvMBlockDescriptor(blockdescriptor) for blockdescriptor in tempNvMBlockDescriptor] if tempNvMBlockDescriptor else None

        tempNvMBlockCiphering = getBswContainerByEnum(BP.NvM_NvMBlockCiphering)
        self.NvMBlockCiphering = [NvMBlockCiphering(blockciphering) for blockciphering in tempNvMBlockCiphering] if tempNvMBlockCiphering else None
        if self.NvMBlockCiphering:
            for cipher in self.NvMBlockCiphering:
                public_NvMCipherName.append(cipher.shortName_)

    @property
    def checkRTE(self):
        if self.__checkRTE is None:
            self.__checkRTE = checkRTE('NvM')
        return self.__checkRTE

    @property
    def checkiRTE(self):
        if self.__checkRTE is False:
            swcInstances = getBswContainerByEnum(BP.iRte_RteBswModuleInstance)
            for swcInstance in swcInstances:
                BswImplementation = swcInstance.getAttrValue(BP.iRte_RteBswImplementationRef)
                if BswImplementation and ('NvM' == BswImplementation.shortName_ or 'NvM' == (BswImplementation.shortName_).split('_')[1]):
                    return True
        return False

    @property
    def NvMBswMBlockStatusInformationEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBswMBlockStatusInformation == 'STD_ON':
                    result = 'STD_ON'
        return result

    @property
    def NVM_TABLE_SIZE_PRIORITY(self):
        result = 1
        for blockdescriptor in self.NvMBlockDescriptor:
            if blockdescriptor.NvMBlockJobPriority+1 > result:
                result = blockdescriptor.NvMBlockJobPriority + 1
        return result

    @property
    def NvMMaxRedundantBlockLength(self):
        result = 0
        for blockdescriptor in self.NvMBlockDescriptor:
            if (blockdescriptor.NvMBlockManagementType == 'NVM_BLOCK_REDUNDANT') and (blockdescriptor.NvMNvBlockLength > result):
                result = blockdescriptor.NvMNvBlockLength
        return result

    @property
    def NvMRedundantBlockCount(self):
        result = 0
        for blockdescriptor in self.NvMBlockDescriptor:
            if blockdescriptor.NvMBlockManagementType == 'NVM_BLOCK_REDUNDANT':
                result = result + 1
        return result

    @property
    def NvMMaxBlockLength(self):
        result = 0
        for blockdescriptor in self.NvMBlockDescriptor:
            if blockdescriptor.NvMNvBlockLength > result:
                result = blockdescriptor.NvMNvBlockLength
        return result

    @property
    def NvMMaxBlockLengthConfigedRamMirror(self):
        result = 0
        for blockdescriptor in self.NvMBlockDescriptor:
            if blockdescriptor.NvMNvBlockLength > result and blockdescriptor.NvMBlockUseSyncMechanism == 'STD_ON':
                result = blockdescriptor.NvMNvBlockLength
        return result

    @property
    def NvMRamBlockDataBufferAutoFillUsed(self):
        result = False
        for blockdescriptor in self.NvMBlockDescriptor:
            if blockdescriptor.NvMRamBlockDataBufferAutoFillEabled == 'STD_ON':
                result = True
        return result

    @property
    def NvMBlockUseCrcEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockUseCrc == 'STD_ON':
                    result = 'STD_ON'
        return result

    @property
    def NvMBlockCRC8Eabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockCrcType == 'NVM_CRC8':
                    result = 'STD_ON'
        return result

    @property
    def NvMBlockCRC16Eabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockCrcType == 'NVM_CRC16':
                    result = 'STD_ON'
        return result

    @property
    def NvMBlockCRC32Eabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockCrcType == 'NVM_CRC32':
                    result = 'STD_ON'
        return result

    @property
    def NvMDemEventNumber(self):
        return self.NvMDemEventParameterRefs

    @property
    def NvMBlockCipheringNumber(self):
        return self.NvMBlockCiphering
    
    @property
    def NvMBlockCipheringMaxLength(self):
        length = 0
        for blockCiphering in self.NvMBlockCiphering:
            if blockCiphering.NvMNvBlockNVRAMDataLength > length:
                length = blockCiphering.NvMNvBlockNVRAMDataLength
        return length

    @property
    def NvMBlockCipheringEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockCipheringRef != 'NULL_PTR':
                    result = 'STD_ON'
        return result

    @property
    def NvMBlocCompressionEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMBlockUseCompression == 'true':
                    result = 'STD_ON'
        return result

    @property
    def NvMWriteVerificationEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMWriteVerification == 'true':
                    result = 'STD_ON'
                    break
        return result

    @property
    def NvMStaticBlockIDCheckEabled(self):
        result = 'STD_OFF'
        if self.NvMBlockDescriptor:
            for blockdescriptor in self.NvMBlockDescriptor:
                if blockdescriptor.NvMStaticBlockIDCheck == 'true':
                    result = 'STD_ON'
                    break
        return result

    @property
    def NvMGetuuid(self):
        return uuid.uuid4()
