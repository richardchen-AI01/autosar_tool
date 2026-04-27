# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticParameterSupportInfo.py
from .ARObject import ARObject

class DiagnosticParameterSupportInfo(ARObject):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameter import DiagnosticParameter
        self._artop_supportInfoBit = None
        self._artop_diagnosticParameter = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_diagnosticParameter": "DIAGNOSTIC-PARAMETER"})

    @property
    def supportInfoBit_(self):
        return self._artop_supportInfoBit

    @property
    def ref_diagnosticParameter_(self):
        return self._artop_diagnosticParameter

    @property
    def diagnosticParameter_(self):
        if self._artop_diagnosticParameter is not None:
            if hasattr(self._artop_diagnosticParameter, "uuid"):
                return self._artop_diagnosticParameter.uuid
        return
