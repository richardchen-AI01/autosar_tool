# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticInfoType.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticInfoType(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameter import DiagnosticParameter
        self._artop_id = None
        self._artop_dataElement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataElement": "DIAGNOSTIC-PARAMETER"})

    @property
    def id_(self):
        return self._artop_id

    @property
    def dataElements_DiagnosticParameter(self):
        return self._artop_dataElement
