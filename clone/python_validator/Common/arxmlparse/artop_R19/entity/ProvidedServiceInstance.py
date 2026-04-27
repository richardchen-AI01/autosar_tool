# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProvidedServiceInstance.py
from .AbstractServiceInstance import AbstractServiceInstance

class ProvidedServiceInstance(AbstractServiceInstance):

    def __init__(self):
        super().__init__()
        from .ApplicationEndpoint import ApplicationEndpoint
        from .EventHandler import EventHandler
        from .ApplicationEndpointRefConditional import ApplicationEndpointRefConditional
        from .SdServerConfig import SdServerConfig
        from .SomeipSdServerServiceInstanceConfigRefConditional import SomeipSdServerServiceInstanceConfigRefConditional
        self._artop_autoAvailable = None
        self._artop_instanceIdentifier = None
        self._artop_loadBalancingPriority = None
        self._artop_loadBalancingWeight = None
        self._artop_minorVersion = None
        self._artop_priority = None
        self._artop_serviceIdentifier = None
        self._artop_applicationEndpoint = None
        self._artop_eventHandler = []
        self._artop_localUnicastAddress = []
        self._artop_remoteUnicastAddress = []
        self._artop_sdServerConfig = None
        self._artop_sdServerTimerConfig = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_applicationEndpoint': '"APPLICATION-ENDPOINT"', 
         '_artop_eventHandler': '"EVENT-HANDLER"', 
         '_artop_localUnicastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_remoteUnicastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_sdServerConfig': '"SD-SERVER-CONFIG"', 
         '_artop_sdServerTimerConfig': '"SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL"'})

    @property
    def autoAvailable_(self):
        if self._artop_autoAvailable:
            if self._artop_autoAvailable == "true":
                return True
            return False
        else:
            return self._artop_autoAvailable

    @property
    def instanceIdentifier_(self):
        return self._artop_instanceIdentifier

    @property
    def loadBalancingPriority_(self):
        return self._artop_loadBalancingPriority

    @property
    def loadBalancingWeight_(self):
        return self._artop_loadBalancingWeight

    @property
    def minorVersion_(self):
        return self._artop_minorVersion

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def serviceIdentifier_(self):
        return self._artop_serviceIdentifier

    @property
    def ref_applicationEndpoint_(self):
        return self._artop_applicationEndpoint

    @property
    def applicationEndpoint_(self):
        if self._artop_applicationEndpoint is not None:
            if hasattr(self._artop_applicationEndpoint, "uuid"):
                return self._artop_applicationEndpoint.uuid
        return

    @property
    def eventHandlers_EventHandler(self):
        return self._artop_eventHandler

    @property
    def localUnicastAddress_ApplicationEndpointRefConditional(self):
        return self._artop_localUnicastAddress

    @property
    def remoteUnicastAddress_ApplicationEndpointRefConditional(self):
        return self._artop_remoteUnicastAddress

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
    def sdServerTimerConfigs_SomeipSdServerServiceInstanceConfigRefConditional(self):
        return self._artop_sdServerTimerConfig
