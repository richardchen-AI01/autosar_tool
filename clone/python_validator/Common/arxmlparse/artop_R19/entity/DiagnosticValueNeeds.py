# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticValueNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticValueNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        self._artop_dataLength = None
        self._artop_diagnosticValueAccess = None
        self._artop_didNumber = None
        self._artop_fixedLength = None
        self._artop_processingStyle = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def diagnosticValueAccess_(self):
        return self._artop_diagnosticValueAccess

    @property
    def didNumber_(self):
        return self._artop_didNumber

    @property
    def fixedLength_(self):
        if self._artop_fixedLength:
            if self._artop_fixedLength == "true":
                return True
            return False
        else:
            return self._artop_fixedLength

    @property
    def processingStyle_(self):
        return self._artop_processingStyle
