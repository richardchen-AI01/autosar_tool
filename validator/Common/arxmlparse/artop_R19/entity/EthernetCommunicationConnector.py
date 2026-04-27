# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetCommunicationConnector.py
from .CommunicationConnector import CommunicationConnector

class EthernetCommunicationConnector(CommunicationConnector):

    def __init__(self):
        super().__init__()
        from .NetworkEndpoint import NetworkEndpoint
        self._artop_ipV6PathMtuEnabled = None
        self._artop_ipV6PathMtuTimeout = None
        self._artop_maximumTransmissionUnit = None
        self._artop_neighborCacheSize = None
        self._artop_pathMtuEnabled = None
        self._artop_pathMtuTimeout = None
        self._artop_pncFilterDataMask = None
        self._artop_networkEndpointRef = []
        self._artop_unicastNetworkEndpointRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkEndpointRef':"NETWORK-ENDPOINT", 
         '_artop_unicastNetworkEndpointRef':"NETWORK-ENDPOINT"})

    @property
    def ipV6PathMtuEnabled_(self):
        if self._artop_ipV6PathMtuEnabled:
            if self._artop_ipV6PathMtuEnabled == "true":
                return True
            return False
        else:
            return self._artop_ipV6PathMtuEnabled

    @property
    def ipV6PathMtuTimeout_(self):
        return self._artop_ipV6PathMtuTimeout

    @property
    def maximumTransmissionUnit_(self):
        return self._artop_maximumTransmissionUnit

    @property
    def neighborCacheSize_(self):
        return self._artop_neighborCacheSize

    @property
    def pathMtuEnabled_(self):
        if self._artop_pathMtuEnabled:
            if self._artop_pathMtuEnabled == "true":
                return True
            return False
        else:
            return self._artop_pathMtuEnabled

    @property
    def pathMtuTimeout_(self):
        return self._artop_pathMtuTimeout

    @property
    def pncFilterDataMask_(self):
        return self._artop_pncFilterDataMask

    @property
    def ref_networkEndpoints_(self):
        return self._artop_networkEndpointRef

    @property
    def networkEndpoints_(self):
        return self._artop_networkEndpointRef

    @property
    def ref_unicastNetworkEndpoint_(self):
        return self._artop_unicastNetworkEndpointRef

    @property
    def unicastNetworkEndpoint_(self):
        if self._artop_unicastNetworkEndpointRef is not None:
            if hasattr(self._artop_unicastNetworkEndpointRef, "uuid"):
                return self._artop_unicastNetworkEndpointRef.uuid
        return
