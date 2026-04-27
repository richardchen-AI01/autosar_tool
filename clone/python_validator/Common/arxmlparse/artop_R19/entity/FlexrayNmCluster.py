# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayNmCluster.py
from .NmCluster import NmCluster

class FlexrayNmCluster(NmCluster):

    def __init__(self):
        super().__init__()
        self._artop_nmCarWakeUpBitPosition = None
        self._artop_nmCarWakeUpFilterEnabled = None
        self._artop_nmCarWakeUpFilterNodeId = None
        self._artop_nmCarWakeUpRxEnabled = None
        self._artop_nmControlBitVectorActive = None
        self._artop_nmDataCycle = None
        self._artop_nmDataEnabled = None
        self._artop_nmDetectionLock = None
        self._artop_nmMainFunctionPeriod = None
        self._artop_nmMessageTimeoutTime = None
        self._artop_nmReadySleepCount = None
        self._artop_nmRemoteSleepIndicationTime = None
        self._artop_nmRepeatMessageBitActive = None
        self._artop_nmRepeatMessageTime = None
        self._artop_nmRepetitionCycle = None
        self._artop_nmVotingCycle = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def nmCarWakeUpBitPosition_(self):
        return self._artop_nmCarWakeUpBitPosition

    @property
    def nmCarWakeUpFilterEnabled_(self):
        if self._artop_nmCarWakeUpFilterEnabled:
            if self._artop_nmCarWakeUpFilterEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmCarWakeUpFilterEnabled

    @property
    def nmCarWakeUpFilterNodeId_(self):
        return self._artop_nmCarWakeUpFilterNodeId

    @property
    def nmCarWakeUpRxEnabled_(self):
        if self._artop_nmCarWakeUpRxEnabled:
            if self._artop_nmCarWakeUpRxEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmCarWakeUpRxEnabled

    @property
    def nmControlBitVectorActive_(self):
        if self._artop_nmControlBitVectorActive:
            if self._artop_nmControlBitVectorActive == "true":
                return True
            return False
        else:
            return self._artop_nmControlBitVectorActive

    @property
    def nmDataCycle_(self):
        if self._artop_nmDataCycle:
            return int(self._artop_nmDataCycle)
        return self._artop_nmDataCycle

    @property
    def nmDataEnabled_(self):
        if self._artop_nmDataEnabled:
            if self._artop_nmDataEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmDataEnabled

    @property
    def nmDetectionLock_(self):
        return self._artop_nmDetectionLock

    @property
    def nmMainFunctionPeriod_(self):
        return self._artop_nmMainFunctionPeriod

    @property
    def nmMessageTimeoutTime_(self):
        return self._artop_nmMessageTimeoutTime

    @property
    def nmReadySleepCount_(self):
        if self._artop_nmReadySleepCount:
            return int(self._artop_nmReadySleepCount)
        return self._artop_nmReadySleepCount

    @property
    def nmRemoteSleepIndicationTime_(self):
        return self._artop_nmRemoteSleepIndicationTime

    @property
    def nmRepeatMessageBitActive_(self):
        if self._artop_nmRepeatMessageBitActive:
            if self._artop_nmRepeatMessageBitActive == "true":
                return True
            return False
        else:
            return self._artop_nmRepeatMessageBitActive

    @property
    def nmRepeatMessageTime_(self):
        return self._artop_nmRepeatMessageTime

    @property
    def nmRepetitionCycle_(self):
        if self._artop_nmRepetitionCycle:
            return int(self._artop_nmRepetitionCycle)
        return self._artop_nmRepetitionCycle

    @property
    def nmVotingCycle_(self):
        if self._artop_nmVotingCycle:
            return int(self._artop_nmVotingCycle)
        return self._artop_nmVotingCycle
