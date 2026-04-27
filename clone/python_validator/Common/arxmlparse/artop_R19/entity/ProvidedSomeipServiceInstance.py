# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProvidedSomeipServiceInstance.py
from .ProvidedApServiceInstance import ProvidedApServiceInstance

class ProvidedSomeipServiceInstance(ProvidedApServiceInstance):

    def __init__(self):
        super().__init__()
        from .TagWithOptionalValue import TagWithOptionalValue
        from .SomeipEventProps import SomeipEventProps
        from .SomeipMethodProps import SomeipMethodProps
        from .SomeipProvidedEventGroup import SomeipProvidedEventGroup
        from .SomeipSdServerServiceInstanceConfig import SomeipSdServerServiceInstanceConfig
        self._artop_loadBalancingPriority = None
        self._artop_loadBalancingWeight = None
        self._artop_serviceInstanceId = None
        self._artop_capabilityRecord = []
        self._artop_eventProps = []
        self._artop_methodResponseProps = []
        self._artop_providedEventGroup = []
        self._artop_sdServerConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_capabilityRecord': '"TAG-WITH-OPTIONAL-VALUE"', 
         '_artop_eventProps': '"SOMEIP-EVENT-PROPS"', 
         '_artop_methodResponseProps': '"SOMEIP-METHOD-PROPS"', 
         '_artop_providedEventGroup': '"SOMEIP-PROVIDED-EVENT-GROUP"', 
         '_artop_sdServerConfigRef': '"SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG"'})

    @property
    def loadBalancingPriority_(self):
        return self._artop_loadBalancingPriority

    @property
    def loadBalancingWeight_(self):
        return self._artop_loadBalancingWeight

    @property
    def serviceInstanceId_(self):
        return self._artop_serviceInstanceId

    @property
    def capabilityRecords_TagWithOptionalValue(self):
        return self._artop_capabilityRecord

    @property
    def eventProps_SomeipEventProps(self):
        return self._artop_eventProps

    @property
    def methodResponseProps_SomeipMethodProps(self):
        return self._artop_methodResponseProps

    @property
    def providedEventGroups_SomeipProvidedEventGroup(self):
        return self._artop_providedEventGroup

    @property
    def ref_sdServerConfig_(self):
        return self._artop_sdServerConfigRef

    @property
    def sdServerConfig_(self):
        if self._artop_sdServerConfigRef is not None:
            if hasattr(self._artop_sdServerConfigRef, "uuid"):
                return self._artop_sdServerConfigRef.uuid
        return
