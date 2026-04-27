# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayFrameTriggering.py
from .FrameTriggering import FrameTriggering

class FlexrayFrameTriggering(FrameTriggering):

    def __init__(self):
        super().__init__()
        from .FlexrayAbsolutelyScheduledTiming import FlexrayAbsolutelyScheduledTiming
        self._artop_allowDynamicLSduLength = None
        self._artop_messageId = None
        self._artop_payloadPreambleIndicator = None
        self._artop_absolutelyScheduledTiming = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_absolutelyScheduledTiming": "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING"})

    @property
    def allowDynamicLSduLength_(self):
        if self._artop_allowDynamicLSduLength:
            if self._artop_allowDynamicLSduLength == "true":
                return True
            return False
        else:
            return self._artop_allowDynamicLSduLength

    @property
    def messageId_(self):
        return self._artop_messageId

    @property
    def payloadPreambleIndicator_(self):
        if self._artop_payloadPreambleIndicator:
            if self._artop_payloadPreambleIndicator == "true":
                return True
            return False
        else:
            return self._artop_payloadPreambleIndicator

    @property
    def absolutelyScheduledTimings_FlexrayAbsolutelyScheduledTiming(self):
        return self._artop_absolutelyScheduledTiming
