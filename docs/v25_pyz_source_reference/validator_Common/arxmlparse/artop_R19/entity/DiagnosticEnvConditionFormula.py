# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnvConditionFormula.py
from .DiagnosticEnvConditionFormulaPart import DiagnosticEnvConditionFormulaPart

class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnvironmentalCondition import DiagnosticEnvironmentalCondition
        from .DiagnosticEnvConditionFormulaPart import DiagnosticEnvConditionFormulaPart
        self._artop_nrcValue = None
        self._artop_op = None
        self._artop_diagnosticEnvironmentalCondition = None
        self._artop_part = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticEnvironmentalCondition':"DIAGNOSTIC-ENVIRONMENTAL-CONDITION", 
         '_artop_part':"DIAGNOSTIC-ENV-CONDITION-FORMULA-PART"})

    @property
    def nrcValue_(self):
        return self._artop_nrcValue

    @property
    def op_(self):
        return self._artop_op

    @property
    def ref_diagnosticEnvironmentalCondition_(self):
        return self._artop_diagnosticEnvironmentalCondition

    @property
    def diagnosticEnvironmentalCondition_(self):
        if self._artop_diagnosticEnvironmentalCondition is not None:
            if hasattr(self._artop_diagnosticEnvironmentalCondition, "uuid"):
                return self._artop_diagnosticEnvironmentalCondition.uuid
        return

    @property
    def parts_DiagnosticEnvConditionFormulaPart(self):
        return self._artop_part
