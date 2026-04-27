# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BusMirrorCanIdRangeMapping.py
from .ARObject import ARObject

class BusMirrorCanIdRangeMapping(ARObject):

    def __init__(self):
        super().__init__()
        from .BusMirrorChannelMappingCan import BusMirrorChannelMappingCan
        self._artop_destinationBaseId = None
        self._artop_sourceCanIdCode = None
        self._artop_sourceCanIdMask = None
        self._artop_busMirrorChannelMappingCan = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_busMirrorChannelMappingCan": "BUS-MIRROR-CHANNEL-MAPPING-CAN"})

    @property
    def destinationBaseId_(self):
        return self._artop_destinationBaseId

    @property
    def sourceCanIdCode_(self):
        return self._artop_sourceCanIdCode

    @property
    def sourceCanIdMask_(self):
        return self._artop_sourceCanIdMask

    @property
    def ref_busMirrorChannelMappingCan_(self):
        return self._artop_busMirrorChannelMappingCan

    @property
    def busMirrorChannelMappingCan_(self):
        if self._artop_busMirrorChannelMappingCan is not None:
            if hasattr(self._artop_busMirrorChannelMappingCan, "uuid"):
                return self._artop_busMirrorChannelMappingCan.uuid
        return
