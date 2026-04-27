# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanNmNode.py
from .NmNode import NmNode

class CanNmNode(NmNode):

    def __init__(self):
        super().__init__()
        from .CanNmRangeConfig import CanNmRangeConfig
        self._artop_allNmMessagesKeepAwake = None
        self._artop_nmCarWakeUpFilterEnabled = None
        self._artop_nmCarWakeUpRxEnabled = None
        self._artop_nmMsgCycleOffset = None
        self._artop_nmMsgReducedTime = None
        self._artop_nmRangeConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_nmRangeConfig": "CAN-NM-RANGE-CONFIG"})

    @property
    def allNmMessagesKeepAwake_(self):
        if self._artop_allNmMessagesKeepAwake:
            if self._artop_allNmMessagesKeepAwake == "true":
                return True
            return False
        else:
            return self._artop_allNmMessagesKeepAwake

    @property
    def nmCarWakeUpFilterEnabled_(self):
        if self._artop_nmCarWakeUpFilterEnabled:
            if self._artop_nmCarWakeUpFilterEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmCarWakeUpFilterEnabled

    @property
    def nmCarWakeUpRxEnabled_(self):
        if self._artop_nmCarWakeUpRxEnabled:
            if self._artop_nmCarWakeUpRxEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmCarWakeUpRxEnabled

    @property
    def nmMsgCycleOffset_(self):
        return self._artop_nmMsgCycleOffset

    @property
    def nmMsgReducedTime_(self):
        return self._artop_nmMsgReducedTime

    @property
    def ref_nmRangeConfig_(self):
        return self._artop_nmRangeConfig

    @property
    def nmRangeConfig_(self):
        if self._artop_nmRangeConfig is not None:
            if hasattr(self._artop_nmRangeConfig, "uuid"):
                return self._artop_nmRangeConfig.uuid
        return
