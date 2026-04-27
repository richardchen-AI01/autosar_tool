# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConsumedEventGroup.py
from .Identifiable import Identifiable

class ConsumedEventGroup(Identifiable):

    def __init__(self):
        super().__init__()
        from .ConsumedServiceInstance import ConsumedServiceInstance
        from .ApplicationEndpoint import ApplicationEndpoint
        from .ApplicationEndpointRefConditional import ApplicationEndpointRefConditional
        from .PduActivationRoutingGroup import PduActivationRoutingGroup
        from .SoAdRoutingGroup import SoAdRoutingGroup
        from .SdClientConfig import SdClientConfig
        from .SomeipSdClientEventGroupTimingConfigRefConditional import SomeipSdClientEventGroupTimingConfigRefConditional
        from .VariationPoint import VariationPoint
        self._artop_autoRequire = None
        self._artop_eventGroupIdentifier = None
        self._artop_instanceIdentifier = None
        self._artop_priority = None
        self._artop_consumedServiceInstance = None
        self._artop_applicationEndpointRef = None
        self._artop_eventMulticastAddress = []
        self._artop_pduActivationRoutingGroup = []
        self._artop_routingGroupRef = []
        self._artop_sdClientConfig = None
        self._artop_sdClientTimerConfig = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_consumedServiceInstance': '"CONSUMED-SERVICE-INSTANCE"', 
         '_artop_applicationEndpointRef': '"APPLICATION-ENDPOINT"', 
         '_artop_eventMulticastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_pduActivationRoutingGroup': '"PDU-ACTIVATION-ROUTING-GROUP"', 
         '_artop_routingGroupRef': '"SO-AD-ROUTING-GROUP"', 
         '_artop_sdClientConfig': '"SD-CLIENT-CONFIG"', 
         '_artop_sdClientTimerConfig': '"SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def autoRequire_(self):
        if self._artop_autoRequire:
            if self._artop_autoRequire == "true":
                return True
            return False
        else:
            return self._artop_autoRequire

    @property
    def eventGroupIdentifier_(self):
        return self._artop_eventGroupIdentifier

    @property
    def instanceIdentifier_(self):
        return self._artop_instanceIdentifier

    @property
    def priority_(self):
        return self._artop_priority

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
    def ref_applicationEndpoint_(self):
        return self._artop_applicationEndpointRef

    @property
    def applicationEndpoint_(self):
        if self._artop_applicationEndpointRef is not None:
            if hasattr(self._artop_applicationEndpointRef, "uuid"):
                return self._artop_applicationEndpointRef.uuid
        return

    @property
    def eventMulticastAddress_ApplicationEndpointRefConditional(self):
        return self._artop_eventMulticastAddress

    @property
    def pduActivationRoutingGroups_PduActivationRoutingGroup(self):
        return self._artop_pduActivationRoutingGroup

    @property
    def ref_routingGroups_(self):
        return self._artop_routingGroupRef

    @property
    def routingGroups_(self):
        return self._artop_routingGroupRef

    @property
    def ref_sdClientConfig_(self):
        return self._artop_sdClientConfig

    @property
    def sdClientConfig_(self):
        if self._artop_sdClientConfig is not None:
            if hasattr(self._artop_sdClientConfig, "uuid"):
                return self._artop_sdClientConfig.uuid
        return

    @property
    def sdClientTimerConfigs_SomeipSdClientEventGroupTimingConfigRefConditional(self):
        return self._artop_sdClientTimerConfig

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
