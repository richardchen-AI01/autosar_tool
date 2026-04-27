# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestEmissionRelatedDTC.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestEmissionRelatedDTC(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticRequestEmissionRelatedDTCClass import DiagnosticRequestEmissionRelatedDTCClass
        self._artop_requestEmissionRelatedDtcClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_requestEmissionRelatedDtcClassRef": "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"})

    @property
    def ref_requestEmissionRelatedDtcClass_(self):
        return self._artop_requestEmissionRelatedDtcClassRef

    @property
    def requestEmissionRelatedDtcClass_(self):
        if self._artop_requestEmissionRelatedDtcClassRef is not None:
            if hasattr(self._artop_requestEmissionRelatedDtcClassRef, "uuid"):
                return self._artop_requestEmissionRelatedDtcClassRef.uuid
        return
