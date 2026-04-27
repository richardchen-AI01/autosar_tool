# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticTestIdentifier.py
from .ARObject import ARObject

class DiagnosticTestIdentifier(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticTestResult import DiagnosticTestResult
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_diagnosticTestResult = None
        self._artop_id = None
        self._artop_uasId = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticTestResult':"DIAGNOSTIC-TEST-RESULT", 
         '_artop_id':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_uasId':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def ref_diagnosticTestResult_(self):
        return self._artop_diagnosticTestResult

    @property
    def diagnosticTestResult_(self):
        if self._artop_diagnosticTestResult is not None:
            if hasattr(self._artop_diagnosticTestResult, "uuid"):
                return self._artop_diagnosticTestResult.uuid
        return

    @property
    def ref_id_(self):
        return self._artop_id

    @property
    def id_(self):
        if self._artop_id is not None:
            if hasattr(self._artop_id, "uuid"):
                return self._artop_id.uuid
        return

    @property
    def ref_uasId_(self):
        return self._artop_uasId

    @property
    def uasId_(self):
        if self._artop_uasId is not None:
            if hasattr(self._artop_uasId, "uuid"):
                return self._artop_uasId.uuid
        return
