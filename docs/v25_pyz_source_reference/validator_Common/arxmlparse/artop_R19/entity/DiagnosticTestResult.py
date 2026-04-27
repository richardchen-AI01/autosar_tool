# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTestResult.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticTestResult(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticEventRefConditional import DiagnosticEventRefConditional
        from .DiagnosticEvent import DiagnosticEvent
        from .DiagnosticMeasurementIdentifier import DiagnosticMeasurementIdentifier
        from .DiagnosticTestIdentifier import DiagnosticTestIdentifier
        from .DiagnosticTestResultUpdateEnumValueVariationPoint import DiagnosticTestResultUpdateEnumValueVariationPoint
        self._artop_diagnosticEvent = []
        self._artop_eventRef = None
        self._artop_monitoredIdentifierRef = None
        self._artop_testIdentifier = None
        self._artop_updateKind = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_diagnosticEvent': '"DIAGNOSTIC-EVENT-REF-CONDITIONAL"', 
         '_artop_eventRef': '"DIAGNOSTIC-EVENT"', 
         '_artop_monitoredIdentifierRef': '"DIAGNOSTIC-MEASUREMENT-IDENTIFIER"', 
         '_artop_testIdentifier': '"DIAGNOSTIC-TEST-IDENTIFIER"', 
         '_artop_updateKind': '"DIAGNOSTIC-TEST-RESULT-UPDATE-ENUM-VALUE-VARIATION-POINT"'})

    @property
    def diagnosticEvents_DiagnosticEventRefConditional(self):
        return self._artop_diagnosticEvent

    @property
    def ref_event_(self):
        return self._artop_eventRef

    @property
    def event_(self):
        if self._artop_eventRef is not None:
            if hasattr(self._artop_eventRef, "uuid"):
                return self._artop_eventRef.uuid
        return

    @property
    def ref_monitoredIdentifier_(self):
        return self._artop_monitoredIdentifierRef

    @property
    def monitoredIdentifier_(self):
        if self._artop_monitoredIdentifierRef is not None:
            if hasattr(self._artop_monitoredIdentifierRef, "uuid"):
                return self._artop_monitoredIdentifierRef.uuid
        return

    @property
    def ref_testIdentifier_(self):
        return self._artop_testIdentifier

    @property
    def testIdentifier_(self):
        if self._artop_testIdentifier is not None:
            if hasattr(self._artop_testIdentifier, "uuid"):
                return self._artop_testIdentifier.uuid
        return

    @property
    def ref_updateKind_(self):
        return self._artop_updateKind

    @property
    def updateKind_(self):
        if self._artop_updateKind is not None:
            if hasattr(self._artop_updateKind, "uuid"):
                return self._artop_updateKind.uuid
        return
