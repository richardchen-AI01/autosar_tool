# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnvConditionFormulaPart.py
from .ARObject import ARObject

class DiagnosticEnvConditionFormulaPart(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnvConditionFormula import DiagnosticEnvConditionFormula
        self._artop_diagnosticEnvConditionFormula = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticEnvConditionFormula": "DIAGNOSTIC-ENV-CONDITION-FORMULA"})

    @property
    def ref_diagnosticEnvConditionFormula_(self):
        return self._artop_diagnosticEnvConditionFormula

    @property
    def diagnosticEnvConditionFormula_(self):
        if self._artop_diagnosticEnvConditionFormula is not None:
            if hasattr(self._artop_diagnosticEnvConditionFormula, "uuid"):
                return self._artop_diagnosticEnvConditionFormula.uuid
        return
