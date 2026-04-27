# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AccessCountSet.py
from .ARObject import ARObject

class AccessCountSet(ARObject):

    def __init__(self):
        super().__init__()
        from .ResourceConsumption import ResourceConsumption
        from .AccessCount import AccessCount
        from .VariationPoint import VariationPoint
        self._artop_countProfile = None
        self._artop_resourceConsumption = None
        self._artop_accessCount = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_resourceConsumption':"RESOURCE-CONSUMPTION", 
         '_artop_accessCount':"ACCESS-COUNT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def countProfile_(self):
        return self._artop_countProfile

    @property
    def ref_resourceConsumption_(self):
        return self._artop_resourceConsumption

    @property
    def resourceConsumption_(self):
        if self._artop_resourceConsumption is not None:
            if hasattr(self._artop_resourceConsumption, "uuid"):
                return self._artop_resourceConsumption.uuid
        return

    @property
    def accessCounts_AccessCount(self):
        return self._artop_accessCount

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
