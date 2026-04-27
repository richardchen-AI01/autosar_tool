# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AssignFrameId.py
from .LinConfigurationEntry import LinConfigurationEntry

class AssignFrameId(LinConfigurationEntry):

    def __init__(self):
        super().__init__()
        from .LinFrameTriggering import LinFrameTriggering
        self._artop_messageId = None
        self._artop_assignedFrameTriggeringRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_assignedFrameTriggeringRef": "LIN-FRAME-TRIGGERING"})

    @property
    def messageId_(self):
        return self._artop_messageId

    @property
    def ref_assignedFrameTriggering_(self):
        return self._artop_assignedFrameTriggeringRef

    @property
    def assignedFrameTriggering_(self):
        if self._artop_assignedFrameTriggeringRef is not None:
            if hasattr(self._artop_assignedFrameTriggeringRef, "uuid"):
                return self._artop_assignedFrameTriggeringRef.uuid
        return
