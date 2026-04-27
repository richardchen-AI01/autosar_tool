# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticParameterIdentifier.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticParameterIdentifier(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameter import DiagnosticParameter
        from .DiagnosticSupportInfoByte import DiagnosticSupportInfoByte
        self._artop_id = None
        self._artop_pidSize = None
        self._artop_dataElement = []
        self._artop_supportInfoByte = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElement':"DIAGNOSTIC-PARAMETER", 
         '_artop_supportInfoByte':"DIAGNOSTIC-SUPPORT-INFO-BYTE"})

    @property
    def id_(self):
        return self._artop_id

    @property
    def pidSize_(self):
        return self._artop_pidSize

    @property
    def dataElements_DiagnosticParameter(self):
        return self._artop_dataElement

    @property
    def ref_supportInfoByte_(self):
        return self._artop_supportInfoByte

    @property
    def supportInfoByte_(self):
        if self._artop_supportInfoByte is not None:
            if hasattr(self._artop_supportInfoByte, "uuid"):
                return self._artop_supportInfoByte.uuid
        return
