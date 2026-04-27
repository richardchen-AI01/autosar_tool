# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExternalTriggerOccurredEvent.py
from .RTEEvent import RTEEvent

class ExternalTriggerOccurredEvent(RTEEvent):

    def __init__(self):
        super().__init__()
        from .RTriggerInAtomicSwcInstanceRef import RTriggerInAtomicSwcInstanceRef
        self._artop_triggerIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_triggerIref": "R-TRIGGER-IN-ATOMIC-SWC-INSTANCE-REF"})

    @property
    def ref_trigger_(self):
        return self._artop_triggerIref

    @property
    def trigger_(self):
        if self._artop_triggerIref is not None:
            if hasattr(self._artop_triggerIref, "uuid"):
                return self._artop_triggerIref.uuid
        return
