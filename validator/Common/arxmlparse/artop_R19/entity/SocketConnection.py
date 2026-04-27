# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SocketConnection.py
from .Describable import Describable

class SocketConnection(Describable):

    def __init__(self):
        super().__init__()
        from .IPv6ExtHeaderFilterList import IPv6ExtHeaderFilterList
        from .TcpOptionFilterList import TcpOptionFilterList
        from .SocketAddress import SocketAddress
        from .LogicAddress import LogicAddress
        from .TpConnectionIdent import TpConnectionIdent
        from .NPdu import NPdu
        from .SocketConnectionIpduIdentifier import SocketConnectionIpduIdentifier
        from .VariationPoint import VariationPoint
        self._artop_autosarConnector = None
        self._artop_clientIpAddrFromConnectionRequest = None
        self._artop_clientPortFromConnectionRequest = None
        self._artop_pduCollectionMaxBufferSize = None
        self._artop_pduCollectionTimeout = None
        self._artop_runtimeIpAddressConfiguration = None
        self._artop_runtimePortConfiguration = None
        self._artop_shortLabel = None
        self._artop_socketProtocol = None
        self._artop_allowedIPv6ExtHeadersRef = None
        self._artop_allowedTcpOptionsRef = None
        self._artop_clientPortRef = None
        self._artop_doIpSourceAddressRef = None
        self._artop_doIpTargetAddressRef = None
        self._artop_ident = None
        self._artop_localPortRef = None
        self._artop_nPduRef = None
        self._artop_pdu = []
        self._artop_remotePortRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_allowedIPv6ExtHeadersRef': '"I-PV-6-EXT-HEADER-FILTER-LIST"', 
         '_artop_allowedTcpOptionsRef': '"TCP-OPTION-FILTER-LIST"', 
         '_artop_clientPortRef': '"SOCKET-ADDRESS"', 
         '_artop_doIpSourceAddressRef': '"LOGIC-ADDRESS"', 
         '_artop_doIpTargetAddressRef': '"LOGIC-ADDRESS"', 
         '_artop_ident': '"TP-CONNECTION-IDENT"', 
         '_artop_localPortRef': '"SOCKET-ADDRESS"', 
         '_artop_nPduRef': '"N-PDU"', 
         '_artop_pdu': '"SOCKET-CONNECTION-IPDU-IDENTIFIER"', 
         '_artop_remotePortRef': '"SOCKET-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def autosarConnector_(self):
        return self._artop_autosarConnector

    @property
    def clientIpAddrFromConnectionRequest_(self):
        if self._artop_clientIpAddrFromConnectionRequest:
            if self._artop_clientIpAddrFromConnectionRequest == "true":
                return True
            return False
        else:
            return self._artop_clientIpAddrFromConnectionRequest

    @property
    def clientPortFromConnectionRequest_(self):
        if self._artop_clientPortFromConnectionRequest:
            if self._artop_clientPortFromConnectionRequest == "true":
                return True
            return False
        else:
            return self._artop_clientPortFromConnectionRequest

    @property
    def pduCollectionMaxBufferSize_(self):
        return self._artop_pduCollectionMaxBufferSize

    @property
    def pduCollectionTimeout_(self):
        return self._artop_pduCollectionTimeout

    @property
    def runtimeIpAddressConfiguration_(self):
        return self._artop_runtimeIpAddressConfiguration

    @property
    def runtimePortConfiguration_(self):
        return self._artop_runtimePortConfiguration

    @property
    def shortLabel_(self):
        return self._artop_shortLabel

    @property
    def socketProtocol_(self):
        return self._artop_socketProtocol

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
    def ref_clientPort_(self):
        return self._artop_clientPortRef

    @property
    def clientPort_(self):
        if self._artop_clientPortRef is not None:
            if hasattr(self._artop_clientPortRef, "uuid"):
                return self._artop_clientPortRef.uuid
        return

    @property
    def ref_doIpSourceAddress_(self):
        return self._artop_doIpSourceAddressRef

    @property
    def doIpSourceAddress_(self):
        if self._artop_doIpSourceAddressRef is not None:
            if hasattr(self._artop_doIpSourceAddressRef, "uuid"):
                return self._artop_doIpSourceAddressRef.uuid
        return

    @property
    def ref_doIpTargetAddress_(self):
        return self._artop_doIpTargetAddressRef

    @property
    def doIpTargetAddress_(self):
        if self._artop_doIpTargetAddressRef is not None:
            if hasattr(self._artop_doIpTargetAddressRef, "uuid"):
                return self._artop_doIpTargetAddressRef.uuid
        return

    @property
    def ref_ident_(self):
        return self._artop_ident

    @property
    def ident_(self):
        if self._artop_ident is not None:
            if hasattr(self._artop_ident, "uuid"):
                return self._artop_ident.uuid
        return

    @property
    def ref_localPort_(self):
        return self._artop_localPortRef

    @property
    def localPort_(self):
        if self._artop_localPortRef is not None:
            if hasattr(self._artop_localPortRef, "uuid"):
                return self._artop_localPortRef.uuid
        return

    @property
    def ref_nPdu_(self):
        return self._artop_nPduRef

    @property
    def nPdu_(self):
        if self._artop_nPduRef is not None:
            if hasattr(self._artop_nPduRef, "uuid"):
                return self._artop_nPduRef.uuid
        return

    @property
    def pdus_SocketConnectionIpduIdentifier(self):
        return self._artop_pdu

    @property
    def ref_remotePort_(self):
        return self._artop_remotePortRef

    @property
    def remotePort_(self):
        if self._artop_remotePortRef is not None:
            if hasattr(self._artop_remotePortRef, "uuid"):
                return self._artop_remotePortRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
