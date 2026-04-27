# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticSessionControl.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticSessionControl(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticSession import DiagnosticSession
        from .DiagnosticSessionControlClass import DiagnosticSessionControlClass
        self._artop_diagnosticSessionRef = None
        self._artop_sessionControlClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticSessionRef':"DIAGNOSTIC-SESSION", 
         '_artop_sessionControlClassRef':"DIAGNOSTIC-SESSION-CONTROL-CLASS"})

    @property
    def ref_diagnosticSession_(self):
        return self._artop_diagnosticSessionRef

    @property
    def diagnosticSession_(self):
        if self._artop_diagnosticSessionRef is not None:
            if hasattr(self._artop_diagnosticSessionRef, "uuid"):
                return self._artop_diagnosticSessionRef.uuid
        return

    @property
    def ref_sessionControlClass_(self):
        return self._artop_sessionControlClassRef

    @property
    def sessionControlClass_(self):
        if self._artop_sessionControlClassRef is not None:
            if hasattr(self._artop_sessionControlClassRef, "uuid"):
                return self._artop_sessionControlClassRef.uuid
        return
