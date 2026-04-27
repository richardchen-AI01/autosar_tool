# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayCommunicationConnector.py
from .CommunicationConnector import CommunicationConnector

class FlexrayCommunicationConnector(CommunicationConnector):

    def __init__(self):
        super().__init__()
        self._artop_nmReadySleepTime = None
        self._artop_pncFilterDataMask = None
        self._artop_wakeUpChannel = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def nmReadySleepTime_(self):
        if self._artop_nmReadySleepTime:
            return float(self._artop_nmReadySleepTime)
        return self._artop_nmReadySleepTime

    @property
    def pncFilterDataMask_(self):
        return self._artop_pncFilterDataMask

    @property
    def wakeUpChannel_(self):
        if self._artop_wakeUpChannel:
            if self._artop_wakeUpChannel == "true":
                return True
            return False
        else:
            return self._artop_wakeUpChannel
