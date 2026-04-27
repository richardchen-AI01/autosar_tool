# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventToTroubleCodeJ1939Mapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticEvent import DiagnosticEvent
        from .DiagnosticTroubleCodeJ1939 import DiagnosticTroubleCodeJ1939
        self._artop_diagnosticEventRef = None
        self._artop_troubleCodeJ1939Ref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticEventRef':"DIAGNOSTIC-EVENT", 
         '_artop_troubleCodeJ1939Ref':"DIAGNOSTIC-TROUBLE-CODE-J-1939"})

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
    def ref_troubleCodeJ1939_(self):
        return self._artop_troubleCodeJ1939Ref

    @property
    def troubleCodeJ1939_(self):
        if self._artop_troubleCodeJ1939Ref is not None:
            if hasattr(self._artop_troubleCodeJ1939Ref, "uuid"):
                return self._artop_troubleCodeJ1939Ref.uuid
        return
