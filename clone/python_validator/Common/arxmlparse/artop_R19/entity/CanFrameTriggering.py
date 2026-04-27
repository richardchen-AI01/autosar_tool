# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanFrameTriggering.py
from .FrameTriggering import FrameTriggering

class CanFrameTriggering(FrameTriggering):

    def __init__(self):
        super().__init__()
        from .TtcanAbsolutelyScheduledTiming import TtcanAbsolutelyScheduledTiming
        from .RxIdentifierRange import RxIdentifierRange
        self._artop_canAddressingMode = None
        self._artop_canFdFrameSupport = None
        self._artop_canFrameRxBehavior = None
        self._artop_canFrameTxBehavior = None
        self._artop_identifier = None
        self._artop_j1939Requestable = None
        self._artop_rxMask = None
        self._artop_txMask = None
        self._artop_absolutelyScheduledTiming = []
        self._artop_rxIdentifierRange = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_absolutelyScheduledTiming':"TTCAN-ABSOLUTELY-SCHEDULED-TIMING", 
         '_artop_rxIdentifierRange':"RX-IDENTIFIER-RANGE"})

    @property
    def canAddressingMode_(self):
        return self._artop_canAddressingMode

    @property
    def canFdFrameSupport_(self):
        if self._artop_canFdFrameSupport:
            if self._artop_canFdFrameSupport == "true":
                return True
            return False
        else:
            return self._artop_canFdFrameSupport

    @property
    def canFrameRxBehavior_(self):
        return self._artop_canFrameRxBehavior

    @property
    def canFrameTxBehavior_(self):
        return self._artop_canFrameTxBehavior

    @property
    def identifier_(self):
        if self._artop_identifier:
            return int(self._artop_identifier)
        return self._artop_identifier

    @property
    def j1939Requestable_(self):
        if self._artop_j1939Requestable:
            if self._artop_j1939Requestable == "true":
                return True
            return False
        else:
            return self._artop_j1939Requestable

    @property
    def rxMask_(self):
        return self._artop_rxMask

    @property
    def txMask_(self):
        return self._artop_txMask

    @property
    def absolutelyScheduledTimings_TtcanAbsolutelyScheduledTiming(self):
        return self._artop_absolutelyScheduledTiming

    @property
    def ref_rxIdentifierRange_(self):
        return self._artop_rxIdentifierRange

    @property
    def rxIdentifierRange_(self):
        if self._artop_rxIdentifierRange is not None:
            if hasattr(self._artop_rxIdentifierRange, "uuid"):
                return self._artop_rxIdentifierRange.uuid
        return
