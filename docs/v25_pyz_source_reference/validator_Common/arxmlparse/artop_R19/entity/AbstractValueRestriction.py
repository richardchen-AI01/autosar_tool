# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractValueRestriction.py
from .ARObject import ARObject

class AbstractValueRestriction(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_max = None
        self._artop_maxLength = None
        self._artop_min = None
        self._artop_minLength = None
        self._artop_pattern = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def max_(self):
        return self._artop_max

    @property
    def maxLength_(self):
        return self._artop_maxLength

    @property
    def min_(self):
        return self._artop_min

    @property
    def minLength_(self):
        return self._artop_minLength

    @property
    def pattern_(self):
        return self._artop_pattern
