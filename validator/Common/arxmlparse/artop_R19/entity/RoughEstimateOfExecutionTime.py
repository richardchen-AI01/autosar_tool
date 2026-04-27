# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RoughEstimateOfExecutionTime.py
from .ExecutionTime import ExecutionTime

class RoughEstimateOfExecutionTime(ExecutionTime):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_additionalInformation = None
        self._artop_estimatedExecutionTime = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_estimatedExecutionTime": "MULTIDIMENSIONAL-TIME"})

    @property
    def additionalInformation_(self):
        return self._artop_additionalInformation

    @property
    def ref_estimatedExecutionTime_(self):
        return self._artop_estimatedExecutionTime

    @property
    def estimatedExecutionTime_(self):
        if self._artop_estimatedExecutionTime is not None:
            if hasattr(self._artop_estimatedExecutionTime, "uuid"):
                return self._artop_estimatedExecutionTime.uuid
        return
