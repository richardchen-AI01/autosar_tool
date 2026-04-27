# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanControllerFdConfigurationRequirements.py
from .ARObject import ARObject

class CanControllerFdConfigurationRequirements(ARObject):

    def __init__(self):
        super().__init__()
        from .AbstractCanCommunicationControllerAttributes import AbstractCanCommunicationControllerAttributes
        self._artop_maxNumberOfTimeQuantaPerBit = None
        self._artop_maxSamplePoint = None
        self._artop_maxSyncJumpWidth = None
        self._artop_maxTrcvDelayCompensationOffset = None
        self._artop_minNumberOfTimeQuantaPerBit = None
        self._artop_minSamplePoint = None
        self._artop_minSyncJumpWidth = None
        self._artop_minTrcvDelayCompensationOffset = None
        self._artop_paddingValue = None
        self._artop_txBitRateSwitch = None
        self._artop_abstractCanCommunicationControllerAttributes = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_abstractCanCommunicationControllerAttributes": "ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES"})

    @property
    def maxNumberOfTimeQuantaPerBit_(self):
        if self._artop_maxNumberOfTimeQuantaPerBit:
            return int(self._artop_maxNumberOfTimeQuantaPerBit)
        return self._artop_maxNumberOfTimeQuantaPerBit

    @property
    def maxSamplePoint_(self):
        if self._artop_maxSamplePoint:
            return float(self._artop_maxSamplePoint)
        return self._artop_maxSamplePoint

    @property
    def maxSyncJumpWidth_(self):
        if self._artop_maxSyncJumpWidth:
            return float(self._artop_maxSyncJumpWidth)
        return self._artop_maxSyncJumpWidth

    @property
    def maxTrcvDelayCompensationOffset_(self):
        return self._artop_maxTrcvDelayCompensationOffset

    @property
    def minNumberOfTimeQuantaPerBit_(self):
        if self._artop_minNumberOfTimeQuantaPerBit:
            return int(self._artop_minNumberOfTimeQuantaPerBit)
        return self._artop_minNumberOfTimeQuantaPerBit

    @property
    def minSamplePoint_(self):
        if self._artop_minSamplePoint:
            return float(self._artop_minSamplePoint)
        return self._artop_minSamplePoint

    @property
    def minSyncJumpWidth_(self):
        if self._artop_minSyncJumpWidth:
            return float(self._artop_minSyncJumpWidth)
        return self._artop_minSyncJumpWidth

    @property
    def minTrcvDelayCompensationOffset_(self):
        return self._artop_minTrcvDelayCompensationOffset

    @property
    def paddingValue_(self):
        return self._artop_paddingValue

    @property
    def txBitRateSwitch_(self):
        if self._artop_txBitRateSwitch:
            if self._artop_txBitRateSwitch == "true":
                return True
            return False
        else:
            return self._artop_txBitRateSwitch

    @property
    def ref_abstractCanCommunicationControllerAttributes_(self):
        return self._artop_abstractCanCommunicationControllerAttributes

    @property
    def abstractCanCommunicationControllerAttributes_(self):
        if self._artop_abstractCanCommunicationControllerAttributes is not None:
            if hasattr(self._artop_abstractCanCommunicationControllerAttributes, "uuid"):
                return self._artop_abstractCanCommunicationControllerAttributes.uuid
        return
