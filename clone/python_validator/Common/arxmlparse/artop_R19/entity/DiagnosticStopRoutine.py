# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticStopRoutine.py
from .DiagnosticRoutineSubfunction import DiagnosticRoutineSubfunction

class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):

    def __init__(self):
        super().__init__()
        from .DiagnosticRoutine import DiagnosticRoutine
        from .DiagnosticParameter import DiagnosticParameter
        self._artop_diagnosticRoutine = None
        self._artop_request = []
        self._artop_response = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticRoutine':"DIAGNOSTIC-ROUTINE", 
         '_artop_request':"DIAGNOSTIC-PARAMETER", 
         '_artop_response':"DIAGNOSTIC-PARAMETER"})

    @property
    def ref_diagnosticRoutine_(self):
        return self._artop_diagnosticRoutine

    @property
    def diagnosticRoutine_(self):
        if self._artop_diagnosticRoutine is not None:
            if hasattr(self._artop_diagnosticRoutine, "uuid"):
                return self._artop_diagnosticRoutine.uuid
        return

    @property
    def requests_DiagnosticParameter(self):
        return self._artop_request

    @property
    def responses_DiagnosticParameter(self):
        return self._artop_response
