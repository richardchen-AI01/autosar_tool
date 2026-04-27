# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetRawDataStreamMapping.py
from .RawDataStreamMapping import RawDataStreamMapping

class EthernetRawDataStreamMapping(RawDataStreamMapping):

    def __init__(self):
        super().__init__()
        from .EthernetCommunicationConnector import EthernetCommunicationConnector
        from .TlsSecureComProps import TlsSecureComProps
        self._artop_multicastUdpPort = None
        self._artop_socketOption = None
        self._artop_tcpPort = None
        self._artop_udpPort = None
        self._artop_communicationConnectorRef = None
        self._artop_tlsSecureComProps = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_communicationConnectorRef':"ETHERNET-COMMUNICATION-CONNECTOR", 
         '_artop_tlsSecureComProps':"TLS-SECURE-COM-PROPS"})

    @property
    def multicastUdpPort_(self):
        return self._artop_multicastUdpPort

    @property
    def socketOption_(self):
        return self._artop_socketOption

    @property
    def tcpPort_(self):
        return self._artop_tcpPort

    @property
    def udpPort_(self):
        return self._artop_udpPort

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
        return

    @property
    def ref_tlsSecureComProps_(self):
        return self._artop_tlsSecureComProps

    @property
    def tlsSecureComProps_(self):
        if self._artop_tlsSecureComProps is not None:
            if hasattr(self._artop_tlsSecureComProps, "uuid"):
                return self._artop_tlsSecureComProps.uuid
        return
