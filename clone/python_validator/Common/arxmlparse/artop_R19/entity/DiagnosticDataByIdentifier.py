# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDataByIdentifier.py
from .DiagnosticServiceInstance import DiagnosticServiceInstance

class DiagnosticDataByIdentifier(DiagnosticServiceInstance):

    def __init__(self):
        super().__init__()
        from .DiagnosticAbstractDataIdentifier import DiagnosticAbstractDataIdentifier
        self._artop_dataIdentifierRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataIdentifierRef": "DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER"})

    @property
    def ref_dataIdentifier_(self):
        return self._artop_dataIdentifierRef

    @property
    def dataIdentifier_(self):
        if self._artop_dataIdentifierRef is not None:
            if hasattr(self._artop_dataIdentifierRef, "uuid"):
                return self._artop_dataIdentifierRef.uuid
        return
