# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ValueList.py
from .ARObject import ARObject

class ValueList(ARObject):

    def __init__(self):
        super().__init__()
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        self._artop_v = None
        self._artop_mixed = None
        self._artop_vf = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_vf": "NUMERICAL-VALUE-VARIATION-POINT"})

    @property
    def v_(self):
        return self._artop_v

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def vfs_NumericalValueVariationPoint(self):
        return self._artop_vf
