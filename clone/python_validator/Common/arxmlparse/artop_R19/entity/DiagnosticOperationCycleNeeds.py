# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticOperationCycleNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        self._artop_operationCycle = None
        self._artop_operationCycleAutomaticEnd = None
        self._artop_operationCycleAutostart = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def operationCycle_(self):
        return self._artop_operationCycle

    @property
    def operationCycleAutomaticEnd_(self):
        if self._artop_operationCycleAutomaticEnd:
            if self._artop_operationCycleAutomaticEnd == "true":
                return True
            return False
        else:
            return self._artop_operationCycleAutomaticEnd

    @property
    def operationCycleAutostart_(self):
        if self._artop_operationCycleAutostart:
            if self._artop_operationCycleAutostart == "true":
                return True
            return False
        else:
            return self._artop_operationCycleAutostart
