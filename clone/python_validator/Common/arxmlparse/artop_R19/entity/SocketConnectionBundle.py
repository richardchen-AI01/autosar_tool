# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SocketConnectionBundle.py
from .Referrable import Referrable

class SocketConnectionBundle(Referrable):

    def __init__(self):
        super().__init__()
        from .SoAdConfig import SoAdConfig
        from .SocketConnection import SocketConnection
        from .SocketConnectionIpduIdentifier import SocketConnectionIpduIdentifier
        from .SocketAddress import SocketAddress
        from .VariationPoint import VariationPoint
        self._artop_differentiatedServiceField = None
        self._artop_flowLabel = None
        self._artop_pathMtuDiscoveryEnabled = None
        self._artop_udpChecksumHandling = None
        self._artop_soAdConfig = None
        self._artop_bundledConnection = []
        self._artop_pdu = []
        self._artop_serverPortRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_soAdConfig': '"SO-AD-CONFIG"', 
         '_artop_bundledConnection': '"SOCKET-CONNECTION"', 
         '_artop_pdu': '"SOCKET-CONNECTION-IPDU-IDENTIFIER"', 
         '_artop_serverPortRef': '"SOCKET-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def differentiatedServiceField_(self):
        return self._artop_differentiatedServiceField

    @property
    def flowLabel_(self):
        return self._artop_flowLabel

    @property
    def pathMtuDiscoveryEnabled_(self):
        if self._artop_pathMtuDiscoveryEnabled:
            if self._artop_pathMtuDiscoveryEnabled == "true":
                return True
            return False
        else:
            return self._artop_pathMtuDiscoveryEnabled

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
    def bundledConnections_SocketConnection(self):
        return self._artop_bundledConnection

    @property
    def pdus_SocketConnectionIpduIdentifier(self):
        return self._artop_pdu

    @property
    def ref_serverPort_(self):
        return self._artop_serverPortRef

    @property
    def serverPort_(self):
        if self._artop_serverPortRef is not None:
            if hasattr(self._artop_serverPortRef, "uuid"):
                return self._artop_serverPortRef.uuid
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
