# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEnvModeElement.py
from .Referrable import Referrable

class DiagnosticEnvModeElement(Referrable):

    def __init__(self):
        super().__init__()
        from .DiagnosticEnvironmentalCondition import DiagnosticEnvironmentalCondition
        self._artop_diagnosticEnvironmentalCondition = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticEnvironmentalCondition": "DIAGNOSTIC-ENVIRONMENTAL-CONDITION"})

    @property
    def ref_diagnosticEnvironmentalCondition_(self):
        return self._artop_diagnosticEnvironmentalCondition

    @property
    def diagnosticEnvironmentalCondition_(self):
        if self._artop_diagnosticEnvironmentalCondition is not None:
            if hasattr(self._artop_diagnosticEnvironmentalCondition, "uuid"):
                return self._artop_diagnosticEnvironmentalCondition.uuid
        return
