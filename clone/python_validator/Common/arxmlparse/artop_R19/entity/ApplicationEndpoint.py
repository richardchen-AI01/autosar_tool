# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ApplicationEndpoint.py
from .Identifiable import Identifiable

class ApplicationEndpoint(Identifiable):

    def __init__(self):
        super().__init__()
        from .SocketAddress import SocketAddress
        from .ConsumedServiceInstance import ConsumedServiceInstance
        from .DiscoveryTechnology import DiscoveryTechnology
        from .NetworkEndpoint import NetworkEndpoint
        from .ProvidedServiceInstance import ProvidedServiceInstance
        from .RemotingTechnology import RemotingTechnology
        from .SerializationTechnology import SerializationTechnology
        from .TlsCryptoServiceMapping import TlsCryptoServiceMapping
        from .TransportProtocolConfiguration import TransportProtocolConfiguration
        self._artop_maxNumberOfConnections = None
        self._artop_priority = None
        self._artop_socketAddress = None
        self._artop_consumedServiceInstance = []
        self._artop_discoveryTechnology = None
        self._artop_networkEndpointRef = None
        self._artop_providedServiceInstance = []
        self._artop_remotingTechnology = None
        self._artop_serializationTechnologyRef = None
        self._artop_tlsCryptoMappingRef = None
        self._artop_tpConfiguration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_socketAddress': '"SOCKET-ADDRESS"', 
         '_artop_consumedServiceInstance': '"CONSUMED-SERVICE-INSTANCE"', 
         '_artop_discoveryTechnology': '"DISCOVERY-TECHNOLOGY"', 
         '_artop_networkEndpointRef': '"NETWORK-ENDPOINT"', 
         '_artop_providedServiceInstance': '"PROVIDED-SERVICE-INSTANCE"', 
         '_artop_remotingTechnology': '"REMOTING-TECHNOLOGY"', 
         '_artop_serializationTechnologyRef': '"SERIALIZATION-TECHNOLOGY"', 
         '_artop_tlsCryptoMappingRef': '"TLS-CRYPTO-SERVICE-MAPPING"', 
         '_artop_tpConfiguration': '"TRANSPORT-PROTOCOL-CONFIGURATION"'})

    @property
    def maxNumberOfConnections_(self):
        return self._artop_maxNumberOfConnections

    @property
    def priority_(self):
        return self._artop_priority

    @property
    def ref_socketAddress_(self):
        return self._artop_socketAddress

    @property
    def socketAddress_(self):
        if self._artop_socketAddress is not None:
            if hasattr(self._artop_socketAddress, "uuid"):
                return self._artop_socketAddress.uuid
        return

    @property
    def consumedServiceInstances_ConsumedServiceInstance(self):
        return self._artop_consumedServiceInstance

    @property
    def ref_discoveryTechnology_(self):
        return self._artop_discoveryTechnology

    @property
    def discoveryTechnology_(self):
        if self._artop_discoveryTechnology is not None:
            if hasattr(self._artop_discoveryTechnology, "uuid"):
                return self._artop_discoveryTechnology.uuid
        return

    @property
    def ref_networkEndpoint_(self):
        return self._artop_networkEndpointRef

    @property
    def networkEndpoint_(self):
        if self._artop_networkEndpointRef is not None:
            if hasattr(self._artop_networkEndpointRef, "uuid"):
                return self._artop_networkEndpointRef.uuid
        return

    @property
    def providedServiceInstances_ProvidedServiceInstance(self):
        return self._artop_providedServiceInstance

    @property
    def ref_remotingTechnology_(self):
        return self._artop_remotingTechnology

    @property
    def remotingTechnology_(self):
        if self._artop_remotingTechnology is not None:
            if hasattr(self._artop_remotingTechnology, "uuid"):
                return self._artop_remotingTechnology.uuid
        return

    @property
    def ref_serializationTechnology_(self):
        return self._artop_serializationTechnologyRef

    @property
    def serializationTechnology_(self):
        if self._artop_serializationTechnologyRef is not None:
            if hasattr(self._artop_serializationTechnologyRef, "uuid"):
                return self._artop_serializationTechnologyRef.uuid
        return

    @property
    def ref_tlsCryptoMapping_(self):
        return self._artop_tlsCryptoMappingRef

    @property
    def tlsCryptoMapping_(self):
        if self._artop_tlsCryptoMappingRef is not None:
            if hasattr(self._artop_tlsCryptoMappingRef, "uuid"):
                return self._artop_tlsCryptoMappingRef.uuid
        return

    @property
    def ref_tpConfiguration_(self):
        return self._artop_tpConfiguration

    @property
    def tpConfiguration_(self):
        if self._artop_tpConfiguration is not None:
            if hasattr(self._artop_tpConfiguration, "uuid"):
                return self._artop_tpConfiguration.uuid
        return
