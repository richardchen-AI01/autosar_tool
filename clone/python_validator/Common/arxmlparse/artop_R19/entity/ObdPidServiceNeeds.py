# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ObdPidServiceNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class ObdPidServiceNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        self._artop_dataLength = None
        self._artop_parameterId = None
        self._artop_standard = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def dataLength_(self):
        return self._artop_dataLength

    @property
    def parameterId_(self):
        return self._artop_parameterId

    @property
    def standard_(self):
        return self._artop_standard
