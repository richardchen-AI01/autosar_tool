# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticRequestCurrentPowertrainData.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameterIdentifier import DiagnosticParameterIdentifier
        from .DiagnosticRequestCurrentPowertrainDataClass import DiagnosticRequestCurrentPowertrainDataClass
        self._artop_pidRef = None
        self._artop_requestCurrentPowertrainDiagnosticDataClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_pidRef':"DIAGNOSTIC-PARAMETER-IDENTIFIER", 
         '_artop_requestCurrentPowertrainDiagnosticDataClassRef':"DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"})

    @property
    def ref_pid_(self):
        return self._artop_pidRef

    @property
    def pid_(self):
        if self._artop_pidRef is not None:
            if hasattr(self._artop_pidRef, "uuid"):
                return self._artop_pidRef.uuid
        return

    @property
    def ref_requestCurrentPowertrainDiagnosticDataClass_(self):
        return self._artop_requestCurrentPowertrainDiagnosticDataClassRef

    @property
    def requestCurrentPowertrainDiagnosticDataClass_(self):
        if self._artop_requestCurrentPowertrainDiagnosticDataClassRef is not None:
            if hasattr(self._artop_requestCurrentPowertrainDiagnosticDataClassRef, "uuid"):
                return self._artop_requestCurrentPowertrainDiagnosticDataClassRef.uuid
        return
