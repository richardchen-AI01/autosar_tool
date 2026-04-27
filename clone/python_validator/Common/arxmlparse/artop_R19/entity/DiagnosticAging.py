# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticAging.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticAging(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticOperationCycleRefConditional import DiagnosticOperationCycleRefConditional
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_agingCycle = []
        self._artop_threshold = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_agingCycle':"DIAGNOSTIC-OPERATION-CYCLE-REF-CONDITIONAL", 
         '_artop_threshold':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def agingCycles_DiagnosticOperationCycleRefConditional(self):
        return self._artop_agingCycle

    @property
    def ref_threshold_(self):
        return self._artop_threshold

    @property
    def threshold_(self):
        if self._artop_threshold is not None:
            if hasattr(self._artop_threshold, "uuid"):
                return self._artop_threshold.uuid
        return
