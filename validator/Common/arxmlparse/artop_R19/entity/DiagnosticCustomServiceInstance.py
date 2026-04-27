# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticCustomServiceInstance.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticCustomServiceClass import DiagnosticCustomServiceClass
        self._artop_customServiceClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_customServiceClassRef": "DIAGNOSTIC-CUSTOM-SERVICE-CLASS"})

    @property
    def ref_customServiceClass_(self):
        return self._artop_customServiceClassRef

    @property
    def customServiceClass_(self):
        if self._artop_customServiceClassRef is not None:
            if hasattr(self._artop_customServiceClassRef, "uuid"):
                return self._artop_customServiceClassRef.uuid
        return
