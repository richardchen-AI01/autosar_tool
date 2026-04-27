# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswAsynchronousServerCallPoint.py
from .BswModuleCallPoint import BswModuleCallPoint

class BswAsynchronousServerCallPoint(BswModuleCallPoint):

    def __init__(self):
        super().__init__()
        from .BswModuleClientServerEntry import BswModuleClientServerEntry
        self._artop_calledEntryRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_calledEntryRef": "BSW-MODULE-CLIENT-SERVER-ENTRY"})

    @property
    def ref_calledEntry_(self):
        return self._artop_calledEntryRef

    @property
    def calledEntry_(self):
        if self._artop_calledEntryRef is not None:
            if hasattr(self._artop_calledEntryRef, "uuid"):
                return self._artop_calledEntryRef.uuid
        return
