# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeUdsToClearConditionGroupMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticTroubleCodeUdsToClearConditionGroupMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticClearConditionGroup import DiagnosticClearConditionGroup
        from .DiagnosticTroubleCodeUds import DiagnosticTroubleCodeUds
        self._artop_clearConditionGroupRef = None
        self._artop_troubleCodeUdsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_clearConditionGroupRef':"DIAGNOSTIC-CLEAR-CONDITION-GROUP", 
         '_artop_troubleCodeUdsRef':"DIAGNOSTIC-TROUBLE-CODE-UDS"})

    @property
    def ref_clearConditionGroup_(self):
        return self._artop_clearConditionGroupRef

    @property
    def clearConditionGroup_(self):
        if self._artop_clearConditionGroupRef is not None:
            if hasattr(self._artop_clearConditionGroupRef, "uuid"):
                return self._artop_clearConditionGroupRef.uuid
        return

    @property
    def ref_troubleCodeUds_(self):
        return self._artop_troubleCodeUdsRef

    @property
    def troubleCodeUds_(self):
        if self._artop_troubleCodeUdsRef is not None:
            if hasattr(self._artop_troubleCodeUdsRef, "uuid"):
                return self._artop_troubleCodeUdsRef.uuid
        return
