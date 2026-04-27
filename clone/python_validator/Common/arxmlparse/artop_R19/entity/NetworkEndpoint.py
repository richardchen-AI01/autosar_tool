# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NetworkEndpoint.py
from .Identifiable import Identifiable

class NetworkEndpoint(Identifiable):

    def __init__(self):
        super().__init__()
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        from .InfrastructureServices import InfrastructureServices
        from .IPSecConfig import IPSecConfig
        from .NetworkEndpointAddress import NetworkEndpointAddress
        self._artop_fullyQualifiedDomainName = None
        self._artop_priority = None
        self._artop_ethernetPhysicalChannel = None
        self._artop_infrastructureServices = None
        self._artop_ipSecConfig = None
        self._artop_networkEndpointAddress = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ethernetPhysicalChannel': '"ETHERNET-PHYSICAL-CHANNEL"', 
         '_artop_infrastructureServices': '"INFRASTRUCTURE-SERVICES"', 
         '_artop_ipSecConfig': '"IP-SEC-CONFIG"', 
         '_artop_networkEndpointAddress': '"NETWORK-ENDPOINT-ADDRESS"'})

    @property
    def fullyQualifiedDomainName_(self):
        return self._artop_fullyQualifiedDomainName

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def ref_ethernetPhysicalChannel_(self):
        return self._artop_ethernetPhysicalChannel

    @property
    def ethernetPhysicalChannel_(self):
        if self._artop_ethernetPhysicalChannel is not None:
            if hasattr(self._artop_ethernetPhysicalChannel, "uuid"):
                return self._artop_ethernetPhysicalChannel.uuid
        return

    @property
    def ref_infrastructureServices_(self):
        return self._artop_infrastructureServices

    @property
    def infrastructureServices_(self):
        if self._artop_infrastructureServices is not None:
            if hasattr(self._artop_infrastructureServices, "uuid"):
                return self._artop_infrastructureServices.uuid
        return

    @property
    def ref_ipSecConfig_(self):
        return self._artop_ipSecConfig

    @property
    def ipSecConfig_(self):
        if self._artop_ipSecConfig is not None:
            if hasattr(self._artop_ipSecConfig, "uuid"):
                return self._artop_ipSecConfig.uuid
        return

    @property
    def networkEndpointAddress_NetworkEndpointAddress(self):
        return self._artop_networkEndpointAddress
