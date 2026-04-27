# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BusMirrorCanIdToCanIdMapping.py
from .ARObject import ARObject

class BusMirrorCanIdToCanIdMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .BusMirrorChannelMappingCan import BusMirrorChannelMappingCan
        from .CanFrameTriggering import CanFrameTriggering
        self._artop_remappedCanId = None
        self._artop_busMirrorChannelMappingCan = None
        self._artop_souceCanIdRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_busMirrorChannelMappingCan':"BUS-MIRROR-CHANNEL-MAPPING-CAN", 
         '_artop_souceCanIdRef':"CAN-FRAME-TRIGGERING"})

    @property
    def remappedCanId_(self):
        return self._artop_remappedCanId

    @property
    def ref_busMirrorChannelMappingCan_(self):
        return self._artop_busMirrorChannelMappingCan

    @property
    def busMirrorChannelMappingCan_(self):
        if self._artop_busMirrorChannelMappingCan is not None:
            if hasattr(self._artop_busMirrorChannelMappingCan, "uuid"):
                return self._artop_busMirrorChannelMappingCan.uuid
        return

    @property
    def ref_souceCanId_(self):
        return self._artop_souceCanIdRef

    @property
    def souceCanId_(self):
        if self._artop_souceCanIdRef is not None:
            if hasattr(self._artop_souceCanIdRef, "uuid"):
                return self._artop_souceCanIdRef.uuid
        return
