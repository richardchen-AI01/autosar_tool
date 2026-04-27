# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanCommunicationConnector.py
from .AbstractCanCommunicationConnector import AbstractCanCommunicationConnector

class CanCommunicationConnector(AbstractCanCommunicationConnector):

    def __init__(self):
        super().__init__()
        self._artop_pncWakeupCanId = None
        self._artop_pncWakeupCanIdExtended = None
        self._artop_pncWakeupCanIdMask = None
        self._artop_pncWakeupDataMask = None
        self._artop_pncWakeupDlc = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def pncWakeupCanId_(self):
        return self._artop_pncWakeupCanId

    @property
    def pncWakeupCanIdExtended_(self):
        if self._artop_pncWakeupCanIdExtended:
            if self._artop_pncWakeupCanIdExtended == "true":
                return True
            return False
        else:
            return self._artop_pncWakeupCanIdExtended

    @property
    def pncWakeupCanIdMask_(self):
        return self._artop_pncWakeupCanIdMask

    @property
    def pncWakeupDataMask_(self):
        return self._artop_pncWakeupDataMask

    @property
    def pncWakeupDlc_(self):
        return self._artop_pncWakeupDlc
