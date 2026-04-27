# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventToDebounceAlgorithmMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticDebounceAlgorithmProps import DiagnosticDebounceAlgorithmProps
        from .DiagnosticEvent import DiagnosticEvent
        self._artop_debounceAlgorithmRef = None
        self._artop_diagnosticEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_debounceAlgorithmRef':"DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS", 
         '_artop_diagnosticEventRef':"DIAGNOSTIC-EVENT"})

    @property
    def ref_debounceAlgorithm_(self):
        return self._artop_debounceAlgorithmRef

    @property
    def debounceAlgorithm_(self):
        if self._artop_debounceAlgorithmRef is not None:
            if hasattr(self._artop_debounceAlgorithmRef, "uuid"):
                return self._artop_debounceAlgorithmRef.uuid
        return

    @property
    def ref_diagnosticEvent_(self):
        return self._artop_diagnosticEventRef

    @property
    def diagnosticEvent_(self):
        if self._artop_diagnosticEventRef is not None:
            if hasattr(self._artop_diagnosticEventRef, "uuid"):
                return self._artop_diagnosticEventRef.uuid
        return
