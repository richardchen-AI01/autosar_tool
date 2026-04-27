# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticClearResetEmissionRelatedInfo.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticClearResetEmissionRelatedInfoClass import DiagnosticClearResetEmissionRelatedInfoClass
        self._artop_clearResetEmissionRelatedDiagnosticInfoClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_clearResetEmissionRelatedDiagnosticInfoClassRef": "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"})

    @property
    def ref_clearResetEmissionRelatedDiagnosticInfoClass_(self):
        return self._artop_clearResetEmissionRelatedDiagnosticInfoClassRef

    @property
    def clearResetEmissionRelatedDiagnosticInfoClass_(self):
        if self._artop_clearResetEmissionRelatedDiagnosticInfoClassRef is not None:
            if hasattr(self._artop_clearResetEmissionRelatedDiagnosticInfoClassRef, "uuid"):
                return self._artop_clearResetEmissionRelatedDiagnosticInfoClassRef.uuid
        return
