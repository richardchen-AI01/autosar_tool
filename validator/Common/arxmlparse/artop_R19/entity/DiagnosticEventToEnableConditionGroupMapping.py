# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventToEnableConditionGroupMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticEvent import DiagnosticEvent
        from .DiagnosticEnableConditionGroup import DiagnosticEnableConditionGroup
        self._artop_diagnosticEventRef = None
        self._artop_enableConditionGroupRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticEventRef':"DIAGNOSTIC-EVENT", 
         '_artop_enableConditionGroupRef':"DIAGNOSTIC-ENABLE-CONDITION-GROUP"})

    @property
    def ref_diagnosticEvent_(self):
        return self._artop_diagnosticEventRef

    @property
    def diagnosticEvent_(self):
        if self._artop_diagnosticEventRef is not None:
            if hasattr(self._artop_diagnosticEventRef, "uuid"):
                return self._artop_diagnosticEventRef.uuid
        return

    @property
    def ref_enableConditionGroup_(self):
        return self._artop_enableConditionGroupRef

    @property
    def enableConditionGroup_(self):
        if self._artop_enableConditionGroupRef is not None:
            if hasattr(self._artop_enableConditionGroupRef, "uuid"):
                return self._artop_enableConditionGroupRef.uuid
        return
