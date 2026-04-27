# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdServerServiceInstanceConfigRefConditional.py
from .ARObject import ARObject

class SomeipSdServerServiceInstanceConfigRefConditional(ARObject):

    def __init__(self):
        super().__init__()
        from .ProvidedServiceInstance import ProvidedServiceInstance
        from .SomeipSdServerServiceInstanceConfig import SomeipSdServerServiceInstanceConfig
        from .VariationPoint import VariationPoint
        self._artop_providedServiceInstance = None
        self._artop_someipSdServerServiceInstanceConfigRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providedServiceInstance':"PROVIDED-SERVICE-INSTANCE", 
         '_artop_someipSdServerServiceInstanceConfigRef':"SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_providedServiceInstance_(self):
        return self._artop_providedServiceInstance

    @property
    def providedServiceInstance_(self):
        if self._artop_providedServiceInstance is not None:
            if hasattr(self._artop_providedServiceInstance, "uuid"):
                return self._artop_providedServiceInstance.uuid
        return

    @property
    def ref_someipSdServerServiceInstanceConfig_(self):
        return self._artop_someipSdServerServiceInstanceConfigRef

    @property
    def someipSdServerServiceInstanceConfig_(self):
        if self._artop_someipSdServerServiceInstanceConfigRef is not None:
            if hasattr(self._artop_someipSdServerServiceInstanceConfigRef, "uuid"):
                return self._artop_someipSdServerServiceInstanceConfigRef.uuid
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
