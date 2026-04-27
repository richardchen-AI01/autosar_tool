# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventWindow.py
from .ARObject import ARObject

class DiagnosticEventWindow(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticResponseOnEvent import DiagnosticResponseOnEvent
        self._artop_eventWindowTime = None
        self._artop_storageStateEvaluation = None
        self._artop_diagnosticResponseOnEvent = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticResponseOnEvent": "DIAGNOSTIC-RESPONSE-ON-EVENT"})

    @property
    def eventWindowTime_(self):
        return self._artop_eventWindowTime

    @property
    def storageStateEvaluation_(self):
        if self._artop_storageStateEvaluation:
            if self._artop_storageStateEvaluation == "true":
                return True
            return False
        else:
            return self._artop_storageStateEvaluation

    @property
    def ref_diagnosticResponseOnEvent_(self):
        return self._artop_diagnosticResponseOnEvent

    @property
    def diagnosticResponseOnEvent_(self):
        if self._artop_diagnosticResponseOnEvent is not None:
            if hasattr(self._artop_diagnosticResponseOnEvent, "uuid"):
                return self._artop_diagnosticResponseOnEvent.uuid
        return
