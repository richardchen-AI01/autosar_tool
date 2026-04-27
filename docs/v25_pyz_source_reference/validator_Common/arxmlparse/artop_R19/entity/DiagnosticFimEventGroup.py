# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticFimEventGroup.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticFimEventGroup(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        from .DiagnosticEvent import DiagnosticEvent
        self._artop_eventRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_eventRef": "DIAGNOSTIC-EVENT"})

    @property
    def ref_events_(self):
        return self._artop_eventRef

    @property
    def events_(self):
        return self._artop_eventRef
