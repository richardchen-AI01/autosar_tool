# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeRangeType.py
from .ARObject import ARObject

class TimeRangeType(ARObject):

    def __init__(self):
        super().__init__()
        from .TimeRangeTypeTolerance import TimeRangeTypeTolerance
        self._artop_value = None
        self._artop_tolerance = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tolerance": "TIME-RANGE-TYPE-TOLERANCE"})

    @property
    def value_(self):
        return self._artop_value

    @property
    def ref_tolerance_(self):
        return self._artop_tolerance

    @property
    def tolerance_(self):
        if self._artop_tolerance is not None:
            if hasattr(self._artop_tolerance, "uuid"):
                return self._artop_tolerance.uuid
        return
