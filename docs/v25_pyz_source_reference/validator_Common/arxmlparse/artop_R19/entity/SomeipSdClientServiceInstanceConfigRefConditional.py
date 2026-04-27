# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdClientServiceInstanceConfigRefConditional.py
from .ARObject import ARObject

class SomeipSdClientServiceInstanceConfigRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ConsumedServiceInstance import ConsumedServiceInstance
        from .SomeipSdClientServiceInstanceConfig import SomeipSdClientServiceInstanceConfig
        from .VariationPoint import VariationPoint
        self._artop_consumedServiceInstance = None
        self._artop_someipSdClientServiceInstanceConfigRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_consumedServiceInstance':"CONSUMED-SERVICE-INSTANCE", 
         '_artop_someipSdClientServiceInstanceConfigRef':"SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_consumedServiceInstance_(self):
        return self._artop_consumedServiceInstance

    @property
    def consumedServiceInstance_(self):
        if self._artop_consumedServiceInstance is not None:
            if hasattr(self._artop_consumedServiceInstance, "uuid"):
                return self._artop_consumedServiceInstance.uuid
        return

    @property
    def ref_someipSdClientServiceInstanceConfig_(self):
        return self._artop_someipSdClientServiceInstanceConfigRef

    @property
    def someipSdClientServiceInstanceConfig_(self):
        if self._artop_someipSdClientServiceInstanceConfigRef is not None:
            if hasattr(self._artop_someipSdClientServiceInstanceConfigRef, "uuid"):
                return self._artop_someipSdClientServiceInstanceConfigRef.uuid
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
