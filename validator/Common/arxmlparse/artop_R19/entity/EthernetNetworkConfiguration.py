# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetNetworkConfiguration.py
from .NetworkConfiguration import NetworkConfiguration

class EthernetNetworkConfiguration(NetworkConfiguration):

    def __init__(self):
        super().__init__()
        from .DoIpNetworkConfiguration import DoIpNetworkConfiguration
        from .EthernetCommunicationConnector import EthernetCommunicationConnector
        self._artop_ipv4MulticastIpAddress = None
        self._artop_ipv6MulticastIpAddress = None
        self._artop_tcpPort = None
        self._artop_udpPort = None
        self._artop_doIpNetworkConfiguration = None
        self._artop_communicationConnectorRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_doIpNetworkConfiguration':"DO-IP-NETWORK-CONFIGURATION", 
         '_artop_communicationConnectorRef':"ETHERNET-COMMUNICATION-CONNECTOR"})

    @property
    def ipv4MulticastIpAddress_(self):
        return self._artop_ipv4MulticastIpAddress

    @property
    def ipv6MulticastIpAddress_(self):
        return self._artop_ipv6MulticastIpAddress

    @property
    def tcpPort_(self):
        return self._artop_tcpPort

    @property
    def udpPort_(self):
        return self._artop_udpPort

    @property
    def ref_doIpNetworkConfiguration_(self):
        return self._artop_doIpNetworkConfiguration

    @property
    def doIpNetworkConfiguration_(self):
        if self._artop_doIpNetworkConfiguration is not None:
            if hasattr(self._artop_doIpNetworkConfiguration, "uuid"):
                return self._artop_doIpNetworkConfiguration.uuid
        return

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
        return
