# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestFileTransfer.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticRequestFileTransferClass import DiagnosticRequestFileTransferClass
        self._artop_requestFileTransferClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_requestFileTransferClassRef": "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"})

    @property
    def ref_requestFileTransferClass_(self):
        return self._artop_requestFileTransferClassRef

    @property
    def requestFileTransferClass_(self):
        if self._artop_requestFileTransferClassRef is not None:
            if hasattr(self._artop_requestFileTransferClassRef, "uuid"):
                return self._artop_requestFileTransferClassRef.uuid
        return
