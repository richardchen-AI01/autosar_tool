# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRoutineNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        self._artop_diagRoutineType = None
        self._artop_ridNumber = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def diagRoutineType_(self):
        return self._artop_diagRoutineType

    @property
    def ridNumber_(self):
        return self._artop_ridNumber
