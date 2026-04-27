# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SegmentPosition.py
from .ARObject import ARObject

class SegmentPosition(ARObject):

    def __init__(self):
        super().__init__()
        from .MultiplexedPart import MultiplexedPart
        self._artop_segmentByteOrder = None
        self._artop_segmentLength = None
        self._artop_segmentPosition = None
        self._artop_multiplexedPart = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_multiplexedPart": "MULTIPLEXED-PART"})

    @property
    def segmentByteOrder_(self):
        return self._artop_segmentByteOrder

    @property
    def segmentLength_(self):
        if self._artop_segmentLength:
            return int(self._artop_segmentLength)
        return self._artop_segmentLength

    @property
    def segmentPosition_(self):
        if self._artop_segmentPosition:
            return int(self._artop_segmentPosition)
        return self._artop_segmentPosition

    @property
    def ref_multiplexedPart_(self):
        return self._artop_multiplexedPart

    @property
    def multiplexedPart_(self):
        if self._artop_multiplexedPart is not None:
            if hasattr(self._artop_multiplexedPart, "uuid"):
                return self._artop_multiplexedPart.uuid
        return
