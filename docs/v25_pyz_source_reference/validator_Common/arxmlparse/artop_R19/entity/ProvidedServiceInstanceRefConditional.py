# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProvidedServiceInstanceRefConditional.py
from .ARObject import ARObject

class ProvidedServiceInstanceRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ConsumedProvidedServiceInstanceGroup import ConsumedProvidedServiceInstanceGroup
        from .ProvidedServiceInstance import ProvidedServiceInstance
        from .VariationPoint import VariationPoint
        self._artop_consumedProvidedServiceInstanceGroup = None
        self._artop_providedServiceInstanceRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_consumedProvidedServiceInstanceGroup':"CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP", 
         '_artop_providedServiceInstanceRef':"PROVIDED-SERVICE-INSTANCE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_consumedProvidedServiceInstanceGroup_(self):
        return self._artop_consumedProvidedServiceInstanceGroup

    @property
    def consumedProvidedServiceInstanceGroup_(self):
        if self._artop_consumedProvidedServiceInstanceGroup is not None:
            if hasattr(self._artop_consumedProvidedServiceInstanceGroup, "uuid"):
                return self._artop_consumedProvidedServiceInstanceGroup.uuid
        return

    @property
    def ref_providedServiceInstance_(self):
        return self._artop_providedServiceInstanceRef

    @property
    def providedServiceInstance_(self):
        if self._artop_providedServiceInstanceRef is not None:
            if hasattr(self._artop_providedServiceInstanceRef, "uuid"):
                return self._artop_providedServiceInstanceRef.uuid
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
