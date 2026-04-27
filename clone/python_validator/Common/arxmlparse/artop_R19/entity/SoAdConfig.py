# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoAdConfig.py
from .ARObject import ARObject

class SoAdConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        from .SocketConnection import SocketConnection
        from .SocketConnectionBundle import SocketConnectionBundle
        from .LogicAddress import LogicAddress
        from .SocketAddress import SocketAddress
        self._artop_ethernetPhysicalChannel = None
        self._artop_connection = []
        self._artop_connectionBundle = []
        self._artop_logicAddress = []
        self._artop_socketAddress = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_ethernetPhysicalChannel': '"ETHERNET-PHYSICAL-CHANNEL"', 
         '_artop_connection': '"SOCKET-CONNECTION"', 
         '_artop_connectionBundle': '"SOCKET-CONNECTION-BUNDLE"', 
         '_artop_logicAddress': '"LOGIC-ADDRESS"', 
         '_artop_socketAddress': '"SOCKET-ADDRESS"'})

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
    def connections_SocketConnection(self):
        return self._artop_connection

    @property
    def connectionBundles_SocketConnectionBundle(self):
        return self._artop_connectionBundle

    @property
    def logicAddress_LogicAddress(self):
        return self._artop_logicAddress

    @property
    def socketAddress_SocketAddress(self):
        return self._artop_socketAddress
