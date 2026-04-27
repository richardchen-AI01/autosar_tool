# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRoutineInterface.py
from .DiagnosticAbstractRoutineInterface import DiagnosticAbstractRoutineInterface

class DiagnosticRoutineInterface(DiagnosticAbstractRoutineInterface):

    def __init__(self):
        super().__init__()
        from .ClientServerOperation import ClientServerOperation
        self._artop_requestResult = None
        self._artop_start = None
        self._artop_stop = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_requestResult':"CLIENT-SERVER-OPERATION", 
         '_artop_start':"CLIENT-SERVER-OPERATION", 
         '_artop_stop':"CLIENT-SERVER-OPERATION"})

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
