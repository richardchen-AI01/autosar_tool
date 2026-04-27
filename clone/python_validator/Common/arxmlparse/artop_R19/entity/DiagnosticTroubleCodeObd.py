# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeObd.py
from .DiagnosticTroubleCode import DiagnosticTroubleCode

class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):

    def __init__(self):
        super().__init__()
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        from .DiagnosticTroubleCodeProps import DiagnosticTroubleCodeProps
        from .NameTokenValueVariationPoint import NameTokenValueVariationPoint
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_considerPtoStatus = None
        self._artop_dtcPropsRef = None
        self._artop_eventObdReadinessGroup = None
        self._artop_obdDtcValue = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_considerPtoStatus': '"BOOLEAN-VALUE-VARIATION-POINT"', 
         '_artop_dtcPropsRef': '"DIAGNOSTIC-TROUBLE-CODE-PROPS"', 
         '_artop_eventObdReadinessGroup': '"NAME-TOKEN-VALUE-VARIATION-POINT"', 
         '_artop_obdDtcValue': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"'})

    @property
    def ref_considerPtoStatus_(self):
        return self._artop_considerPtoStatus

    @property
    def considerPtoStatus_(self):
        if self._artop_considerPtoStatus is not None:
            if hasattr(self._artop_considerPtoStatus, "uuid"):
                return self._artop_considerPtoStatus.uuid
        return

    @property
    def ref_dtcProps_(self):
        return self._artop_dtcPropsRef

    @property
    def dtcProps_(self):
        if self._artop_dtcPropsRef is not None:
            if hasattr(self._artop_dtcPropsRef, "uuid"):
                return self._artop_dtcPropsRef.uuid
        return

    @property
    def ref_eventObdReadinessGroup_(self):
        return self._artop_eventObdReadinessGroup

    @property
    def eventObdReadinessGroup_(self):
        if self._artop_eventObdReadinessGroup is not None:
            if hasattr(self._artop_eventObdReadinessGroup, "uuid"):
                return self._artop_eventObdReadinessGroup.uuid
        return

    @property
    def ref_obdDTCValue_(self):
        return self._artop_obdDtcValue

    @property
    def obdDTCValue_(self):
        if self._artop_obdDtcValue is not None:
            if hasattr(self._artop_obdDtcValue, "uuid"):
                return self._artop_obdDtcValue.uuid
        return
