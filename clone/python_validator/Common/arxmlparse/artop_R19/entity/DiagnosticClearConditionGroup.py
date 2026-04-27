# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticClearConditionGroup.py
from .DiagnosticConditionGroup import DiagnosticConditionGroup

class DiagnosticClearConditionGroup(DiagnosticConditionGroup):

    def __init__(self):
        super().__init__()
        from .DiagnosticClearCondition import DiagnosticClearCondition
        self._artop_clearConditionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_clearConditionRef": "DIAGNOSTIC-CLEAR-CONDITION"})

    @property
    def ref_clearConditions_(self):
        return self._artop_clearConditionRef

    @property
    def clearConditions_(self):
        return self._artop_clearConditionRef
