# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticReadScalingDataByIdentifier.py
from .DiagnosticDataByIdentifier import DiagnosticDataByIdentifier

class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):

    def __init__(self):
        super().__init__()
        from .DiagnosticReadScalingDataByIdentifierClass import DiagnosticReadScalingDataByIdentifierClass
        self._artop_readScalingDataClassRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_readScalingDataClassRef": "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"})

    @property
    def ref_readScalingDataClass_(self):
        return self._artop_readScalingDataClassRef

    @property
    def readScalingDataClass_(self):
        if self._artop_readScalingDataClassRef is not None:
            if hasattr(self._artop_readScalingDataClassRef, "uuid"):
                return self._artop_readScalingDataClassRef.uuid
        return
