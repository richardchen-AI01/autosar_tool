# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnvironmentalCondition.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnvConditionFormula import DiagnosticEnvConditionFormula
        from .DiagnosticEnvModeElement import DiagnosticEnvModeElement
        self._artop_formula = None
        self._artop_modeElement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_formula':"DIAGNOSTIC-ENV-CONDITION-FORMULA", 
         '_artop_modeElement':"DIAGNOSTIC-ENV-MODE-ELEMENT"})

    @property
    def ref_formula_(self):
        return self._artop_formula

    @property
    def formula_(self):
        if self._artop_formula is not None:
            if hasattr(self._artop_formula, "uuid"):
                return self._artop_formula.uuid
        return

    @property
    def modeElements_DiagnosticEnvModeElement(self):
        return self._artop_modeElement
