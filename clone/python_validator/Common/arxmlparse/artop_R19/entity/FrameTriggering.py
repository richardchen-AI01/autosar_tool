# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FrameTriggering.py
from .Identifiable import Identifiable

class FrameTriggering(Identifiable):

    def __init__(self):
        super().__init__()
        from .PhysicalChannel import PhysicalChannel
        from .FramePort import FramePort
        from .Frame import Frame
        from .PduTriggeringRefConditional import PduTriggeringRefConditional
        from .VariationPoint import VariationPoint
        self._artop_physicalChannel = None
        self._artop_framePortRef = []
        self._artop_frameRef = None
        self._artop_pduTriggering = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_physicalChannel': '"PHYSICAL-CHANNEL"', 
         '_artop_framePortRef': '"FRAME-PORT"', 
         '_artop_frameRef': '"FRAME"', 
         '_artop_pduTriggering': '"PDU-TRIGGERING-REF-CONDITIONAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_physicalChannel_(self):
        return self._artop_physicalChannel

    @property
    def physicalChannel_(self):
        if self._artop_physicalChannel is not None:
            if hasattr(self._artop_physicalChannel, "uuid"):
                return self._artop_physicalChannel.uuid
        return

    @property
    def ref_framePorts_(self):
        return self._artop_framePortRef

    @property
    def framePorts_(self):
        return self._artop_framePortRef

    @property
    def ref_frame_(self):
        return self._artop_frameRef

    @property
    def frame_(self):
        if self._artop_frameRef is not None:
            if hasattr(self._artop_frameRef, "uuid"):
                return self._artop_frameRef.uuid
        return

    @property
    def pduTriggerings_PduTriggeringRefConditional(self):
        return self._artop_pduTriggering

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
