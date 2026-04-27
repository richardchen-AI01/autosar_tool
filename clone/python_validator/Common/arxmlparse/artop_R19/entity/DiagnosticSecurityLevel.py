# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticSecurityLevel.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticSecurityLevel(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        self._artop_accessDataRecordSize = None
        self._artop_keySize = None
        self._artop_numFailedSecurityAccess = None
        self._artop_securityDelayTime = None
        self._artop_seedSize = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def accessDataRecordSize_(self):
        return self._artop_accessDataRecordSize

    @property
    def keySize_(self):
        return self._artop_keySize

    @property
    def numFailedSecurityAccess_(self):
        return self._artop_numFailedSecurityAccess

    @property
    def securityDelayTime_(self):
        return self._artop_securityDelayTime

    @property
    def seedSize_(self):
        return self._artop_seedSize
