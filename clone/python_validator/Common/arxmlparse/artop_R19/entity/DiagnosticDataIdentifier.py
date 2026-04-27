# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDataIdentifier.py
from .DiagnosticAbstractDataIdentifier import DiagnosticAbstractDataIdentifier

class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):

    def __init__(self):
        super().__init__()
        from .DiagnosticParameter import DiagnosticParameter
        from .DiagnosticSupportInfoByte import DiagnosticSupportInfoByte
        self._artop_didSize = None
        self._artop_representsVin = None
        self._artop_dataElement = []
        self._artop_supportInfoByte = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_dataElement':"DIAGNOSTIC-PARAMETER", 
         '_artop_supportInfoByte':"DIAGNOSTIC-SUPPORT-INFO-BYTE"})

    @property
    def didSize_(self):
        return self._artop_didSize

    @property
    def representsVin_(self):
        if self._artop_representsVin:
            if self._artop_representsVin == "true":
                return True
            return False
        else:
            return self._artop_representsVin

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
