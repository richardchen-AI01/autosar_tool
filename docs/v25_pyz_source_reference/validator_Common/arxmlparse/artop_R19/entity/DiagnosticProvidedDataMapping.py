# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticProvidedDataMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticProvidedDataMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataElement import DiagnosticDataElement
        self._artop_dataProvider = None
        self._artop_dataElementRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataElementRef": "DIAGNOSTIC-DATA-ELEMENT"})

    @property
    def dataProvider_(self):
        return self._artop_dataProvider

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return
