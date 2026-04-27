# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwAxisGeneric.py
from .ARObject import ARObject

class SwAxisGeneric(ARObject):

    def __init__(self):
        super().__init__()
        from .SwAxisIndividual import SwAxisIndividual
        from .SwAxisType import SwAxisType
        from .IntegerValueVariationPoint import IntegerValueVariationPoint
        from .SwGenericAxisParam import SwGenericAxisParam
        self._artop_swAxisIndividual = None
        self._artop_swAxisTypeRef = None
        self._artop_swNumberOfAxisPoints = None
        self._artop_swGenericAxisParam = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swAxisIndividual': '"SW-AXIS-INDIVIDUAL"', 
         '_artop_swAxisTypeRef': '"SW-AXIS-TYPE"', 
         '_artop_swNumberOfAxisPoints': '"INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_swGenericAxisParam': '"SW-GENERIC-AXIS-PARAM"'})

    @property
    def ref_swAxisIndividual_(self):
        return self._artop_swAxisIndividual

    @property
    def swAxisIndividual_(self):
        if self._artop_swAxisIndividual is not None:
            if hasattr(self._artop_swAxisIndividual, "uuid"):
                return self._artop_swAxisIndividual.uuid
        return

    @property
    def ref_swAxisType_(self):
        return self._artop_swAxisTypeRef

    @property
    def swAxisType_(self):
        if self._artop_swAxisTypeRef is not None:
            if hasattr(self._artop_swAxisTypeRef, "uuid"):
                return self._artop_swAxisTypeRef.uuid
        return

    @property
    def ref_swNumberOfAxisPoints_(self):
        return self._artop_swNumberOfAxisPoints

    @property
    def swNumberOfAxisPoints_(self):
        if self._artop_swNumberOfAxisPoints is not None:
            if hasattr(self._artop_swNumberOfAxisPoints, "uuid"):
                return self._artop_swNumberOfAxisPoints.uuid
        return

    @property
    def swGenericAxisParams_SwGenericAxisParam(self):
        return self._artop_swGenericAxisParam
