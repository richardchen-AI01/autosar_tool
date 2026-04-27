# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRoutineControl.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRoutineControl(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticRoutineControlClass import DiagnosticRoutineControlClass
        from .DiagnosticRoutine import DiagnosticRoutine
        self._artop_routineControlClassRef = None
        self._artop_routineRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_routineControlClassRef':"DIAGNOSTIC-ROUTINE-CONTROL-CLASS", 
         '_artop_routineRef':"DIAGNOSTIC-ROUTINE"})

    @property
    def ref_routineControlClass_(self):
        return self._artop_routineControlClassRef

    @property
    def routineControlClass_(self):
        if self._artop_routineControlClassRef is not None:
            if hasattr(self._artop_routineControlClassRef, "uuid"):
                return self._artop_routineControlClassRef.uuid
        return

    @property
    def ref_routine_(self):
        return self._artop_routineRef

    @property
    def routine_(self):
        if self._artop_routineRef is not None:
            if hasattr(self._artop_routineRef, "uuid"):
                return self._artop_routineRef.uuid
        return
