# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeGroup.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeRefConditional import DiagnosticTroubleCodeRefConditional
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_dtc = []
        self._artop_groupNumber = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dtc':"DIAGNOSTIC-TROUBLE-CODE-REF-CONDITIONAL", 
         '_artop_groupNumber':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def dtcs_DiagnosticTroubleCodeRefConditional(self):
        return self._artop_dtc

    @property
    def ref_groupNumber_(self):
        return self._artop_groupNumber

    @property
    def groupNumber_(self):
        if self._artop_groupNumber is not None:
            if hasattr(self._artop_groupNumber, "uuid"):
                return self._artop_groupNumber.uuid
        return
