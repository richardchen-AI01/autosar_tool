# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswOperationInvokedEvent.py
from .BswEvent import BswEvent

class BswOperationInvokedEvent(BswEvent):

    def __init__(self):
        super().__init__()
        from .BswModuleClientServerEntry import BswModuleClientServerEntry
        self._artop_entryRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_entryRef": "BSW-MODULE-CLIENT-SERVER-ENTRY"})

    @property
    def ref_entry_(self):
        return self._artop_entryRef

    @property
    def entry_(self):
        if self._artop_entryRef is not None:
            if hasattr(self._artop_entryRef, "uuid"):
                return self._artop_entryRef.uuid
        return
