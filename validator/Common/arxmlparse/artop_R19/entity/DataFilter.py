# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DataFilter.py
from .ARObject import ARObject

class DataFilter(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_dataFilterType = None
        self._artop_mask = None
        self._artop_max = None
        self._artop_min = None
        self._artop_offset = None
        self._artop_period = None
        self._artop_x = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def dataFilterType_(self):
        return self._artop_dataFilterType

    @property
    def mask_(self):
        return self._artop_mask

    @property
    def max_(self):
        return self._artop_max

    @property
    def min_(self):
        return self._artop_min

    @property
    def offset_(self):
        return self._artop_offset

    @property
    def period_(self):
        return self._artop_period

    @property
    def x_(self):
        return self._artop_x
