# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ResourceConsumption.py
from .Identifiable import Identifiable

class ResourceConsumption(Identifiable):

    def __init__(self):
        super().__init__()
        from .AccessCountSet import AccessCountSet
        from .ExecutionTime import ExecutionTime
        from .HeapUsage import HeapUsage
        from .MemorySection import MemorySection
        from .SectionNamePrefix import SectionNamePrefix
        from .StackUsage import StackUsage
        from .SystemMemoryUsage import SystemMemoryUsage
        self._artop_accessCountSet = []
        self._artop_executionTime = []
        self._artop_heapUsage = []
        self._artop_memorySection = []
        self._artop_sectionNamePrefix = []
        self._artop_stackUsage = []
        self._artop_systemMemoryUsage = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_accessCountSet': '"ACCESS-COUNT-SET"', 
         '_artop_executionTime': '"EXECUTION-TIME"', 
         '_artop_heapUsage': '"HEAP-USAGE"', 
         '_artop_memorySection': '"MEMORY-SECTION"', 
         '_artop_sectionNamePrefix': '"SECTION-NAME-PREFIX"', 
         '_artop_stackUsage': '"STACK-USAGE"', 
         '_artop_systemMemoryUsage': '"SYSTEM-MEMORY-USAGE"'})

    @property
    def accessCountSets_AccessCountSet(self):
        return self._artop_accessCountSet

    @property
    def executionTimes_ExecutionTime(self):
        return self._artop_executionTime

    @property
    def heapUsages_HeapUsage(self):
        return self._artop_heapUsage

    @property
    def memorySections_MemorySection(self):
        return self._artop_memorySection

    @property
    def sectionNamePrefixs_SectionNamePrefix(self):
        return self._artop_sectionNamePrefix

    @property
    def stackUsages_StackUsage(self):
        return self._artop_stackUsage

    @property
    def systemMemoryUsages_SystemMemoryUsage(self):
        return self._artop_systemMemoryUsage
