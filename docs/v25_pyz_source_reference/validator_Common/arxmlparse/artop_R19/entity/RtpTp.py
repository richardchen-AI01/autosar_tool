# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RtpTp.py
from .TransportProtocolConfiguration import TransportProtocolConfiguration

class RtpTp(TransportProtocolConfiguration):

    def __init__(self):
        super().__init__()
        from .TcpUdpConfig import TcpUdpConfig
        self._artop_ssrc = None
        self._artop_tcpUdpConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tcpUdpConfig": "TCP-UDP-CONFIG"})

    @property
    def ssrc_(self):
        return self._artop_ssrc

    @property
    def ref_tcpUdpConfig_(self):
        return self._artop_tcpUdpConfig

    @property
    def tcpUdpConfig_(self):
        if self._artop_tcpUdpConfig is not None:
            if hasattr(self._artop_tcpUdpConfig, "uuid"):
                return self._artop_tcpUdpConfig.uuid
        return
