# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipProvidedEventGroup.py
from .Identifiable import Identifiable

class SomeipProvidedEventGroup(Identifiable):

    def __init__(self):
        super().__init__()
        from .ProvidedSomeipServiceInstance import ProvidedSomeipServiceInstance
        from .SomeipEventGroup import SomeipEventGroup
        from .SomeipSdServerEventGroupTimingConfig import SomeipSdServerEventGroupTimingConfig
        self._artop_eventMulticastUdpPort = None
        self._artop_ipv4MulticastIpAddress = None
        self._artop_ipv6MulticastIpAddress = None
        self._artop_multicastThreshold = None
        self._artop_providedSomeipServiceInstance = None
        self._artop_eventGroupRef = None
        self._artop_sdServerEventGroupTimingConfigRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_providedSomeipServiceInstance':"PROVIDED-SOMEIP-SERVICE-INSTANCE", 
         '_artop_eventGroupRef':"SOMEIP-EVENT-GROUP", 
         '_artop_sdServerEventGroupTimingConfigRef':"SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG"})

    @property
    def eventMulticastUdpPort_(self):
        return self._artop_eventMulticastUdpPort

    @property
    def ipv4MulticastIpAddress_(self):
        return self._artop_ipv4MulticastIpAddress

    @property
    def ipv6MulticastIpAddress_(self):
        return self._artop_ipv6MulticastIpAddress

    @property
    def multicastThreshold_(self):
        return self._artop_multicastThreshold

    @property
    def ref_providedSomeipServiceInstance_(self):
        return self._artop_providedSomeipServiceInstance

    @property
    def providedSomeipServiceInstance_(self):
        if self._artop_providedSomeipServiceInstance is not None:
            if hasattr(self._artop_providedSomeipServiceInstance, "uuid"):
                return self._artop_providedSomeipServiceInstance.uuid
        return

    @property
    def ref_eventGroup_(self):
        return self._artop_eventGroupRef

    @property
    def eventGroup_(self):
        if self._artop_eventGroupRef is not None:
            if hasattr(self._artop_eventGroupRef, "uuid"):
                return self._artop_eventGroupRef.uuid
        return

    @property
    def ref_sdServerEventGroupTimingConfig_(self):
        return self._artop_sdServerEventGroupTimingConfigRef

    @property
    def sdServerEventGroupTimingConfig_(self):
        if self._artop_sdServerEventGroupTimingConfigRef is not None:
            if hasattr(self._artop_sdServerEventGroupTimingConfigRef, "uuid"):
                return self._artop_sdServerEventGroupTimingConfigRef.uuid
        return
