# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayCommunicationControllerContent.py
from .CommunicationControllerContent import CommunicationControllerContent

class FlexrayCommunicationControllerContent(CommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .FlexrayFifoConfiguration import FlexrayFifoConfiguration
        self._artop_acceptedStartupRange = None
        self._artop_allowHaltDueToClock = None
        self._artop_allowPassiveToActive = None
        self._artop_clusterDriftDamping = None
        self._artop_decodingCorrection = None
        self._artop_delayCompensationA = None
        self._artop_delayCompensationB = None
        self._artop_externOffsetCorrection = None
        self._artop_externRateCorrection = None
        self._artop_externalSync = None
        self._artop_fallBackInternal = None
        self._artop_keySlotId = None
        self._artop_keySlotOnlyEnabled = None
        self._artop_keySlotUsedForStartUp = None
        self._artop_keySlotUsedForSync = None
        self._artop_latestTx = None
        self._artop_listenTimeout = None
        self._artop_macroInitialOffsetA = None
        self._artop_macroInitialOffsetB = None
        self._artop_maximumDynamicPayloadLength = None
        self._artop_microInitialOffsetA = None
        self._artop_microInitialOffsetB = None
        self._artop_microPerCycle = None
        self._artop_microtickDuration = None
        self._artop_nmVectorEarlyUpdate = None
        self._artop_offsetCorrectionOut = None
        self._artop_rateCorrectionOut = None
        self._artop_samplesPerMicrotick = None
        self._artop_secondKeySlotId = None
        self._artop_twoKeySlotMode = None
        self._artop_wakeUpPattern = None
        self._artop_flexrayFifo = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_flexrayFifo": "FLEXRAY-FIFO-CONFIGURATION"})

    @property
    def acceptedStartupRange_(self):
        if self._artop_acceptedStartupRange:
            return int(self._artop_acceptedStartupRange)
        return self._artop_acceptedStartupRange

    @property
    def allowHaltDueToClock_(self):
        if self._artop_allowHaltDueToClock:
            if self._artop_allowHaltDueToClock == "true":
                return True
            return False
        else:
            return self._artop_allowHaltDueToClock

    @property
    def allowPassiveToActive_(self):
        if self._artop_allowPassiveToActive:
            return int(self._artop_allowPassiveToActive)
        return self._artop_allowPassiveToActive

    @property
    def clusterDriftDamping_(self):
        if self._artop_clusterDriftDamping:
            return int(self._artop_clusterDriftDamping)
        return self._artop_clusterDriftDamping

    @property
    def decodingCorrection_(self):
        if self._artop_decodingCorrection:
            return int(self._artop_decodingCorrection)
        return self._artop_decodingCorrection

    @property
    def delayCompensationA_(self):
        if self._artop_delayCompensationA:
            return int(self._artop_delayCompensationA)
        return self._artop_delayCompensationA

    @property
    def delayCompensationB_(self):
        if self._artop_delayCompensationB:
            return int(self._artop_delayCompensationB)
        return self._artop_delayCompensationB

    @property
    def externOffsetCorrection_(self):
        if self._artop_externOffsetCorrection:
            return int(self._artop_externOffsetCorrection)
        return self._artop_externOffsetCorrection

    @property
    def externRateCorrection_(self):
        if self._artop_externRateCorrection:
            return int(self._artop_externRateCorrection)
        return self._artop_externRateCorrection

    @property
    def externalSync_(self):
        if self._artop_externalSync:
            if self._artop_externalSync == "true":
                return True
            return False
        else:
            return self._artop_externalSync

    @property
    def fallBackInternal_(self):
        if self._artop_fallBackInternal:
            if self._artop_fallBackInternal == "true":
                return True
            return False
        else:
            return self._artop_fallBackInternal

    @property
    def keySlotId_(self):
        return self._artop_keySlotId

    @property
    def keySlotOnlyEnabled_(self):
        if self._artop_keySlotOnlyEnabled:
            if self._artop_keySlotOnlyEnabled == "true":
                return True
            return False
        else:
            return self._artop_keySlotOnlyEnabled

    @property
    def keySlotUsedForStartUp_(self):
        if self._artop_keySlotUsedForStartUp:
            if self._artop_keySlotUsedForStartUp == "true":
                return True
            return False
        else:
            return self._artop_keySlotUsedForStartUp

    @property
    def keySlotUsedForSync_(self):
        if self._artop_keySlotUsedForSync:
            if self._artop_keySlotUsedForSync == "true":
                return True
            return False
        else:
            return self._artop_keySlotUsedForSync

    @property
    def latestTx_(self):
        if self._artop_latestTx:
            return int(self._artop_latestTx)
        return self._artop_latestTx

    @property
    def listenTimeout_(self):
        if self._artop_listenTimeout:
            return int(self._artop_listenTimeout)
        return self._artop_listenTimeout

    @property
    def macroInitialOffsetA_(self):
        if self._artop_macroInitialOffsetA:
            return int(self._artop_macroInitialOffsetA)
        return self._artop_macroInitialOffsetA

    @property
    def macroInitialOffsetB_(self):
        if self._artop_macroInitialOffsetB:
            return int(self._artop_macroInitialOffsetB)
        return self._artop_macroInitialOffsetB

    @property
    def maximumDynamicPayloadLength_(self):
        if self._artop_maximumDynamicPayloadLength:
            return int(self._artop_maximumDynamicPayloadLength)
        return self._artop_maximumDynamicPayloadLength

    @property
    def microInitialOffsetA_(self):
        if self._artop_microInitialOffsetA:
            return int(self._artop_microInitialOffsetA)
        return self._artop_microInitialOffsetA

    @property
    def microInitialOffsetB_(self):
        if self._artop_microInitialOffsetB:
            return int(self._artop_microInitialOffsetB)
        return self._artop_microInitialOffsetB

    @property
    def microPerCycle_(self):
        if self._artop_microPerCycle:
            return int(self._artop_microPerCycle)
        return self._artop_microPerCycle

    @property
    def microtickDuration_(self):
        return self._artop_microtickDuration

    @property
    def nmVectorEarlyUpdate_(self):
        if self._artop_nmVectorEarlyUpdate:
            if self._artop_nmVectorEarlyUpdate == "true":
                return True
            return False
        else:
            return self._artop_nmVectorEarlyUpdate

    @property
    def offsetCorrectionOut_(self):
        if self._artop_offsetCorrectionOut:
            return int(self._artop_offsetCorrectionOut)
        return self._artop_offsetCorrectionOut

    @property
    def rateCorrectionOut_(self):
        if self._artop_rateCorrectionOut:
            return int(self._artop_rateCorrectionOut)
        return self._artop_rateCorrectionOut

    @property
    def samplesPerMicrotick_(self):
        if self._artop_samplesPerMicrotick:
            return int(self._artop_samplesPerMicrotick)
        return self._artop_samplesPerMicrotick

    @property
    def secondKeySlotId_(self):
        return self._artop_secondKeySlotId

    @property
    def twoKeySlotMode_(self):
        if self._artop_twoKeySlotMode:
            if self._artop_twoKeySlotMode == "true":
                return True
            return False
        else:
            return self._artop_twoKeySlotMode

    @property
    def wakeUpPattern_(self):
        if self._artop_wakeUpPattern:
            return int(self._artop_wakeUpPattern)
        return self._artop_wakeUpPattern

    @property
    def flexrayFifos_FlexrayFifoConfiguration(self):
        return self._artop_flexrayFifo
