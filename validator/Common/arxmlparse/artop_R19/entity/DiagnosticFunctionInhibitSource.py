# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFunctionInhibitSource.py
from .Identifiable import Identifiable

class DiagnosticFunctionInhibitSource(Identifiable):

    def __init__(self):
        super().__init__()
        from .DiagnosticFunctionIdentifierInhibit import DiagnosticFunctionIdentifierInhibit
        from .DiagnosticFimAliasEventGroup import DiagnosticFimAliasEventGroup
        from .DiagnosticFimAliasEvent import DiagnosticFimAliasEvent
        self._artop_diagnosticFunctionIdentifierInhibit = None
        self._artop_eventGroupRef = None
        self._artop_eventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticFunctionIdentifierInhibit':"DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT", 
         '_artop_eventGroupRef':"DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP", 
         '_artop_eventRef':"DIAGNOSTIC-FIM-ALIAS-EVENT"})

    @property
    def ref_diagnosticFunctionIdentifierInhibit_(self):
        return self._artop_diagnosticFunctionIdentifierInhibit

    @property
    def diagnosticFunctionIdentifierInhibit_(self):
        if self._artop_diagnosticFunctionIdentifierInhibit is not None:
            if hasattr(self._artop_diagnosticFunctionIdentifierInhibit, "uuid"):
                return self._artop_diagnosticFunctionIdentifierInhibit.uuid
        return

    @property
    def ref_eventGroup_(self):
        return self._artop_eventGroupRef

    @property
    def eventGroup_(self):
        if self._artop_eventGroupRef is not None:
            if hasattr(self._artop_eventGroupRef, "uuid"):
                return self._artop_eventGroupRef.uuid
        return

    @property
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return
