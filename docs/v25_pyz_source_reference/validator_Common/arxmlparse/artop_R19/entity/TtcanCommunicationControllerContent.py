# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TtcanCommunicationControllerContent.py
from .AbstractCanCommunicationControllerContent import AbstractCanCommunicationControllerContent

class TtcanCommunicationControllerContent(AbstractCanCommunicationControllerContent):

    def __init__(self):
        super().__init__()
        self._artop_applWatchdogLimit = None
        self._artop_expectedTxTrigger = None
        self._artop_externalClockSynchronisation = None
        self._artop_initialRefOffset = None
        self._artop_master = None
        self._artop_timeMasterPriority = None
        self._artop_timeTriggeredCanLevel = None
        self._artop_txEnableWindowLength = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def applWatchdogLimit_(self):
        if self._artop_applWatchdogLimit:
            return int(self._artop_applWatchdogLimit)
        return self._artop_applWatchdogLimit

    @property
    def expectedTxTrigger_(self):
        if self._artop_expectedTxTrigger:
            return int(self._artop_expectedTxTrigger)
        return self._artop_expectedTxTrigger

    @property
    def externalClockSynchronisation_(self):
        if self._artop_externalClockSynchronisation:
            if self._artop_externalClockSynchronisation == "true":
                return True
            return False
        else:
            return self._artop_externalClockSynchronisation

    @property
    def initialRefOffset_(self):
        if self._artop_initialRefOffset:
            return int(self._artop_initialRefOffset)
        return self._artop_initialRefOffset

    @property
    def master_(self):
        if self._artop_master:
            if self._artop_master == "true":
                return True
            return False
        else:
            return self._artop_master

    @property
    def timeMasterPriority_(self):
        if self._artop_timeMasterPriority:
            return int(self._artop_timeMasterPriority)
        return self._artop_timeMasterPriority

    @property
    def timeTriggeredCanLevel_(self):
        if self._artop_timeTriggeredCanLevel:
            return int(self._artop_timeTriggeredCanLevel)
        return self._artop_timeTriggeredCanLevel

    @property
    def txEnableWindowLength_(self):
        if self._artop_txEnableWindowLength:
            return int(self._artop_txEnableWindowLength)
        return self._artop_txEnableWindowLength
