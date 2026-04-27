# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EcuPartition.py
from .Identifiable import Identifiable

class EcuPartition(Identifiable):

    def __init__(self):
        super().__init__()
        from .EcuInstance import EcuInstance
        self._artop_execInUserMode = None
        self._artop_ecuInstance = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ecuInstance": "ECU-INSTANCE"})

    @property
    def execInUserMode_(self):
        if self._artop_execInUserMode:
            if self._artop_execInUserMode == "true":
                return True
            return False
        else:
            return self._artop_execInUserMode

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstance

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstance is not None:
            if hasattr(self._artop_ecuInstance, "uuid"):
                return self._artop_ecuInstance.uuid
        return
