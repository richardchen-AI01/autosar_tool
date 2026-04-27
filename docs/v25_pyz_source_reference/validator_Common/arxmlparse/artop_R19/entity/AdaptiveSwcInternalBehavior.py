# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AdaptiveSwcInternalBehavior.py
from .Identifiable import Identifiable

class AdaptiveSwcInternalBehavior(Identifiable):

    def __init__(self):
        super().__init__()
        from .AdaptiveApplicationSwComponentType import AdaptiveApplicationSwComponentType
        from .SwcServiceDependency import SwcServiceDependency
        from .VariationPoint import VariationPoint
        self._artop_adaptiveApplicationSwComponentType = None
        self._artop_serviceDependency = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_adaptiveApplicationSwComponentType':"ADAPTIVE-APPLICATION-SW-COMPONENT-TYPE", 
         '_artop_serviceDependency':"SWC-SERVICE-DEPENDENCY", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_adaptiveApplicationSwComponentType_(self):
        return self._artop_adaptiveApplicationSwComponentType

    @property
    def adaptiveApplicationSwComponentType_(self):
        if self._artop_adaptiveApplicationSwComponentType is not None:
            if hasattr(self._artop_adaptiveApplicationSwComponentType, "uuid"):
                return self._artop_adaptiveApplicationSwComponentType.uuid
        return

    @property
    def serviceDependencies_SwcServiceDependency(self):
        return self._artop_serviceDependency

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
