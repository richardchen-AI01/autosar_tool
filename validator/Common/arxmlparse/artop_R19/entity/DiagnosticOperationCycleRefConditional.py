# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticOperationCycleRefConditional.py
from .ARObject import ARObject

class DiagnosticOperationCycleRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticAging import DiagnosticAging
        from .DiagnosticOperationCycle import DiagnosticOperationCycle
        from .VariationPoint import VariationPoint
        self._artop_diagnosticAging = None
        self._artop_diagnosticOperationCycleRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticAging':"DIAGNOSTIC-AGING", 
         '_artop_diagnosticOperationCycleRef':"DIAGNOSTIC-OPERATION-CYCLE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticAging_(self):
        return self._artop_diagnosticAging

    @property
    def diagnosticAging_(self):
        if self._artop_diagnosticAging is not None:
            if hasattr(self._artop_diagnosticAging, "uuid"):
                return self._artop_diagnosticAging.uuid
        return

    @property
    def ref_diagnosticOperationCycle_(self):
        return self._artop_diagnosticOperationCycleRef

    @property
    def diagnosticOperationCycle_(self):
        if self._artop_diagnosticOperationCycleRef is not None:
            if hasattr(self._artop_diagnosticOperationCycleRef, "uuid"):
                return self._artop_diagnosticOperationCycleRef.uuid
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
