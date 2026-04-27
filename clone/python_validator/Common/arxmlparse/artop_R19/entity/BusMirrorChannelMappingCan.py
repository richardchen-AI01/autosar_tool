# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BusMirrorChannelMappingCan.py
from .BusMirrorChannelMapping import BusMirrorChannelMapping

class BusMirrorChannelMappingCan(BusMirrorChannelMapping):

    def __init__(self):
        super().__init__()
        from .BusMirrorCanIdRangeMapping import BusMirrorCanIdRangeMapping
        from .BusMirrorCanIdToCanIdMapping import BusMirrorCanIdToCanIdMapping
        from .BusMirrorLinPidToCanIdMapping import BusMirrorLinPidToCanIdMapping
        self._artop_mirrorSourceLinToCanRangeBaseId = None
        self._artop_mirrorStatusCanId = None
        self._artop_canIdRangeMapping = []
        self._artop_canIdToCanIdMapping = []
        self._artop_linPidToCanIdMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_canIdRangeMapping':"BUS-MIRROR-CAN-ID-RANGE-MAPPING", 
         '_artop_canIdToCanIdMapping':"BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING", 
         '_artop_linPidToCanIdMapping':"BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING"})

    @property
    def mirrorSourceLinToCanRangeBaseId_(self):
        return self._artop_mirrorSourceLinToCanRangeBaseId

    @property
    def mirrorStatusCanId_(self):
        return self._artop_mirrorStatusCanId

    @property
    def canIdRangeMappings_BusMirrorCanIdRangeMapping(self):
        return self._artop_canIdRangeMapping

    @property
    def canIdToCanIdMappings_BusMirrorCanIdToCanIdMapping(self):
        return self._artop_canIdToCanIdMapping

    @property
    def linPidToCanIdMappings_BusMirrorLinPidToCanIdMapping(self):
        return self._artop_linPidToCanIdMapping
