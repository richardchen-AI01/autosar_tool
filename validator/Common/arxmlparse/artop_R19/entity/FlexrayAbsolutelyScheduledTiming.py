# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayAbsolutelyScheduledTiming.py
from .ARObject import ARObject

class FlexrayAbsolutelyScheduledTiming(ARObject):

    def __init__(self):
        super().__init__()
        from .FlexrayFrameTriggering import FlexrayFrameTriggering
        from .CommunicationCycle import CommunicationCycle
        self._artop_slotId = None
        self._artop_flexrayFrameTriggering = None
        self._artop_communicationCycle = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flexrayFrameTriggering':"FLEXRAY-FRAME-TRIGGERING", 
         '_artop_communicationCycle':"COMMUNICATION-CYCLE"})

    @property
    def slotId_(self):
        return self._artop_slotId

    @property
    def ref_flexrayFrameTriggering_(self):
        return self._artop_flexrayFrameTriggering

    @property
    def flexrayFrameTriggering_(self):
        if self._artop_flexrayFrameTriggering is not None:
            if hasattr(self._artop_flexrayFrameTriggering, "uuid"):
                return self._artop_flexrayFrameTriggering.uuid
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
