# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeSwitchedAckEvent.py
from .RTEEvent import RTEEvent

class ModeSwitchedAckEvent(RTEEvent):

    def __init__(self):
        super().__init__()
        from .ModeSwitchPoint import ModeSwitchPoint
        self._artop_eventSourceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_eventSourceRef": "MODE-SWITCH-POINT"})

    @property
    def ref_eventSource_(self):
        return self._artop_eventSourceRef

    @property
    def eventSource_(self):
        if self._artop_eventSourceRef is not None:
            if hasattr(self._artop_eventSourceRef, "uuid"):
                return self._artop_eventSourceRef.uuid
        return
