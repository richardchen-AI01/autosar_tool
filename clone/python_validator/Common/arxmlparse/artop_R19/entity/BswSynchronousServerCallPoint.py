# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswSynchronousServerCallPoint.py
from .BswModuleCallPoint import BswModuleCallPoint

class BswSynchronousServerCallPoint(BswModuleCallPoint):

    def __init__(self):
        super().__init__()
        from .BswModuleClientServerEntry import BswModuleClientServerEntry
        from .ExclusiveAreaNestingOrder import ExclusiveAreaNestingOrder
        self._artop_calledEntryRef = None
        self._artop_calledFromWithinExclusiveAreaRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_calledEntryRef':"BSW-MODULE-CLIENT-SERVER-ENTRY", 
         '_artop_calledFromWithinExclusiveAreaRef':"EXCLUSIVE-AREA-NESTING-ORDER"})

    @property
    def ref_calledEntry_(self):
        return self._artop_calledEntryRef

    @property
    def calledEntry_(self):
        if self._artop_calledEntryRef is not None:
            if hasattr(self._artop_calledEntryRef, "uuid"):
                return self._artop_calledEntryRef.uuid
        return

    @property
    def ref_calledFromWithinExclusiveArea_(self):
        return self._artop_calledFromWithinExclusiveAreaRef

    @property
    def calledFromWithinExclusiveArea_(self):
        if self._artop_calledFromWithinExclusiveAreaRef is not None:
            if hasattr(self._artop_calledFromWithinExclusiveAreaRef, "uuid"):
                return self._artop_calledFromWithinExclusiveAreaRef.uuid
        return
