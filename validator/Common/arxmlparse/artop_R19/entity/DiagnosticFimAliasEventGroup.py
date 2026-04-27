# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFimAliasEventGroup.py
from .DiagnosticAbstractAliasEvent import DiagnosticAbstractAliasEvent

class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):

    def __init__(self):
        super().__init__()
        from .DiagnosticFimAliasEvent import DiagnosticFimAliasEvent
        self._artop_groupedAliasEventRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_groupedAliasEventRef": "DIAGNOSTIC-FIM-ALIAS-EVENT"})

    @property
    def ref_groupedAliasEvents_(self):
        return self._artop_groupedAliasEventRef

    @property
    def groupedAliasEvents_(self):
        return self._artop_groupedAliasEventRef
