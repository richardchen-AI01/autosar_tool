# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwCalprmAxisTypeProps.py
from .ARObject import ARObject

class SwCalprmAxisTypeProps(ARObject):

    def __init__(self):
        super().__init__()
        from .SwCalprmAxis import SwCalprmAxis
        self._artop_maxGradient = None
        self._artop_monotony = None
        self._artop_swCalprmAxis = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_swCalprmAxis": "SW-CALPRM-AXIS"})

    @property
    def maxGradient_(self):
        if self._artop_maxGradient:
            return float(self._artop_maxGradient)
        return self._artop_maxGradient

    @property
    def monotony_(self):
        return self._artop_monotony

    @property
    def ref_swCalprmAxis_(self):
        return self._artop_swCalprmAxis

    @property
    def swCalprmAxis_(self):
        if self._artop_swCalprmAxis is not None:
            if hasattr(self._artop_swCalprmAxis, "uuid"):
                return self._artop_swCalprmAxis.uuid
        return
