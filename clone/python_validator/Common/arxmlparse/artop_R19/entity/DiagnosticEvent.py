# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEvent.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticEvent(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticConnectedIndicator import DiagnosticConnectedIndicator
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_agingAllowed = None
        self._artop_clearEventBehavior = None
        self._artop_eventClearAllowed = None
        self._artop_eventKind = None
        self._artop_prestorageFreezeFrame = None
        self._artop_prestoredFreezeframeStoredInNvm = None
        self._artop_recoverableInSameOperationCycle = None
        self._artop_connectedIndicator = []
        self._artop_eventFailureCycleCounterThreshold = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_connectedIndicator':"DIAGNOSTIC-CONNECTED-INDICATOR", 
         '_artop_eventFailureCycleCounterThreshold':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def agingAllowed_(self):
        if self._artop_agingAllowed:
            if self._artop_agingAllowed == "true":
                return True
            return False
        else:
            return self._artop_agingAllowed

    @property
    def clearEventBehavior_(self):
        return self._artop_clearEventBehavior

    @property
    def eventClearAllowed_(self):
        return self._artop_eventClearAllowed

    @property
    def eventKind_(self):
        return self._artop_eventKind

    @property
    def prestorageFreezeFrame_(self):
        if self._artop_prestorageFreezeFrame:
            if self._artop_prestorageFreezeFrame == "true":
                return True
            return False
        else:
            return self._artop_prestorageFreezeFrame

    @property
    def prestoredFreezeframeStoredInNvm_(self):
        if self._artop_prestoredFreezeframeStoredInNvm:
            if self._artop_prestoredFreezeframeStoredInNvm == "true":
                return True
            return False
        else:
            return self._artop_prestoredFreezeframeStoredInNvm

    @property
    def recoverableInSameOperationCycle_(self):
        if self._artop_recoverableInSameOperationCycle:
            if self._artop_recoverableInSameOperationCycle == "true":
                return True
            return False
        else:
            return self._artop_recoverableInSameOperationCycle

    @property
    def connectedIndicators_DiagnosticConnectedIndicator(self):
        return self._artop_connectedIndicator

    @property
    def ref_eventFailureCycleCounterThreshold_(self):
        return self._artop_eventFailureCycleCounterThreshold

    @property
    def eventFailureCycleCounterThreshold_(self):
        if self._artop_eventFailureCycleCounterThreshold is not None:
            if hasattr(self._artop_eventFailureCycleCounterThreshold, "uuid"):
                return self._artop_eventFailureCycleCounterThreshold.uuid
        return
