# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationModeRequestPhmActionItem.py
from .PhmActionItem import PhmActionItem

class ApplicationModeRequestPhmActionItem(PhmActionItem):

    def __init__(self):
        super().__init__()
        from .ModeInProcessInstanceRef import ModeInProcessInstanceRef
        self._artop_requestedModeIref = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_requestedModeIref": "MODE-IN-PROCESS-INSTANCE-REF-IREF"})

    @property
    def ref_requestedMode_(self):
        return self._artop_requestedModeIref

    @property
    def requestedMode_(self):
        if self._artop_requestedModeIref is not None:
            if hasattr(self._artop_requestedModeIref, "uuid"):
                return self._artop_requestedModeIref.uuid
        return
