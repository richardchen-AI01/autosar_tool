# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeRefConditional.py
from .ARObject import ARObject

class DiagnosticTroubleCodeRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeGroup import DiagnosticTroubleCodeGroup
        from .DiagnosticTroubleCode import DiagnosticTroubleCode
        from .VariationPoint import VariationPoint
        self._artop_diagnosticTroubleCodeGroup = None
        self._artop_diagnosticTroubleCodeRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticTroubleCodeGroup':"DIAGNOSTIC-TROUBLE-CODE-GROUP", 
         '_artop_diagnosticTroubleCodeRef':"DIAGNOSTIC-TROUBLE-CODE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticTroubleCodeGroup_(self):
        return self._artop_diagnosticTroubleCodeGroup

    @property
    def diagnosticTroubleCodeGroup_(self):
        if self._artop_diagnosticTroubleCodeGroup is not None:
            if hasattr(self._artop_diagnosticTroubleCodeGroup, "uuid"):
                return self._artop_diagnosticTroubleCodeGroup.uuid
        return

    @property
    def ref_diagnosticTroubleCode_(self):
        return self._artop_diagnosticTroubleCodeRef

    @property
    def diagnosticTroubleCode_(self):
        if self._artop_diagnosticTroubleCodeRef is not None:
            if hasattr(self._artop_diagnosticTroubleCodeRef, "uuid"):
                return self._artop_diagnosticTroubleCodeRef.uuid
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
