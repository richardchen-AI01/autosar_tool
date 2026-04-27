# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticControlEnableMaskBit.py
from .ARObject import ARObject

class DiagnosticControlEnableMaskBit(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticIOControl import DiagnosticIOControl
        from .DiagnosticDataElement import DiagnosticDataElement
        self._artop_bitNumber = None
        self._artop_diagnosticIoControl = None
        self._artop_controlledDataElementRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticIoControl':"DIAGNOSTIC-IO-CONTROL", 
         '_artop_controlledDataElementRef':"DIAGNOSTIC-DATA-ELEMENT"})

    @property
    def bitNumber_(self):
        return self._artop_bitNumber

    @property
    def ref_diagnosticIOControl_(self):
        return self._artop_diagnosticIoControl

    @property
    def diagnosticIOControl_(self):
        if self._artop_diagnosticIoControl is not None:
            if hasattr(self._artop_diagnosticIoControl, "uuid"):
                return self._artop_diagnosticIoControl.uuid
        return

    @property
    def ref_controlledDataElements_(self):
        return self._artop_controlledDataElementRef

    @property
    def controlledDataElements_(self):
        return self._artop_controlledDataElementRef
