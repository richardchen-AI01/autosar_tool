# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConsumedServiceInstance.py
from .AbstractServiceInstance import AbstractServiceInstance

class ConsumedServiceInstance(AbstractServiceInstance):

    def __init__(self):
        super().__init__()
        from .ApplicationEndpoint import ApplicationEndpoint
        from .SomeipServiceVersion import SomeipServiceVersion
        from .ConsumedEventGroup import ConsumedEventGroup
        from .ApplicationEndpointRefConditional import ApplicationEndpointRefConditional
        from .ProvidedServiceInstance import ProvidedServiceInstance
        from .SdClientConfig import SdClientConfig
        from .SomeipSdClientServiceInstanceConfigRefConditional import SomeipSdClientServiceInstanceConfigRefConditional
        self._artop_autoRequire = None
        self._artop_instanceIdentifier = None
        self._artop_minorVersion = None
        self._artop_serviceIdentifier = None
        self._artop_versionDrivenFindBehavior = None
        self._artop_applicationEndpoint = None
        self._artop_blacklistedVersion = []
        self._artop_consumedEventGroup = []
        self._artop_localUnicastAddress = []
        self._artop_providedServiceInstanceRef = None
        self._artop_remoteUnicastAddress = []
        self._artop_sdClientConfig = None
        self._artop_sdClientTimerConfig = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_applicationEndpoint': '"APPLICATION-ENDPOINT"', 
         '_artop_blacklistedVersion': '"SOMEIP-SERVICE-VERSION"', 
         '_artop_consumedEventGroup': '"CONSUMED-EVENT-GROUP"', 
         '_artop_localUnicastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_providedServiceInstanceRef': '"PROVIDED-SERVICE-INSTANCE"', 
         '_artop_remoteUnicastAddress': '"APPLICATION-ENDPOINT-REF-CONDITIONAL"', 
         '_artop_sdClientConfig': '"SD-CLIENT-CONFIG"', 
         '_artop_sdClientTimerConfig': '"SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG-REF-CONDITIONAL"'})

    @property
    def autoRequire_(self):
        if self._artop_autoRequire:
            if self._artop_autoRequire == "true":
                return True
            return False
        else:
            return self._artop_autoRequire

    @property
    def instanceIdentifier_(self):
        return self._artop_instanceIdentifier

    @property
    def minorVersion_(self):
        return self._artop_minorVersion

    @property
    def serviceIdentifier_(self):
        return self._artop_serviceIdentifier

    @property
    def versionDrivenFindBehavior_(self):
        return self._artop_versionDrivenFindBehavior

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
    def blacklistedVersions_SomeipServiceVersion(self):
        return self._artop_blacklistedVersion

    @property
    def consumedEventGroups_ConsumedEventGroup(self):
        return self._artop_consumedEventGroup

    @property
    def localUnicastAddress_ApplicationEndpointRefConditional(self):
        return self._artop_localUnicastAddress

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
    def remoteUnicastAddress_ApplicationEndpointRefConditional(self):
        return self._artop_remoteUnicastAddress

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
    def sdClientTimerConfigs_SomeipSdClientServiceInstanceConfigRefConditional(self):
        return self._artop_sdClientTimerConfig
