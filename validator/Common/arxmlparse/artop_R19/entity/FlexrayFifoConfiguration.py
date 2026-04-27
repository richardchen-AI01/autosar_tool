# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayFifoConfiguration.py
from .ARObject import ARObject

class FlexrayFifoConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .FlexrayCommunicationControllerContent import FlexrayCommunicationControllerContent
        from .FlexrayPhysicalChannel import FlexrayPhysicalChannel
        from .FlexrayFifoRange import FlexrayFifoRange
        self._artop_admitWithoutMessageId = None
        self._artop_baseCycle = None
        self._artop_cycleRepetition = None
        self._artop_fifoDepth = None
        self._artop_msgIdMask = None
        self._artop_msgIdMatch = None
        self._artop_flexrayCommunicationControllerContent = None
        self._artop_channelRef = None
        self._artop_fifoRange = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flexrayCommunicationControllerContent':"FLEXRAY-COMMUNICATION-CONTROLLER-CONTENT", 
         '_artop_channelRef':"FLEXRAY-PHYSICAL-CHANNEL", 
         '_artop_fifoRange':"FLEXRAY-FIFO-RANGE"})

    @property
    def admitWithoutMessageId_(self):
        if self._artop_admitWithoutMessageId:
            if self._artop_admitWithoutMessageId == "true":
                return True
            return False
        else:
            return self._artop_admitWithoutMessageId

    @property
    def baseCycle_(self):
        if self._artop_baseCycle:
            return int(self._artop_baseCycle)
        return self._artop_baseCycle

    @property
    def cycleRepetition_(self):
        if self._artop_cycleRepetition:
            return int(self._artop_cycleRepetition)
        return self._artop_cycleRepetition

    @property
    def fifoDepth_(self):
        if self._artop_fifoDepth:
            return int(self._artop_fifoDepth)
        return self._artop_fifoDepth

    @property
    def msgIdMask_(self):
        if self._artop_msgIdMask:
            return int(self._artop_msgIdMask)
        return self._artop_msgIdMask

    @property
    def msgIdMatch_(self):
        if self._artop_msgIdMatch:
            return int(self._artop_msgIdMatch)
        return self._artop_msgIdMatch

    @property
    def ref_flexrayCommunicationControllerContent_(self):
        return self._artop_flexrayCommunicationControllerContent

    @property
    def flexrayCommunicationControllerContent_(self):
        if self._artop_flexrayCommunicationControllerContent is not None:
            if hasattr(self._artop_flexrayCommunicationControllerContent, "uuid"):
                return self._artop_flexrayCommunicationControllerContent.uuid
        return

    @property
    def ref_channel_(self):
        return self._artop_channelRef

    @property
    def channel_(self):
        if self._artop_channelRef is not None:
            if hasattr(self._artop_channelRef, "uuid"):
                return self._artop_channelRef.uuid
        return

    @property
    def fifoRanges_FlexrayFifoRange(self):
        return self._artop_fifoRange
