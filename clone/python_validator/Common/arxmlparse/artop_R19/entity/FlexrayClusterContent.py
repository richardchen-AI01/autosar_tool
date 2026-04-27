# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayClusterContent.py
from .CommunicationClusterContent import CommunicationClusterContent

class FlexrayClusterContent(CommunicationClusterContent):

    def __init__(self):
        super().__init__()
        self._artop_actionPointOffset = None
        self._artop_bit = None
        self._artop_casRxLowMax = None
        self._artop_coldStartAttempts = None
        self._artop_cycle = None
        self._artop_cycleCountMax = None
        self._artop_detectNitError = None
        self._artop_dynamicSlotIdlePhase = None
        self._artop_ignoreAfterTx = None
        self._artop_listenNoise = None
        self._artop_macroPerCycle = None
        self._artop_macrotickDuration = None
        self._artop_maxWithoutClockCorrectionFatal = None
        self._artop_maxWithoutClockCorrectionPassive = None
        self._artop_minislotActionPointOffset = None
        self._artop_minislotDuration = None
        self._artop_networkIdleTime = None
        self._artop_networkManagementVectorLength = None
        self._artop_numberOfMinislots = None
        self._artop_numberOfStaticSlots = None
        self._artop_offsetCorrectionStart = None
        self._artop_payloadLengthStatic = None
        self._artop_safetyMargin = None
        self._artop_sampleClockPeriod = None
        self._artop_staticSlotDuration = None
        self._artop_symbolWindow = None
        self._artop_symbolWindowActionPointOffset = None
        self._artop_syncFrameIdCountMax = None
        self._artop_tranceiverStandbyDelay = None
        self._artop_transmissionStartSequenceDuration = None
        self._artop_wakeupRxIdle = None
        self._artop_wakeupRxLow = None
        self._artop_wakeupRxWindow = None
        self._artop_wakeupTxActive = None
        self._artop_wakeupTxIdle = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def actionPointOffset_(self):
        if self._artop_actionPointOffset:
            return int(self._artop_actionPointOffset)
        return self._artop_actionPointOffset

    @property
    def bit_(self):
        return self._artop_bit

    @property
    def casRxLowMax_(self):
        if self._artop_casRxLowMax:
            return int(self._artop_casRxLowMax)
        return self._artop_casRxLowMax

    @property
    def coldStartAttempts_(self):
        if self._artop_coldStartAttempts:
            return int(self._artop_coldStartAttempts)
        return self._artop_coldStartAttempts

    @property
    def cycle_(self):
        return self._artop_cycle

    @property
    def cycleCountMax_(self):
        if self._artop_cycleCountMax:
            return int(self._artop_cycleCountMax)
        return self._artop_cycleCountMax

    @property
    def detectNitError_(self):
        if self._artop_detectNitError:
            if self._artop_detectNitError == "true":
                return True
            return False
        else:
            return self._artop_detectNitError

    @property
    def dynamicSlotIdlePhase_(self):
        if self._artop_dynamicSlotIdlePhase:
            return int(self._artop_dynamicSlotIdlePhase)
        return self._artop_dynamicSlotIdlePhase

    @property
    def ignoreAfterTx_(self):
        if self._artop_ignoreAfterTx:
            return int(self._artop_ignoreAfterTx)
        return self._artop_ignoreAfterTx

    @property
    def listenNoise_(self):
        if self._artop_listenNoise:
            return int(self._artop_listenNoise)
        return self._artop_listenNoise

    @property
    def macroPerCycle_(self):
        if self._artop_macroPerCycle:
            return int(self._artop_macroPerCycle)
        return self._artop_macroPerCycle

    @property
    def macrotickDuration_(self):
        return self._artop_macrotickDuration

    @property
    def maxWithoutClockCorrectionFatal_(self):
        if self._artop_maxWithoutClockCorrectionFatal:
            return int(self._artop_maxWithoutClockCorrectionFatal)
        return self._artop_maxWithoutClockCorrectionFatal

    @property
    def maxWithoutClockCorrectionPassive_(self):
        if self._artop_maxWithoutClockCorrectionPassive:
            return int(self._artop_maxWithoutClockCorrectionPassive)
        return self._artop_maxWithoutClockCorrectionPassive

    @property
    def minislotActionPointOffset_(self):
        if self._artop_minislotActionPointOffset:
            return int(self._artop_minislotActionPointOffset)
        return self._artop_minislotActionPointOffset

    @property
    def minislotDuration_(self):
        if self._artop_minislotDuration:
            return int(self._artop_minislotDuration)
        return self._artop_minislotDuration

    @property
    def networkIdleTime_(self):
        if self._artop_networkIdleTime:
            return int(self._artop_networkIdleTime)
        return self._artop_networkIdleTime

    @property
    def networkManagementVectorLength_(self):
        if self._artop_networkManagementVectorLength:
            return int(self._artop_networkManagementVectorLength)
        return self._artop_networkManagementVectorLength

    @property
    def numberOfMinislots_(self):
        if self._artop_numberOfMinislots:
            return int(self._artop_numberOfMinislots)
        return self._artop_numberOfMinislots

    @property
    def numberOfStaticSlots_(self):
        if self._artop_numberOfStaticSlots:
            return int(self._artop_numberOfStaticSlots)
        return self._artop_numberOfStaticSlots

    @property
    def offsetCorrectionStart_(self):
        if self._artop_offsetCorrectionStart:
            return int(self._artop_offsetCorrectionStart)
        return self._artop_offsetCorrectionStart

    @property
    def payloadLengthStatic_(self):
        if self._artop_payloadLengthStatic:
            return int(self._artop_payloadLengthStatic)
        return self._artop_payloadLengthStatic

    @property
    def safetyMargin_(self):
        if self._artop_safetyMargin:
            return int(self._artop_safetyMargin)
        return self._artop_safetyMargin

    @property
    def sampleClockPeriod_(self):
        return self._artop_sampleClockPeriod

    @property
    def staticSlotDuration_(self):
        if self._artop_staticSlotDuration:
            return int(self._artop_staticSlotDuration)
        return self._artop_staticSlotDuration

    @property
    def symbolWindow_(self):
        if self._artop_symbolWindow:
            return int(self._artop_symbolWindow)
        return self._artop_symbolWindow

    @property
    def symbolWindowActionPointOffset_(self):
        if self._artop_symbolWindowActionPointOffset:
            return int(self._artop_symbolWindowActionPointOffset)
        return self._artop_symbolWindowActionPointOffset

    @property
    def syncFrameIdCountMax_(self):
        if self._artop_syncFrameIdCountMax:
            return int(self._artop_syncFrameIdCountMax)
        return self._artop_syncFrameIdCountMax

    @property
    def tranceiverStandbyDelay_(self):
        if self._artop_tranceiverStandbyDelay:
            return float(self._artop_tranceiverStandbyDelay)
        return self._artop_tranceiverStandbyDelay

    @property
    def transmissionStartSequenceDuration_(self):
        if self._artop_transmissionStartSequenceDuration:
            return int(self._artop_transmissionStartSequenceDuration)
        return self._artop_transmissionStartSequenceDuration

    @property
    def wakeupRxIdle_(self):
        if self._artop_wakeupRxIdle:
            return int(self._artop_wakeupRxIdle)
        return self._artop_wakeupRxIdle

    @property
    def wakeupRxLow_(self):
        if self._artop_wakeupRxLow:
            return int(self._artop_wakeupRxLow)
        return self._artop_wakeupRxLow

    @property
    def wakeupRxWindow_(self):
        if self._artop_wakeupRxWindow:
            return int(self._artop_wakeupRxWindow)
        return self._artop_wakeupRxWindow

    @property
    def wakeupTxActive_(self):
        if self._artop_wakeupTxActive:
            return int(self._artop_wakeupTxActive)
        return self._artop_wakeupTxActive

    @property
    def wakeupTxIdle_(self):
        if self._artop_wakeupTxIdle:
            return int(self._artop_wakeupTxIdle)
        return self._artop_wakeupTxIdle
