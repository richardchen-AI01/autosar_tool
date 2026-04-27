# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticOperationCycle.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticOperationCycle(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        self._artop_automaticEnd = None
        self._artop_cycleAutostart = None
        self._artop_cycleStatusStorage = None
        self._artop_type = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def automaticEnd_(self):
        if self._artop_automaticEnd:
            if self._artop_automaticEnd == "true":
                return True
            return False
        else:
            return self._artop_automaticEnd

    @property
    def cycleAutostart_(self):
        if self._artop_cycleAutostart:
            if self._artop_cycleAutostart == "true":
                return True
            return False
        else:
            return self._artop_cycleAutostart

    @property
    def cycleStatusStorage_(self):
        if self._artop_cycleStatusStorage:
            if self._artop_cycleStatusStorage == "true":
                return True
            return False
        else:
            return self._artop_cycleStatusStorage

    @property
    def type_(self):
        return self._artop_type
