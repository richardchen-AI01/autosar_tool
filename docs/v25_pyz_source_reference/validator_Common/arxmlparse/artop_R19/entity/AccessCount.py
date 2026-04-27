# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AccessCount.py
from .ARObject import ARObject

class AccessCount(ARObject):

    def __init__(self):
        super().__init__()
        from .AccessCountSet import AccessCountSet
        from .AbstractAccessPoint import AbstractAccessPoint
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .VariationPoint import VariationPoint
        self._artop_accessCountSet = None
        self._artop_accessPointRef = None
        self._artop_value = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_accessCountSet': '"ACCESS-COUNT-SET"', 
         '_artop_accessPointRef': '"ABSTRACT-ACCESS-POINT"', 
         '_artop_value': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_accessCountSet_(self):
        return self._artop_accessCountSet

    @property
    def accessCountSet_(self):
        if self._artop_accessCountSet is not None:
            if hasattr(self._artop_accessCountSet, "uuid"):
                return self._artop_accessCountSet.uuid
        return

    @property
    def ref_accessPoint_(self):
        return self._artop_accessPointRef

    @property
    def accessPoint_(self):
        if self._artop_accessPointRef is not None:
            if hasattr(self._artop_accessPointRef, "uuid"):
                return self._artop_accessPointRef.uuid
        return

    @property
    def ref_value_(self):
        return self._artop_value

    @property
    def value_(self):
        if self._artop_value is not None:
            if hasattr(self._artop_value, "uuid"):
                return self._artop_value.uuid
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
