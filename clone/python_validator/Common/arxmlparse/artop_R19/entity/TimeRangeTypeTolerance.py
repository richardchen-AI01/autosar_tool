# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeRangeTypeTolerance.py
from .ARObject import ARObject

class TimeRangeTypeTolerance(ARObject):

    def __init__(self):
        super().__init__()
        from .TimeRangeType import TimeRangeType
        self._artop_timeRangeType = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_timeRangeType": "TIME-RANGE-TYPE"})

    @property
    def ref_timeRangeType_(self):
        return self._artop_timeRangeType

    @property
    def timeRangeType_(self):
        if self._artop_timeRangeType is not None:
            if hasattr(self._artop_timeRangeType, "uuid"):
                return self._artop_timeRangeType.uuid
        return
