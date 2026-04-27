# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AnalyzedExecutionTime.py
from .ExecutionTime import ExecutionTime

class AnalyzedExecutionTime(ExecutionTime):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_bestCaseExecutionTime = None
        self._artop_worstCaseExecutionTime = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bestCaseExecutionTime':"MULTIDIMENSIONAL-TIME", 
         '_artop_worstCaseExecutionTime':"MULTIDIMENSIONAL-TIME"})

    @property
    def ref_bestCaseExecutionTime_(self):
        return self._artop_bestCaseExecutionTime

    @property
    def bestCaseExecutionTime_(self):
        if self._artop_bestCaseExecutionTime is not None:
            if hasattr(self._artop_bestCaseExecutionTime, "uuid"):
                return self._artop_bestCaseExecutionTime.uuid
        return

    @property
    def ref_worstCaseExecutionTime_(self):
        return self._artop_worstCaseExecutionTime

    @property
    def worstCaseExecutionTime_(self):
        if self._artop_worstCaseExecutionTime is not None:
            if hasattr(self._artop_worstCaseExecutionTime, "uuid"):
                return self._artop_worstCaseExecutionTime.uuid
        return
