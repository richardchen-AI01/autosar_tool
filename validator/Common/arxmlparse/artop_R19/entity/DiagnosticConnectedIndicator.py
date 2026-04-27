# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticConnectedIndicator.py
from .Identifiable import Identifiable

class DiagnosticConnectedIndicator(Identifiable):

    def __init__(self):
        super().__init__()
        from .DiagnosticEvent import DiagnosticEvent
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .DiagnosticOperationCycle import DiagnosticOperationCycle
        from .DiagnosticIndicator import DiagnosticIndicator
        from .VariationPoint import VariationPoint
        self._artop_behavior = None
        self._artop_diagnosticEvent = None
        self._artop_healingCycleCounterThreshold = None
        self._artop_healingCycleRef = None
        self._artop_indicatorRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticEvent': '"DIAGNOSTIC-EVENT"', 
         '_artop_healingCycleCounterThreshold': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_healingCycleRef': '"DIAGNOSTIC-OPERATION-CYCLE"', 
         '_artop_indicatorRef': '"DIAGNOSTIC-INDICATOR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def behavior_(self):
        return self._artop_behavior

    @property
    def ref_diagnosticEvent_(self):
        return self._artop_diagnosticEvent

    @property
    def diagnosticEvent_(self):
        if self._artop_diagnosticEvent is not None:
            if hasattr(self._artop_diagnosticEvent, "uuid"):
                return self._artop_diagnosticEvent.uuid
        return

    @property
    def ref_healingCycleCounterThreshold_(self):
        return self._artop_healingCycleCounterThreshold

    @property
    def healingCycleCounterThreshold_(self):
        if self._artop_healingCycleCounterThreshold is not None:
            if hasattr(self._artop_healingCycleCounterThreshold, "uuid"):
                return self._artop_healingCycleCounterThreshold.uuid
        return

    @property
    def ref_healingCycle_(self):
        return self._artop_healingCycleRef

    @property
    def healingCycle_(self):
        if self._artop_healingCycleRef is not None:
            if hasattr(self._artop_healingCycleRef, "uuid"):
                return self._artop_healingCycleRef.uuid
        return

    @property
    def ref_indicator_(self):
        return self._artop_indicatorRef

    @property
    def indicator_(self):
        if self._artop_indicatorRef is not None:
            if hasattr(self._artop_indicatorRef, "uuid"):
                return self._artop_indicatorRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
