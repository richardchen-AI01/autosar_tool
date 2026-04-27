# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticIoControlNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticValueNeeds import DiagnosticValueNeeds
        self._artop_didNumber = None
        self._artop_freezeCurrentStateSupported = None
        self._artop_resetToDefaultSupported = None
        self._artop_shortTermAdjustmentSupported = None
        self._artop_currentValueRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_currentValueRef": "DIAGNOSTIC-VALUE-NEEDS"})

    @property
    def didNumber_(self):
        return self._artop_didNumber

    @property
    def freezeCurrentStateSupported_(self):
        if self._artop_freezeCurrentStateSupported:
            if self._artop_freezeCurrentStateSupported == "true":
                return True
            return False
        else:
            return self._artop_freezeCurrentStateSupported

    @property
    def resetToDefaultSupported_(self):
        if self._artop_resetToDefaultSupported:
            if self._artop_resetToDefaultSupported == "true":
                return True
            return False
        else:
            return self._artop_resetToDefaultSupported

    @property
    def shortTermAdjustmentSupported_(self):
        if self._artop_shortTermAdjustmentSupported:
            if self._artop_shortTermAdjustmentSupported == "true":
                return True
            return False
        else:
            return self._artop_shortTermAdjustmentSupported

    @property
    def ref_currentValue_(self):
        return self._artop_currentValueRef

    @property
    def currentValue_(self):
        if self._artop_currentValueRef is not None:
            if hasattr(self._artop_currentValueRef, "uuid"):
                return self._artop_currentValueRef.uuid
        return
