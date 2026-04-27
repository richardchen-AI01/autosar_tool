# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticDataIdentifierSet.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticDataIdentifierSet(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticDataIdentifier import DiagnosticDataIdentifier
        self._artop_dataIdentifierRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dataIdentifierRef": "DIAGNOSTIC-DATA-IDENTIFIER"})

    @property
    def ref_dataIdentifiers_(self):
        return self._artop_dataIdentifierRef

    @property
    def dataIdentifiers_(self):
        return self._artop_dataIdentifierRef
