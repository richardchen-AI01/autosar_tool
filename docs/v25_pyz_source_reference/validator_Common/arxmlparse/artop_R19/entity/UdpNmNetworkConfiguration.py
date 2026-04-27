# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UdpNmNetworkConfiguration.py
from .ARObject import ARObject

class UdpNmNetworkConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .UdpNmCluster import UdpNmCluster
        self._artop_ipv4MulticastIpAddress = None
        self._artop_ipv6MulticastIpAddress = None
        self._artop_udpPort = None
        self._artop_udpNmCluster = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_udpNmCluster": "UDP-NM-CLUSTER"})

    @property
    def ipv4MulticastIpAddress_(self):
        return self._artop_ipv4MulticastIpAddress

    @property
    def ipv6MulticastIpAddress_(self):
        return self._artop_ipv6MulticastIpAddress

    @property
    def udpPort_(self):
        return self._artop_udpPort

    @property
    def ref_udpNmCluster_(self):
        return self._artop_udpNmCluster

    @property
    def udpNmCluster_(self):
        if self._artop_udpNmCluster is not None:
            if hasattr(self._artop_udpNmCluster, "uuid"):
                return self._artop_udpNmCluster.uuid
        return
