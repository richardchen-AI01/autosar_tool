# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TtcanAbsolutelyScheduledTiming.py
from .ARObject import ARObject

class TtcanAbsolutelyScheduledTiming(ARObject):

    def __init__(self):
        super().__init__()
        from .CanFrameTriggering import CanFrameTriggering
        from .CommunicationCycle import CommunicationCycle
        self._artop_timeMark = None
        self._artop_trigger = None
        self._artop_canFrameTriggering = None
        self._artop_communicationCycle = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_canFrameTriggering':"CAN-FRAME-TRIGGERING", 
         '_artop_communicationCycle':"COMMUNICATION-CYCLE"})

    @property
    def timeMark_(self):
        if self._artop_timeMark:
            return int(self._artop_timeMark)
        return self._artop_timeMark

    @property
    def trigger_(self):
        return self._artop_trigger

    @property
    def ref_canFrameTriggering_(self):
        return self._artop_canFrameTriggering

    @property
    def canFrameTriggering_(self):
        if self._artop_canFrameTriggering is not None:
            if hasattr(self._artop_canFrameTriggering, "uuid"):
                return self._artop_canFrameTriggering.uuid
        return

    @property
    def ref_communicationCycle_(self):
        return self._artop_communicationCycle

    @property
    def communicationCycle_(self):
        if self._artop_communicationCycle is not None:
            if hasattr(self._artop_communicationCycle, "uuid"):
                return self._artop_communicationCycle.uuid
        return
