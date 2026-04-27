# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticMemoryAddressableRangeAccess.py
from .DiagnosticMemoryByAddress import DiagnosticMemoryByAddress

class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress):

    def __init__(self):
        super().__init__()
        from .DiagnosticMemoryIdentifier import DiagnosticMemoryIdentifier
        self._artop_memoryRangeRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_memoryRangeRef": "DIAGNOSTIC-MEMORY-IDENTIFIER"})

    @property
    def ref_memoryRanges_(self):
        return self._artop_memoryRangeRef

    @property
    def memoryRanges_(self):
        return self._artop_memoryRangeRef
