# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTestResultUpdateEnumValueVariationPoint.py
from .AbstractEnumerationValueVariationPoint import AbstractEnumerationValueVariationPoint

class DiagnosticTestResultUpdateEnumValueVariationPoint(AbstractEnumerationValueVariationPoint):

    def __init__(self):
        super().__init__()
        from .DiagnosticTestResult import DiagnosticTestResult
        self._artop_diagnosticTestResult = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticTestResult": "DIAGNOSTIC-TEST-RESULT"})

    @property
    def ref_diagnosticTestResult_(self):
        return self._artop_diagnosticTestResult

    @property
    def diagnosticTestResult_(self):
        if self._artop_diagnosticTestResult is not None:
            if hasattr(self._artop_diagnosticTestResult, "uuid"):
                return self._artop_diagnosticTestResult.uuid
        return
