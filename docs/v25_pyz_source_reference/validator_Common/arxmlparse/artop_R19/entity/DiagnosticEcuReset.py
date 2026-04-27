# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEcuReset.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticEcuReset(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticEcuResetClass import DiagnosticEcuResetClass
        self._artop_customSubFunctionNumber = None
        self._artop_respondToReset = None
        self._artop_ecuResetClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecuResetClassRef": "DIAGNOSTIC-ECU-RESET-CLASS"})

    @property
    def customSubFunctionNumber_(self):
        return self._artop_customSubFunctionNumber

    @property
    def respondToReset_(self):
        return self._artop_respondToReset

    @property
    def ref_ecuResetClass_(self):
        return self._artop_ecuResetClassRef

    @property
    def ecuResetClass_(self):
        if self._artop_ecuResetClassRef is not None:
            if hasattr(self._artop_ecuResetClassRef, "uuid"):
                return self._artop_ecuResetClassRef.uuid
        return
