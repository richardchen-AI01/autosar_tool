# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRoutine.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticRoutine(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .DiagnosticRequestRoutineResults import DiagnosticRequestRoutineResults
        from .DiagnosticStartRoutine import DiagnosticStartRoutine
        from .DiagnosticStopRoutine import DiagnosticStopRoutine
        self._artop_routineInfo = None
        self._artop_id = None
        self._artop_requestResult = None
        self._artop_start = None
        self._artop_stop = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_id': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_requestResult': '"DIAGNOSTIC-REQUEST-ROUTINE-RESULTS"', 
         '_artop_start': '"DIAGNOSTIC-START-ROUTINE"', 
         '_artop_stop': '"DIAGNOSTIC-STOP-ROUTINE"'})

    @property
    def routineInfo_(self):
        return self._artop_routineInfo

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
    def ref_requestResult_(self):
        return self._artop_requestResult

    @property
    def requestResult_(self):
        if self._artop_requestResult is not None:
            if hasattr(self._artop_requestResult, "uuid"):
                return self._artop_requestResult.uuid
        return

    @property
    def ref_start_(self):
        return self._artop_start

    @property
    def start_(self):
        if self._artop_start is not None:
            if hasattr(self._artop_start, "uuid"):
                return self._artop_start.uuid
        return

    @property
    def ref_stop_(self):
        return self._artop_stop

    @property
    def stop_(self):
        if self._artop_stop is not None:
            if hasattr(self._artop_stop, "uuid"):
                return self._artop_stop.uuid
        return
