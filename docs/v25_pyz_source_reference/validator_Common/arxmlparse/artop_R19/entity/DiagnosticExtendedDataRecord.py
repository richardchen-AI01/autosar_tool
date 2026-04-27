# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticExtendedDataRecord.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticExtendedDataRecord(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameter import DiagnosticParameter
        self._artop_customTrigger = None
        self._artop_recordNumber = None
        self._artop_trigger = None
        self._artop_update = None
        self._artop_recordElement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_recordElement": "DIAGNOSTIC-PARAMETER"})

    @property
    def customTrigger_(self):
        return self._artop_customTrigger

    @property
    def recordNumber_(self):
        return self._artop_recordNumber

    @property
    def trigger_(self):
        return self._artop_trigger

    @property
    def update_(self):
        if self._artop_update:
            if self._artop_update == "true":
                return True
            return False
        else:
            return self._artop_update

    @property
    def recordElements_DiagnosticParameter(self):
        return self._artop_recordElement
