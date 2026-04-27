# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwGenericAxisParam.py
from .ARObject import ARObject

class SwGenericAxisParam(ARObject):

    def __init__(self):
        super().__init__()
        from .SwAxisGeneric import SwAxisGeneric
        from .SwGenericAxisParamType import SwGenericAxisParamType
        from .NumericalValueVariationPoint import NumericalValueVariationPoint
        self._artop_swAxisGeneric = None
        self._artop_swGenericAxisParamTypeRef = None
        self._artop_vf = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_swAxisGeneric':"SW-AXIS-GENERIC", 
         '_artop_swGenericAxisParamTypeRef':"SW-GENERIC-AXIS-PARAM-TYPE", 
         '_artop_vf':"NUMERICAL-VALUE-VARIATION-POINT"})

    @property
    def ref_swAxisGeneric_(self):
        return self._artop_swAxisGeneric

    @property
    def swAxisGeneric_(self):
        if self._artop_swAxisGeneric is not None:
            if hasattr(self._artop_swAxisGeneric, "uuid"):
                return self._artop_swAxisGeneric.uuid
        return

    @property
    def ref_swGenericAxisParamType_(self):
        return self._artop_swGenericAxisParamTypeRef

    @property
    def swGenericAxisParamType_(self):
        if self._artop_swGenericAxisParamTypeRef is not None:
            if hasattr(self._artop_swGenericAxisParamTypeRef, "uuid"):
                return self._artop_swGenericAxisParamTypeRef.uuid
        return

    @property
    def vfs_NumericalValueVariationPoint(self):
        return self._artop_vf
