# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticReadMemoryByAddress.py
from .DiagnosticMemoryAddressableRangeAccess import DiagnosticMemoryAddressableRangeAccess

class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):

    def __init__(self):
        super().__init__()
        from .DiagnosticReadMemoryByAddressClass import DiagnosticReadMemoryByAddressClass
        self._artop_readClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_readClassRef": "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"})

    @property
    def ref_readClass_(self):
        return self._artop_readClassRef

    @property
    def readClass_(self):
        if self._artop_readClassRef is not None:
            if hasattr(self._artop_readClassRef, "uuid"):
                return self._artop_readClassRef.uuid
        return
