# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SocketAddress.py
from .Identifiable import Identifiable

class SocketAddress(Identifiable):

    def __init__(self):
        super().__init__()
        from .SoAdConfig import SoAdConfig
        from .IPv6ExtHeaderFilterList import IPv6ExtHeaderFilterList
        from .TcpOptionFilterList import TcpOptionFilterList
        from .ApplicationEndpoint import ApplicationEndpoint
        from .EthernetCommunicationConnector import EthernetCommunicationConnector
        from .StaticSocketConnection import StaticSocketConnection
        from .VariationPoint import VariationPoint
        self._artop_differentiatedServiceField = None
        self._artop_flowLabel = None
        self._artop_ipAddress = None
        self._artop_pathMtuDiscoveryEnabled = None
        self._artop_pduCollectionMaxBufferSize = None
        self._artop_pduCollectionTimeout = None
        self._artop_portAddress = None
        self._artop_udpChecksumHandling = None
        self._artop_soAdConfig = None
        self._artop_allowedIPv6ExtHeadersRef = None
        self._artop_allowedTcpOptionsRef = None
        self._artop_applicationEndpoint = None
        self._artop_connectorRef = None
        self._artop_multicastConnectorRef = []
        self._artop_staticSocketConnection = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_soAdConfig': '"SO-AD-CONFIG"', 
         '_artop_allowedIPv6ExtHeadersRef': '"I-PV-6-EXT-HEADER-FILTER-LIST"', 
         '_artop_allowedTcpOptionsRef': '"TCP-OPTION-FILTER-LIST"', 
         '_artop_applicationEndpoint': '"APPLICATION-ENDPOINT"', 
         '_artop_connectorRef': '"ETHERNET-COMMUNICATION-CONNECTOR"', 
         '_artop_multicastConnectorRef': '"ETHERNET-COMMUNICATION-CONNECTOR"', 
         '_artop_staticSocketConnection': '"STATIC-SOCKET-CONNECTION"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def differentiatedServiceField_(self):
        return self._artop_differentiatedServiceField

    @property
    def flowLabel_(self):
        return self._artop_flowLabel

    @property
    def ipAddress_(self):
        return self._artop_ipAddress

    @property
    def pathMtuDiscoveryEnabled_(self):
        if self._artop_pathMtuDiscoveryEnabled:
            if self._artop_pathMtuDiscoveryEnabled == "true":
                return True
            return False
        else:
            return self._artop_pathMtuDiscoveryEnabled

    @property
    def pduCollectionMaxBufferSize_(self):
        return self._artop_pduCollectionMaxBufferSize

    @property
    def pduCollectionTimeout_(self):
        return self._artop_pduCollectionTimeout

    @property
    def portAddress_(self):
        if self._artop_portAddress:
            return int(self._artop_portAddress)
        return self._artop_portAddress

    @property
    def udpChecksumHandling_(self):
        return self._artop_udpChecksumHandling

    @property
    def ref_soAdConfig_(self):
        return self._artop_soAdConfig

    @property
    def soAdConfig_(self):
        if self._artop_soAdConfig is not None:
            if hasattr(self._artop_soAdConfig, "uuid"):
                return self._artop_soAdConfig.uuid
        return

    @property
    def ref_allowedIPv6ExtHeaders_(self):
        return self._artop_allowedIPv6ExtHeadersRef

    @property
    def allowedIPv6ExtHeaders_(self):
        if self._artop_allowedIPv6ExtHeadersRef is not None:
            if hasattr(self._artop_allowedIPv6ExtHeadersRef, "uuid"):
                return self._artop_allowedIPv6ExtHeadersRef.uuid
        return

    @property
    def ref_allowedTcpOptions_(self):
        return self._artop_allowedTcpOptionsRef

    @property
    def allowedTcpOptions_(self):
        if self._artop_allowedTcpOptionsRef is not None:
            if hasattr(self._artop_allowedTcpOptionsRef, "uuid"):
                return self._artop_allowedTcpOptionsRef.uuid
        return

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
    def ref_connector_(self):
        return self._artop_connectorRef

    @property
    def connector_(self):
        if self._artop_connectorRef is not None:
            if hasattr(self._artop_connectorRef, "uuid"):
                return self._artop_connectorRef.uuid
        return

    @property
    def ref_multicastConnectors_(self):
        return self._artop_multicastConnectorRef

    @property
    def multicastConnectors_(self):
        return self._artop_multicastConnectorRef

    @property
    def staticSocketConnections_StaticSocketConnection(self):
        return self._artop_staticSocketConnection

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
