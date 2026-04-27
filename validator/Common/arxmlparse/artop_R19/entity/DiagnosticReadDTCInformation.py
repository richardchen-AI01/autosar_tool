# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticReadDTCInformation.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticReadDTCInformation(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticReadDTCInformationClass import DiagnosticReadDTCInformationClass
        self._artop_readDtcInformationClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_readDtcInformationClassRef": "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"})

    @property
    def ref_readDTCInformationClass_(self):
        return self._artop_readDtcInformationClassRef

    @property
    def readDTCInformationClass_(self):
        if self._artop_readDtcInformationClassRef is not None:
            if hasattr(self._artop_readDtcInformationClassRef, "uuid"):
                return self._artop_readDtcInformationClassRef.uuid
        return
