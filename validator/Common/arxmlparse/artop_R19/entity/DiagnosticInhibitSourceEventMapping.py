# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticInhibitSourceEventMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticEvent import DiagnosticEvent
        from .DiagnosticFimEventGroup import DiagnosticFimEventGroup
        from .DiagnosticFunctionInhibitSource import DiagnosticFunctionInhibitSource
        self._artop_diagnosticEventRef = None
        self._artop_eventGroupRef = None
        self._artop_inhibitionSourceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticEventRef':"DIAGNOSTIC-EVENT", 
         '_artop_eventGroupRef':"DIAGNOSTIC-FIM-EVENT-GROUP", 
         '_artop_inhibitionSourceRef':"DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE"})

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
    def ref_eventGroup_(self):
        return self._artop_eventGroupRef

    @property
    def eventGroup_(self):
        if self._artop_eventGroupRef is not None:
            if hasattr(self._artop_eventGroupRef, "uuid"):
                return self._artop_eventGroupRef.uuid
        return

    @property
    def ref_inhibitionSource_(self):
        return self._artop_inhibitionSourceRef

    @property
    def inhibitionSource_(self):
        if self._artop_inhibitionSourceRef is not None:
            if hasattr(self._artop_inhibitionSourceRef, "uuid"):
                return self._artop_inhibitionSourceRef.uuid
        return
