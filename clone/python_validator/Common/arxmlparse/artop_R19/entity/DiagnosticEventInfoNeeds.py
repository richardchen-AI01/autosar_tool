# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventInfoNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        self._artop_dtcKind = None
        self._artop_dtcNumber = None
        self._artop_obdDtcNumber = None
        self._artop_udsDtcNumber = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def dtcKind_(self):
        return self._artop_dtcKind

    @property
    def dtcNumber_(self):
        return self._artop_dtcNumber

    @property
    def obdDtcNumber_(self):
        return self._artop_obdDtcNumber

    @property
    def udsDtcNumber_(self):
        return self._artop_udsDtcNumber
