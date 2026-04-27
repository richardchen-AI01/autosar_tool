# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SimulatedExecutionTime.py
from .ExecutionTime import ExecutionTime

class SimulatedExecutionTime(ExecutionTime):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_maximumExecutionTime = None
        self._artop_minimumExecutionTime = None
        self._artop_nominalExecutionTime = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_maximumExecutionTime':"MULTIDIMENSIONAL-TIME", 
         '_artop_minimumExecutionTime':"MULTIDIMENSIONAL-TIME", 
         '_artop_nominalExecutionTime':"MULTIDIMENSIONAL-TIME"})

    @property
    def ref_maximumExecutionTime_(self):
        return self._artop_maximumExecutionTime

    @property
    def maximumExecutionTime_(self):
        if self._artop_maximumExecutionTime is not None:
            if hasattr(self._artop_maximumExecutionTime, "uuid"):
                return self._artop_maximumExecutionTime.uuid
        return

    @property
    def ref_minimumExecutionTime_(self):
        return self._artop_minimumExecutionTime

    @property
    def minimumExecutionTime_(self):
        if self._artop_minimumExecutionTime is not None:
            if hasattr(self._artop_minimumExecutionTime, "uuid"):
                return self._artop_minimumExecutionTime.uuid
        return

    @property
    def ref_nominalExecutionTime_(self):
        return self._artop_nominalExecutionTime

    @property
    def nominalExecutionTime_(self):
        if self._artop_nominalExecutionTime is not None:
            if hasattr(self._artop_nominalExecutionTime, "uuid"):
                return self._artop_nominalExecutionTime.uuid
        return
