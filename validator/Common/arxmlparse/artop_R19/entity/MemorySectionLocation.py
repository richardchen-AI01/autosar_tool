# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MemorySectionLocation.py
from .ARObject import ARObject

class MemorySectionLocation(ARObject):

    def __init__(self):
        super().__init__()
        from .ExecutionTime import ExecutionTime
        from .HwElement import HwElement
        from .MemorySection import MemorySection
        self._artop_executionTime = None
        self._artop_providedMemoryRef = None
        self._artop_softwareMemorySectionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_executionTime':"EXECUTION-TIME", 
         '_artop_providedMemoryRef':"HW-ELEMENT", 
         '_artop_softwareMemorySectionRef':"MEMORY-SECTION"})

    @property
    def ref_executionTime_(self):
        return self._artop_executionTime

    @property
    def executionTime_(self):
        if self._artop_executionTime is not None:
            if hasattr(self._artop_executionTime, "uuid"):
                return self._artop_executionTime.uuid
        return

    @property
    def ref_providedMemory_(self):
        return self._artop_providedMemoryRef

    @property
    def providedMemory_(self):
        if self._artop_providedMemoryRef is not None:
            if hasattr(self._artop_providedMemoryRef, "uuid"):
                return self._artop_providedMemoryRef.uuid
        return

    @property
    def ref_softwareMemorySection_(self):
        return self._artop_softwareMemorySectionRef

    @property
    def softwareMemorySection_(self):
        if self._artop_softwareMemorySectionRef is not None:
            if hasattr(self._artop_softwareMemorySectionRef, "uuid"):
                return self._artop_softwareMemorySectionRef.uuid
        return
