# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeUdsToTroubleCodeObdMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeObd import DiagnosticTroubleCodeObd
        from .DiagnosticTroubleCodeUds import DiagnosticTroubleCodeUds
        self._artop_troubleCodeObdRef = None
        self._artop_troubleCodeUdsRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_troubleCodeObdRef':"DIAGNOSTIC-TROUBLE-CODE-OBD", 
         '_artop_troubleCodeUdsRef':"DIAGNOSTIC-TROUBLE-CODE-UDS"})

    @property
    def ref_troubleCodeObd_(self):
        return self._artop_troubleCodeObdRef

    @property
    def troubleCodeObd_(self):
        if self._artop_troubleCodeObdRef is not None:
            if hasattr(self._artop_troubleCodeObdRef, "uuid"):
                return self._artop_troubleCodeObdRef.uuid
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
