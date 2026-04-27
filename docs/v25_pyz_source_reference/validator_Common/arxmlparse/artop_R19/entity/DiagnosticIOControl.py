# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticIOControl.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticIOControl(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticControlEnableMaskBit import DiagnosticControlEnableMaskBit
        from .DiagnosticDataIdentifier import DiagnosticDataIdentifier
        from .DiagnosticIoControlClass import DiagnosticIoControlClass
        self._artop_freezeCurrentState = None
        self._artop_resetToDefault = None
        self._artop_shortTermAdjustment = None
        self._artop_controlEnableMaskBit = []
        self._artop_dataIdentifierRef = None
        self._artop_ioControlClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_controlEnableMaskBit':"DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT", 
         '_artop_dataIdentifierRef':"DIAGNOSTIC-DATA-IDENTIFIER", 
         '_artop_ioControlClassRef':"DIAGNOSTIC-IO-CONTROL-CLASS"})

    @property
    def freezeCurrentState_(self):
        if self._artop_freezeCurrentState:
            if self._artop_freezeCurrentState == "true":
                return True
            return False
        else:
            return self._artop_freezeCurrentState

    @property
    def resetToDefault_(self):
        if self._artop_resetToDefault:
            if self._artop_resetToDefault == "true":
                return True
            return False
        else:
            return self._artop_resetToDefault

    @property
    def shortTermAdjustment_(self):
        if self._artop_shortTermAdjustment:
            if self._artop_shortTermAdjustment == "true":
                return True
            return False
        else:
            return self._artop_shortTermAdjustment

    @property
    def controlEnableMaskBits_DiagnosticControlEnableMaskBit(self):
        return self._artop_controlEnableMaskBit

    @property
    def ref_dataIdentifier_(self):
        return self._artop_dataIdentifierRef

    @property
    def dataIdentifier_(self):
        if self._artop_dataIdentifierRef is not None:
            if hasattr(self._artop_dataIdentifierRef, "uuid"):
                return self._artop_dataIdentifierRef.uuid
        return

    @property
    def ref_ioControlClass_(self):
        return self._artop_ioControlClassRef

    @property
    def ioControlClass_(self):
        if self._artop_ioControlClassRef is not None:
            if hasattr(self._artop_ioControlClassRef, "uuid"):
                return self._artop_ioControlClassRef.uuid
        return
