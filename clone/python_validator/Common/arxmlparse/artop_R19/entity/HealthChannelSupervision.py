# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HealthChannelSupervision.py
from .HealthChannel import HealthChannel

class HealthChannelSupervision(HealthChannel):

    def __init__(self):
        super().__init__()
        from .PhmSupervision import PhmSupervision
        self._artop_supervisionCondition = None
        self._artop_supervisionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_supervisionRef": "PHM-SUPERVISION"})

    @property
    def supervisionCondition_(self):
        return self._artop_supervisionCondition

    @property
    def ref_supervision_(self):
        return self._artop_supervisionRef

    @property
    def supervision_(self):
        if self._artop_supervisionRef is not None:
            if hasattr(self._artop_supervisionRef, "uuid"):
                return self._artop_supervisionRef.uuid
        return
