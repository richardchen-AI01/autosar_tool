# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestControlOfOnBoardDevice.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticRequestControlOfOnBoardDeviceClass import DiagnosticRequestControlOfOnBoardDeviceClass
        from .DiagnosticTestRoutineIdentifier import DiagnosticTestRoutineIdentifier
        self._artop_requestControlOfOnBoardDeviceClassRef = None
        self._artop_testIdRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_requestControlOfOnBoardDeviceClassRef':"DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS", 
         '_artop_testIdRef':"DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"})

    @property
    def ref_requestControlOfOnBoardDeviceClass_(self):
        return self._artop_requestControlOfOnBoardDeviceClassRef

    @property
    def requestControlOfOnBoardDeviceClass_(self):
        if self._artop_requestControlOfOnBoardDeviceClassRef is not None:
            if hasattr(self._artop_requestControlOfOnBoardDeviceClassRef, "uuid"):
                return self._artop_requestControlOfOnBoardDeviceClassRef.uuid
        return

    @property
    def ref_testId_(self):
        return self._artop_testIdRef

    @property
    def testId_(self):
        if self._artop_testIdRef is not None:
            if hasattr(self._artop_testIdRef, "uuid"):
                return self._artop_testIdRef.uuid
        return
