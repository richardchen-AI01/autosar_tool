# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventTrigger.py
from .TDEventVfbPort import TDEventVfbPort

class TDEventTrigger(TDEventVfbPort):

    def __init__(self):
        super().__init__()
        from .Trigger import Trigger
        self._artop_tdEventTriggerType = None
        self._artop_triggerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_triggerRef": "TRIGGER"})

    @property
    def tdEventTriggerType_(self):
        return self._artop_tdEventTriggerType

    @property
    def ref_trigger_(self):
        return self._artop_triggerRef

    @property
    def trigger_(self):
        if self._artop_triggerRef is not None:
            if hasattr(self._artop_triggerRef, "uuid"):
                return self._artop_triggerRef.uuid
        return
