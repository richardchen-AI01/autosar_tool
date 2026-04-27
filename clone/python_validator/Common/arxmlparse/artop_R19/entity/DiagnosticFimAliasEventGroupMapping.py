# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFimAliasEventGroupMapping.py
from .DiagnosticMapping import DiagnosticMapping

class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):

    def __init__(self):
        super().__init__()
        from .DiagnosticFimEventGroup import DiagnosticFimEventGroup
        from .DiagnosticFimAliasEventGroup import DiagnosticFimAliasEventGroup
        self._artop_actualEventRef = None
        self._artop_aliasEventRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_actualEventRef':"DIAGNOSTIC-FIM-EVENT-GROUP", 
         '_artop_aliasEventRef':"DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP"})

    @property
    def ref_actualEvent_(self):
        return self._artop_actualEventRef

    @property
    def actualEvent_(self):
        if self._artop_actualEventRef is not None:
            if hasattr(self._artop_actualEventRef, "uuid"):
                return self._artop_actualEventRef.uuid
        return

    @property
    def ref_aliasEvent_(self):
        return self._artop_aliasEventRef

    @property
    def aliasEvent_(self):
        if self._artop_aliasEventRef is not None:
            if hasattr(self._artop_aliasEventRef, "uuid"):
                return self._artop_aliasEventRef.uuid
        return
