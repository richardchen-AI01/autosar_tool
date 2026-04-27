# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanControllerFdConfiguration.py
from .ARObject import ARObject

class CanControllerFdConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .AbstractCanCommunicationControllerAttributes import AbstractCanCommunicationControllerAttributes
        self._artop_paddingValue = None
        self._artop_propSeg = None
        self._artop_sspOffset = None
        self._artop_syncJumpWidth = None
        self._artop_timeSeg1 = None
        self._artop_timeSeg2 = None
        self._artop_trcvDelayCompensationOffset = None
        self._artop_txBitRateSwitch = None
        self._artop_abstractCanCommunicationControllerAttributes = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_abstractCanCommunicationControllerAttributes": "ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES"})

    @property
    def paddingValue_(self):
        return self._artop_paddingValue

    @property
    def propSeg_(self):
        return self._artop_propSeg

    @property
    def sspOffset_(self):
        return self._artop_sspOffset

    @property
    def syncJumpWidth_(self):
        return self._artop_syncJumpWidth

    @property
    def timeSeg1_(self):
        return self._artop_timeSeg1

    @property
    def timeSeg2_(self):
        return self._artop_timeSeg2

    @property
    def trcvDelayCompensationOffset_(self):
        return self._artop_trcvDelayCompensationOffset

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
