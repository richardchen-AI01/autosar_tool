# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwValues.py
from .ARObject import ARObject

class SwValues(ARObject):

    def __init__(self):
        super().__init__()
        from .NumericalOrText import NumericalOrText
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        from .ValueGroup import ValueGroup
        self._artop_vt = None
        self._artop_v = None
        self._artop_mixed = None
        self._artop_vtf = []
        self._artop_vf = []
        self._artop_vg = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_vtf':"NUMERICAL-OR-TEXT", 
         '_artop_vf':"NUMERICAL-VALUE-VARIATION-POINT", 
         '_artop_vg':"VALUE-GROUP"})

    @property
    def vt_(self):
        return self._artop_vt

    @property
    def v_(self):
        return self._artop_v

    @property
    def mixed_(self):
        return self._artop_mixed

    @property
    def vtfs_NumericalOrText(self):
        return self._artop_vtf

    @property
    def vfs_NumericalValueVariationPoint(self):
        return self._artop_vf

    @property
    def vgs_ValueGroup(self):
        return self._artop_vg
