# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwServiceArg.py
from .Identifiable import Identifiable

class SwServiceArg(Identifiable):

    def __init__(self):
        super().__init__()
        from .ValueList import ValueList
        from .SwDataDefProps import SwDataDefProps
        from .VariationPoint import VariationPoint
        self._artop_direction = None
        self._artop_swArraysize = None
        self._artop_swDataDefProps = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swArraysize':"VALUE-LIST", 
         '_artop_swDataDefProps':"SW-DATA-DEF-PROPS", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def direction_(self):
        return self._artop_direction

    @property
    def ref_swArraysize_(self):
        return self._artop_swArraysize

    @property
    def swArraysize_(self):
        if self._artop_swArraysize is not None:
            if hasattr(self._artop_swArraysize, "uuid"):
                return self._artop_swArraysize.uuid
        return

    @property
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
