# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestOnBoardMonitoringTestResults.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticTestResult import DiagnosticTestResult
        from .DiagnosticRequestOnBoardMonitoringTestResultsClass import DiagnosticRequestOnBoardMonitoringTestResultsClass
        self._artop_diagnosticTestResultRef = []
        self._artop_requestOnBoardMonitoringTestResultsClassRef = None
        self._artop_testResultRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_diagnosticTestResultRef':"DIAGNOSTIC-TEST-RESULT", 
         '_artop_requestOnBoardMonitoringTestResultsClassRef':"DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS", 
         '_artop_testResultRef':"DIAGNOSTIC-TEST-RESULT"})

    @property
    def ref_diagnosticTestResults_(self):
        return self._artop_diagnosticTestResultRef

    @property
    def diagnosticTestResults_(self):
        return self._artop_diagnosticTestResultRef

    @property
    def ref_requestOnBoardMonitoringTestResultsClass_(self):
        return self._artop_requestOnBoardMonitoringTestResultsClassRef

    @property
    def requestOnBoardMonitoringTestResultsClass_(self):
        if self._artop_requestOnBoardMonitoringTestResultsClassRef is not None:
            if hasattr(self._artop_requestOnBoardMonitoringTestResultsClassRef, "uuid"):
                return self._artop_requestOnBoardMonitoringTestResultsClassRef.uuid
        return

    @property
    def ref_testResult_(self):
        return self._artop_testResultRef

    @property
    def testResult_(self):
        if self._artop_testResultRef is not None:
            if hasattr(self._artop_testResultRef, "uuid"):
                return self._artop_testResultRef.uuid
        return
