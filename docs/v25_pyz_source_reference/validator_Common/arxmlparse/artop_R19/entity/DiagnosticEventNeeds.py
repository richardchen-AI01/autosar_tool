# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticEventNeeds.py
from .DiagnosticCapabilityElement import DiagnosticCapabilityElement

class DiagnosticEventNeeds(DiagnosticCapabilityElement):

    def __init__(self):
        super().__init__()
        from .FunctionInhibitionNeeds import FunctionInhibitionNeeds
        from .DiagEventDebounceAlgorithm import DiagEventDebounceAlgorithm
        self._artop_considerPtoStatus = None
        self._artop_dtcKind = None
        self._artop_dtcNumber = None
        self._artop_obdDtcNumber = None
        self._artop_prestoredFreezeframeStoredInNvm = None
        self._artop_reportBehavior = None
        self._artop_udsDtcNumber = None
        self._artop_usesMonitorData = None
        self._artop_deferringFidRef = []
        self._artop_diagEventDebounceAlgorithm = None
        self._artop_inhibitingFidRef = None
        self._artop_inhibitingSecondaryFidRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_deferringFidRef': '"FUNCTION-INHIBITION-NEEDS"', 
         '_artop_diagEventDebounceAlgorithm': '"DIAG-EVENT-DEBOUNCE-ALGORITHM"', 
         '_artop_inhibitingFidRef': '"FUNCTION-INHIBITION-NEEDS"', 
         '_artop_inhibitingSecondaryFidRef': '"FUNCTION-INHIBITION-NEEDS"'})

    @property
    def considerPtoStatus_(self):
        if self._artop_considerPtoStatus:
            if self._artop_considerPtoStatus == "true":
                return True
            return False
        else:
            return self._artop_considerPtoStatus

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
    def prestoredFreezeframeStoredInNvm_(self):
        if self._artop_prestoredFreezeframeStoredInNvm:
            if self._artop_prestoredFreezeframeStoredInNvm == "true":
                return True
            return False
        else:
            return self._artop_prestoredFreezeframeStoredInNvm

    @property
    def reportBehavior_(self):
        return self._artop_reportBehavior

    @property
    def udsDtcNumber_(self):
        return self._artop_udsDtcNumber

    @property
    def usesMonitorData_(self):
        if self._artop_usesMonitorData:
            if self._artop_usesMonitorData == "true":
                return True
            return False
        else:
            return self._artop_usesMonitorData

    @property
    def ref_deferringFids_(self):
        return self._artop_deferringFidRef

    @property
    def deferringFids_(self):
        return self._artop_deferringFidRef

    @property
    def ref_diagEventDebounceAlgorithm_(self):
        return self._artop_diagEventDebounceAlgorithm

    @property
    def diagEventDebounceAlgorithm_(self):
        if self._artop_diagEventDebounceAlgorithm is not None:
            if hasattr(self._artop_diagEventDebounceAlgorithm, "uuid"):
                return self._artop_diagEventDebounceAlgorithm.uuid
        return

    @property
    def ref_inhibitingFid_(self):
        return self._artop_inhibitingFidRef

    @property
    def inhibitingFid_(self):
        if self._artop_inhibitingFidRef is not None:
            if hasattr(self._artop_inhibitingFidRef, "uuid"):
                return self._artop_inhibitingFidRef.uuid
        return

    @property
    def ref_inhibitingSecondaryFids_(self):
        return self._artop_inhibitingSecondaryFidRef

    @property
    def inhibitingSecondaryFids_(self):
        return self._artop_inhibitingSecondaryFidRef
