# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticAccessPermission.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticAccessPermission(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticSession import DiagnosticSession
        from .DiagnosticEnvironmentalCondition import DiagnosticEnvironmentalCondition
        from .DiagnosticSecurityLevel import DiagnosticSecurityLevel
        self._artop_diagnosticSessionRef = []
        self._artop_environmentalConditionRef = None
        self._artop_securityLevelRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticSessionRef':"DIAGNOSTIC-SESSION", 
         '_artop_environmentalConditionRef':"DIAGNOSTIC-ENVIRONMENTAL-CONDITION", 
         '_artop_securityLevelRef':"DIAGNOSTIC-SECURITY-LEVEL"})

    @property
    def ref_diagnosticSessions_(self):
        return self._artop_diagnosticSessionRef

    @property
    def diagnosticSessions_(self):
        return self._artop_diagnosticSessionRef

    @property
    def ref_environmentalCondition_(self):
        return self._artop_environmentalConditionRef

    @property
    def environmentalCondition_(self):
        if self._artop_environmentalConditionRef is not None:
            if hasattr(self._artop_environmentalConditionRef, "uuid"):
                return self._artop_environmentalConditionRef.uuid
        return

    @property
    def ref_securityLevels_(self):
        return self._artop_securityLevelRef

    @property
    def securityLevels_(self):
        return self._artop_securityLevelRef
