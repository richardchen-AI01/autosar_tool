# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EventHandler.py
from .Referrable import Referrable

class EventHandler(Referrable):

    def __init__(self):
        super().__init__()
        from .ProvidedServiceInstance import ProvidedServiceInstance
        from .ApplicationEndpoint import ApplicationEndpoint
        from .ConsumedEventGroup import ConsumedEventGroup
        from .ApplicationEndpointRefConditional import ApplicationEndpointRefConditional
        from .PduActivationRoutingGroup import PduActivationRoutingGroup
        from .SoAdRoutingGroup import SoAdRoutingGroup
        from .SdServerConfig import SdServerConfig
        from .SomeipSdServerEventGroupTimingConfigRefConditional import SomeipSdServerEventGroupTimingConfigRefConditional
        from .VariationPoint import VariationPoint
        self._artop_eventGroupIdentifier = None
        self._artop_multicastThreshold = None
        self._artop_providedServiceInstance = None
        self._artop_applicationEndpointRef = None
        self._artop_consumedEventGroupRef = []
        self._artop_eventMulticastAddress = []
        self._artop_pduActivationRoutingGroup = []
        self._artop_routingGroupRef = []
        self._artop_sdServerConfig = None
        self._artop_sdServerEgTimingConfig = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_providedServiceInstance': '"PROVIDED-SERVICE-INSTANCE"', 
         '_artop_applicationEndpointRef': '"APPLICATION-ENDPOINT"', 
         '_artop_consumedEventGroupRef': '"CONSUMED-EVENT-GROUP"', 
         '_artop_eventMulticastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_pduActivationRoutingGroup': '"PDU-ACTIVATION-ROUTING-GROUP"', 
         '_artop_routingGroupRef': '"SO-AD-ROUTING-GROUP"', 
         '_artop_sdServerConfig': '"SD-SERVER-CONFIG"', 
         '_artop_sdServerEgTimingConfig': '"SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def eventGroupIdentifier_(self):
        return self._artop_eventGroupIdentifier

    @property
    def multicastThreshold_(self):
        return self._artop_multicastThreshold

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
    def ref_applicationEndpoint_(self):
        return self._artop_applicationEndpointRef

    @property
    def applicationEndpoint_(self):
        if self._artop_applicationEndpointRef is not None:
            if hasattr(self._artop_applicationEndpointRef, "uuid"):
                return self._artop_applicationEndpointRef.uuid
        return

    @property
    def ref_consumedEventGroups_(self):
        return self._artop_consumedEventGroupRef

    @property
    def consumedEventGroups_(self):
        return self._artop_consumedEventGroupRef

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
    def ref_sdServerConfig_(self):
        return self._artop_sdServerConfig

    @property
    def sdServerConfig_(self):
        if self._artop_sdServerConfig is not None:
            if hasattr(self._artop_sdServerConfig, "uuid"):
                return self._artop_sdServerConfig.uuid
        return

    @property
    def sdServerEgTimingConfigs_SomeipSdServerEventGroupTimingConfigRefConditional(self):
        return self._artop_sdServerEgTimingConfig

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
