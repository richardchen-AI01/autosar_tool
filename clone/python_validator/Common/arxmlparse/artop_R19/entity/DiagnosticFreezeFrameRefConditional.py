# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFreezeFrameRefConditional.py
from .ARObject import ARObject

class DiagnosticFreezeFrameRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeProps import DiagnosticTroubleCodeProps
        from .DiagnosticFreezeFrame import DiagnosticFreezeFrame
        from .VariationPoint import VariationPoint
        self._artop_diagnosticTroubleCodeProps = None
        self._artop_diagnosticFreezeFrameRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticTroubleCodeProps':"DIAGNOSTIC-TROUBLE-CODE-PROPS", 
         '_artop_diagnosticFreezeFrameRef':"DIAGNOSTIC-FREEZE-FRAME", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_diagnosticTroubleCodeProps_(self):
        return self._artop_diagnosticTroubleCodeProps

    @property
    def diagnosticTroubleCodeProps_(self):
        if self._artop_diagnosticTroubleCodeProps is not None:
            if hasattr(self._artop_diagnosticTroubleCodeProps, "uuid"):
                return self._artop_diagnosticTroubleCodeProps.uuid
        return

    @property
    def ref_diagnosticFreezeFrame_(self):
        return self._artop_diagnosticFreezeFrameRef

    @property
    def diagnosticFreezeFrame_(self):
        if self._artop_diagnosticFreezeFrameRef is not None:
            if hasattr(self._artop_diagnosticFreezeFrameRef, "uuid"):
                return self._artop_diagnosticFreezeFrameRef.uuid
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
