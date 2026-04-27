# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDataTransfer.py
from .DiagnosticMemoryByAddress import DiagnosticMemoryByAddress

class DiagnosticDataTransfer(DiagnosticMemoryByAddress):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataTransferClass import DiagnosticDataTransferClass
        self._artop_dataTransferClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataTransferClassRef": "DIAGNOSTIC-DATA-TRANSFER-CLASS"})

    @property
    def ref_dataTransferClass_(self):
        return self._artop_dataTransferClassRef

    @property
    def dataTransferClass_(self):
        if self._artop_dataTransferClassRef is not None:
            if hasattr(self._artop_dataTransferClassRef, "uuid"):
                return self._artop_dataTransferClassRef.uuid
        return
