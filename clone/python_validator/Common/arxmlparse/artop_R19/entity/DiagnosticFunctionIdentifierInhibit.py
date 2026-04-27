# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFunctionIdentifierInhibit.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticFunctionIdentifier import DiagnosticFunctionIdentifier
        from .DiagnosticFunctionInhibitSource import DiagnosticFunctionInhibitSource
        self._artop_inhibitionMask = None
        self._artop_functionIdentifierRef = None
        self._artop_inhibitSource = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_functionIdentifierRef':"DIAGNOSTIC-FUNCTION-IDENTIFIER", 
         '_artop_inhibitSource':"DIAGNOSTIC-FUNCTION-INHIBIT-SOURCE"})

    @property
    def inhibitionMask_(self):
        return self._artop_inhibitionMask

    @property
    def ref_functionIdentifier_(self):
        return self._artop_functionIdentifierRef

    @property
    def functionIdentifier_(self):
        if self._artop_functionIdentifierRef is not None:
            if hasattr(self._artop_functionIdentifierRef, "uuid"):
                return self._artop_functionIdentifierRef.uuid
        return

    @property
    def inhibitSources_DiagnosticFunctionInhibitSource(self):
        return self._artop_inhibitSource
