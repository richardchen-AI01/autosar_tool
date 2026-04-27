# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticCommonPropsContent.py
from .ARObject import ARObject

class DiagnosticCommonPropsContent(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticDebounceAlgorithmProps import DiagnosticDebounceAlgorithmProps
        self._artop_agingRequiresTestedCycle = None
        self._artop_clearDtcLimitation = None
        self._artop_defaultEndianness = None
        self._artop_dtcStatusAvailabilityMask = None
        self._artop_environmentDataCapture = None
        self._artop_eventDisplacementStrategy = None
        self._artop_maxNumberOfEventEntries = None
        self._artop_maxNumberOfRequestCorrectlyReceivedResponsePending = None
        self._artop_memoryEntryStorageTrigger = None
        self._artop_occurrenceCounterProcessing = None
        self._artop_resetConfirmedBitOnOverflow = None
        self._artop_responseOnAllRequestSids = None
        self._artop_responseOnSecondDeclinedRequest = None
        self._artop_securityDelayTimeOnBoot = None
        self._artop_statusBitHandlingTestFailedSinceLastClear = None
        self._artop_statusBitStorageTestFailed = None
        self._artop_typeOfDtcSupported = None
        self._artop_typeOfFreezeFrameRecordNumeration = None
        self._artop_debounceAlgorithmProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_debounceAlgorithmProps": "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS"})

    @property
    def agingRequiresTestedCycle_(self):
        if self._artop_agingRequiresTestedCycle:
            if self._artop_agingRequiresTestedCycle == "true":
                return True
            return False
        else:
            return self._artop_agingRequiresTestedCycle

    @property
    def clearDtcLimitation_(self):
        return self._artop_clearDtcLimitation

    @property
    def defaultEndianness_(self):
        return self._artop_defaultEndianness

    @property
    def dtcStatusAvailabilityMask_(self):
        return self._artop_dtcStatusAvailabilityMask

    @property
    def environmentDataCapture_(self):
        return self._artop_environmentDataCapture

    @property
    def eventDisplacementStrategy_(self):
        return self._artop_eventDisplacementStrategy

    @property
    def maxNumberOfEventEntries_(self):
        return self._artop_maxNumberOfEventEntries

    @property
    def maxNumberOfRequestCorrectlyReceivedResponsePending_(self):
        return self._artop_maxNumberOfRequestCorrectlyReceivedResponsePending

    @property
    def memoryEntryStorageTrigger_(self):
        return self._artop_memoryEntryStorageTrigger

    @property
    def occurrenceCounterProcessing_(self):
        return self._artop_occurrenceCounterProcessing

    @property
    def resetConfirmedBitOnOverflow_(self):
        if self._artop_resetConfirmedBitOnOverflow:
            if self._artop_resetConfirmedBitOnOverflow == "true":
                return True
            return False
        else:
            return self._artop_resetConfirmedBitOnOverflow

    @property
    def responseOnAllRequestSids_(self):
        if self._artop_responseOnAllRequestSids:
            if self._artop_responseOnAllRequestSids == "true":
                return True
            return False
        else:
            return self._artop_responseOnAllRequestSids

    @property
    def responseOnSecondDeclinedRequest_(self):
        if self._artop_responseOnSecondDeclinedRequest:
            if self._artop_responseOnSecondDeclinedRequest == "true":
                return True
            return False
        else:
            return self._artop_responseOnSecondDeclinedRequest

    @property
    def securityDelayTimeOnBoot_(self):
        return self._artop_securityDelayTimeOnBoot

    @property
    def statusBitHandlingTestFailedSinceLastClear_(self):
        return self._artop_statusBitHandlingTestFailedSinceLastClear

    @property
    def statusBitStorageTestFailed_(self):
        if self._artop_statusBitStorageTestFailed:
            if self._artop_statusBitStorageTestFailed == "true":
                return True
            return False
        else:
            return self._artop_statusBitStorageTestFailed

    @property
    def typeOfDtcSupported_(self):
        return self._artop_typeOfDtcSupported

    @property
    def typeOfFreezeFrameRecordNumeration_(self):
        return self._artop_typeOfFreezeFrameRecordNumeration

    @property
    def debounceAlgorithmProps_DiagnosticDebounceAlgorithmProps(self):
        return self._artop_debounceAlgorithmProps
