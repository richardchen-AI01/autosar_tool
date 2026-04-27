# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTroubleCodeUds.py
from .DiagnosticTroubleCode import DiagnosticTroubleCode

class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):

    def __init__(self):
        super().__init__()
        from .DiagnosticTroubleCodeProps import DiagnosticTroubleCodeProps
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .DiagnosticWwhObdDtcClassEnumValueVariationPoint import DiagnosticWwhObdDtcClassEnumValueVariationPoint
        self._artop_considerPtoStatus = None
        self._artop_eventObdReadinessGroup = None
        self._artop_functionalUnit = None
        self._artop_severity = None
        self._artop_dtcPropsRef = None
        self._artop_udsDtcValue = None
        self._artop_wwhObdDtcClass = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dtcPropsRef':"DIAGNOSTIC-TROUBLE-CODE-PROPS", 
         '_artop_udsDtcValue':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_wwhObdDtcClass':"DIAGNOSTIC-WWH-OBD-DTC-CLASS-ENUM-VALUE-VARIATION-POINT"})

    @property
    def considerPtoStatus_(self):
        if self._artop_considerPtoStatus:
            if self._artop_considerPtoStatus == "true":
                return True
            return False
        else:
            return self._artop_considerPtoStatus

    @property
    def eventObdReadinessGroup_(self):
        return self._artop_eventObdReadinessGroup

    @property
    def functionalUnit_(self):
        return self._artop_functionalUnit

    @property
    def severity_(self):
        return self._artop_severity

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
    def ref_udsDtcValue_(self):
        return self._artop_udsDtcValue

    @property
    def udsDtcValue_(self):
        if self._artop_udsDtcValue is not None:
            if hasattr(self._artop_udsDtcValue, "uuid"):
                return self._artop_udsDtcValue.uuid
        return

    @property
    def ref_wwhObdDtcClass_(self):
        return self._artop_wwhObdDtcClass

    @property
    def wwhObdDtcClass_(self):
        if self._artop_wwhObdDtcClass is not None:
            if hasattr(self._artop_wwhObdDtcClass, "uuid"):
                return self._artop_wwhObdDtcClass.uuid
        return
