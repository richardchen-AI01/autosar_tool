# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeProps.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticTroubleCodeProps(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticAging import DiagnosticAging
        from .DiagnosticExtendedDataRecordRefConditional import DiagnosticExtendedDataRecordRefConditional
        from .DiagnosticFreezeFrameRefConditional import DiagnosticFreezeFrameRefConditional
        from .DiagnosticDataIdentifierSet import DiagnosticDataIdentifierSet
        from .DiagnosticDataIdentifierSetRefConditional import DiagnosticDataIdentifierSetRefConditional
        from .DiagnosticMemoryDestination import DiagnosticMemoryDestination
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_agingAllowed = None
        self._artop_environmentCaptureToReporting = None
        self._artop_fdcThresholdStorageValue = None
        self._artop_immediateNvDataStorage = None
        self._artop_maxNumberFreezeFrameRecords = None
        self._artop_significance = None
        self._artop_agingRef = None
        self._artop_extendedDataRecord = []
        self._artop_freezeFrame = []
        self._artop_freezeFrameContentRef = None
        self._artop_freezeFrameContentWwhObdRef = None
        self._artop_legislatedFreezeFrameContentWwhObd = []
        self._artop_memoryDestinationRef = []
        self._artop_priority = None
        self._artop_snapshotRecordContent = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_agingRef': '"DIAGNOSTIC-AGING"', 
         '_artop_extendedDataRecord': '"DIAGNOSTIC-EXTENDED-DATA-RECORD-REF-CONDITIONAL"', 
         '_artop_freezeFrame': '"DIAGNOSTIC-FREEZE-FRAME-REF-CONDITIONAL"', 
         '_artop_freezeFrameContentRef': '"DIAGNOSTIC-DATA-IDENTIFIER-SET"', 
         '_artop_freezeFrameContentWwhObdRef': '"DIAGNOSTIC-DATA-IDENTIFIER-SET"', 
         '_artop_legislatedFreezeFrameContentWwhObd': '"DIAGNOSTIC-DATA-IDENTIFIER-SET-REF-CONDITIONAL"', 
         '_artop_memoryDestinationRef': '"DIAGNOSTIC-MEMORY-DESTINATION"', 
         '_artop_priority': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_snapshotRecordContent': '"DIAGNOSTIC-DATA-IDENTIFIER-SET-REF-CONDITIONAL"'})

    @property
    def agingAllowed_(self):
        if self._artop_agingAllowed:
            if self._artop_agingAllowed == "true":
                return True
            return False
        else:
            return self._artop_agingAllowed

    @property
    def environmentCaptureToReporting_(self):
        return self._artop_environmentCaptureToReporting

    @property
    def fdcThresholdStorageValue_(self):
        return self._artop_fdcThresholdStorageValue

    @property
    def immediateNvDataStorage_(self):
        if self._artop_immediateNvDataStorage:
            if self._artop_immediateNvDataStorage == "true":
                return True
            return False
        else:
            return self._artop_immediateNvDataStorage

    @property
    def maxNumberFreezeFrameRecords_(self):
        return self._artop_maxNumberFreezeFrameRecords

    @property
    def significance_(self):
        return self._artop_significance

    @property
    def ref_aging_(self):
        return self._artop_agingRef

    @property
    def aging_(self):
        if self._artop_agingRef is not None:
            if hasattr(self._artop_agingRef, "uuid"):
                return self._artop_agingRef.uuid
        return

    @property
    def extendedDataRecords_DiagnosticExtendedDataRecordRefConditional(self):
        return self._artop_extendedDataRecord

    @property
    def freezeFrames_DiagnosticFreezeFrameRefConditional(self):
        return self._artop_freezeFrame

    @property
    def ref_freezeFrameContent_(self):
        return self._artop_freezeFrameContentRef

    @property
    def freezeFrameContent_(self):
        if self._artop_freezeFrameContentRef is not None:
            if hasattr(self._artop_freezeFrameContentRef, "uuid"):
                return self._artop_freezeFrameContentRef.uuid
        return

    @property
    def ref_freezeFrameContentWwhObd_(self):
        return self._artop_freezeFrameContentWwhObdRef

    @property
    def freezeFrameContentWwhObd_(self):
        if self._artop_freezeFrameContentWwhObdRef is not None:
            if hasattr(self._artop_freezeFrameContentWwhObdRef, "uuid"):
                return self._artop_freezeFrameContentWwhObdRef.uuid
        return

    @property
    def legislatedFreezeFrameContentWwhObds_DiagnosticDataIdentifierSetRefConditional(self):
        return self._artop_legislatedFreezeFrameContentWwhObd

    @property
    def ref_memoryDestinations_(self):
        return self._artop_memoryDestinationRef

    @property
    def memoryDestinations_(self):
        return self._artop_memoryDestinationRef

    @property
    def ref_priority_(self):
        return self._artop_priority

    @property
    def priority_(self):
        if self._artop_priority is not None:
            if hasattr(self._artop_priority, "uuid"):
                return self._artop_priority.uuid
        return

    @property
    def snapshotRecordContents_DiagnosticDataIdentifierSetRefConditional(self):
        return self._artop_snapshotRecordContent
