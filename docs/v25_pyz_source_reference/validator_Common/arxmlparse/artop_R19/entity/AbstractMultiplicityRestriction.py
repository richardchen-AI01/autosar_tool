# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractMultiplicityRestriction.py
from .ARObject import ARObject

class AbstractMultiplicityRestriction(ARObject):

    def __init__(self):
        super().__init__()
        self._artop_lowerMultiplicity = None
        self._artop_upperMultiplicity = None
        self._artop_upperMultiplicityInfinite = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def lowerMultiplicity_(self):
        return self._artop_lowerMultiplicity

    @property
    def upperMultiplicity_(self):
        return self._artop_upperMultiplicity

    @property
    def upperMultiplicityInfinite_(self):
        if self._artop_upperMultiplicityInfinite:
            if self._artop_upperMultiplicityInfinite == "true":
                return True
            return False
        else:
            return self._artop_upperMultiplicityInfinite
