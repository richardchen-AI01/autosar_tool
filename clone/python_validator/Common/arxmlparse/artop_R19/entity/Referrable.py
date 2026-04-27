# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Referrable.py
from .ARObject import ARObject

class Referrable(ARObject):

    def __init__(self):
        super().__init__()
        from .ShortNameFragment import ShortNameFragment
        self._artop_shortName = None
        self._artop_shortNameFragment = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_shortNameFragment": "SHORT-NAME-FRAGMENT"})

    @property
    def shortName_(self):
        return self._artop_shortName

    @property
    def shortNameFragments_ShortNameFragment(self):
        return self._artop_shortNameFragment
