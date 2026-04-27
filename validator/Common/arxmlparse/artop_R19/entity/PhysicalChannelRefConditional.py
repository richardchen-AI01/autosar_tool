# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhysicalChannelRefConditional.py
from .ARObject import ARObject

class PhysicalChannelRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .BusMirrorChannel import BusMirrorChannel
        from .PhysicalChannel import PhysicalChannel
        from .VariationPoint import VariationPoint
        self._artop_busMirrorChannel = None
        self._artop_physicalChannelRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_busMirrorChannel':"BUS-MIRROR-CHANNEL", 
         '_artop_physicalChannelRef':"PHYSICAL-CHANNEL", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_busMirrorChannel_(self):
        return self._artop_busMirrorChannel

    @property
    def busMirrorChannel_(self):
        if self._artop_busMirrorChannel is not None:
            if hasattr(self._artop_busMirrorChannel, "uuid"):
                return self._artop_busMirrorChannel.uuid
        return

    @property
    def ref_physicalChannel_(self):
        return self._artop_physicalChannelRef

    @property
    def physicalChannel_(self):
        if self._artop_physicalChannelRef is not None:
            if hasattr(self._artop_physicalChannelRef, "uuid"):
                return self._artop_physicalChannelRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
