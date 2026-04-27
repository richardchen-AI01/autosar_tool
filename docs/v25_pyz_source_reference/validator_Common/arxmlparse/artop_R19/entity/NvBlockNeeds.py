# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NvBlockNeeds.py
from .ServiceNeeds import ServiceNeeds

class NvBlockNeeds(ServiceNeeds):

    def __init__(self):
        super().__init__()
        from .NvBlockDescriptor import NvBlockDescriptor
        self._artop_calcRamBlockCrc = None
        self._artop_checkStaticBlockId = None
        self._artop_cyclicWritingPeriod = None
        self._artop_nDataSets = None
        self._artop_nRomBlocks = None
        self._artop_ramBlockStatusControl = None
        self._artop_readonly = None
        self._artop_reliability = None
        self._artop_resistantToChangedSw = None
        self._artop_restoreAtStart = None
        self._artop_selectBlockForFirstInitAll = None
        self._artop_storeAtShutdown = None
        self._artop_storeCyclic = None
        self._artop_storeEmergency = None
        self._artop_storeImmediate = None
        self._artop_useAutoValidationAtShutDown = None
        self._artop_useCrcCompMechanism = None
        self._artop_writeOnlyOnce = None
        self._artop_writeVerification = None
        self._artop_writingFrequency = None
        self._artop_writingPriority = None
        self._artop_nvBlockDescriptor = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_nvBlockDescriptor": "NV-BLOCK-DESCRIPTOR"})

    @property
    def calcRamBlockCrc_(self):
        if self._artop_calcRamBlockCrc:
            if self._artop_calcRamBlockCrc == "true":
                return True
            return False
        else:
            return self._artop_calcRamBlockCrc

    @property
    def checkStaticBlockId_(self):
        if self._artop_checkStaticBlockId:
            if self._artop_checkStaticBlockId == "true":
                return True
            return False
        else:
            return self._artop_checkStaticBlockId

    @property
    def cyclicWritingPeriod_(self):
        return self._artop_cyclicWritingPeriod

    @property
    def nDataSets_(self):
        return self._artop_nDataSets

    @property
    def nRomBlocks_(self):
        return self._artop_nRomBlocks

    @property
    def ramBlockStatusControl_(self):
        return self._artop_ramBlockStatusControl

    @property
    def readonly_(self):
        if self._artop_readonly:
            if self._artop_readonly == "true":
                return True
            return False
        else:
            return self._artop_readonly

    @property
    def reliability_(self):
        return self._artop_reliability

    @property
    def resistantToChangedSw_(self):
        if self._artop_resistantToChangedSw:
            if self._artop_resistantToChangedSw == "true":
                return True
            return False
        else:
            return self._artop_resistantToChangedSw

    @property
    def restoreAtStart_(self):
        if self._artop_restoreAtStart:
            if self._artop_restoreAtStart == "true":
                return True
            return False
        else:
            return self._artop_restoreAtStart

    @property
    def selectBlockForFirstInitAll_(self):
        if self._artop_selectBlockForFirstInitAll:
            if self._artop_selectBlockForFirstInitAll == "true":
                return True
            return False
        else:
            return self._artop_selectBlockForFirstInitAll

    @property
    def storeAtShutdown_(self):
        if self._artop_storeAtShutdown:
            if self._artop_storeAtShutdown == "true":
                return True
            return False
        else:
            return self._artop_storeAtShutdown

    @property
    def storeCyclic_(self):
        if self._artop_storeCyclic:
            if self._artop_storeCyclic == "true":
                return True
            return False
        else:
            return self._artop_storeCyclic

    @property
    def storeEmergency_(self):
        if self._artop_storeEmergency:
            if self._artop_storeEmergency == "true":
                return True
            return False
        else:
            return self._artop_storeEmergency

    @property
    def storeImmediate_(self):
        if self._artop_storeImmediate:
            if self._artop_storeImmediate == "true":
                return True
            return False
        else:
            return self._artop_storeImmediate

    @property
    def useAutoValidationAtShutDown_(self):
        if self._artop_useAutoValidationAtShutDown:
            if self._artop_useAutoValidationAtShutDown == "true":
                return True
            return False
        else:
            return self._artop_useAutoValidationAtShutDown

    @property
    def useCrcCompMechanism_(self):
        if self._artop_useCrcCompMechanism:
            if self._artop_useCrcCompMechanism == "true":
                return True
            return False
        else:
            return self._artop_useCrcCompMechanism

    @property
    def writeOnlyOnce_(self):
        if self._artop_writeOnlyOnce:
            if self._artop_writeOnlyOnce == "true":
                return True
            return False
        else:
            return self._artop_writeOnlyOnce

    @property
    def writeVerification_(self):
        if self._artop_writeVerification:
            if self._artop_writeVerification == "true":
                return True
            return False
        else:
            return self._artop_writeVerification

    @property
    def writingFrequency_(self):
        return self._artop_writingFrequency

    @property
    def writingPriority_(self):
        return self._artop_writingPriority

    @property
    def ref_nvBlockDescriptor_(self):
        return self._artop_nvBlockDescriptor

    @property
    def nvBlockDescriptor_(self):
        if self._artop_nvBlockDescriptor is not None:
            if hasattr(self._artop_nvBlockDescriptor, "uuid"):
                return self._artop_nvBlockDescriptor.uuid
        return
