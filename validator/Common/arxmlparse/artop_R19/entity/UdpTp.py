# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UdpTp.py
from .TcpUdpConfig import TcpUdpConfig

class UdpTp(TcpUdpConfig):

    def __init__(self):
        super().__init__()
        from .TpPort import TpPort
        self._artop_udpTpPort = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_udpTpPort": "TP-PORT"})

    @property
    def ref_udpTpPort_(self):
        return self._artop_udpTpPort

    @property
    def udpTpPort_(self):
        if self._artop_udpTpPort is not None:
            if hasattr(self._artop_udpTpPort, "uuid"):
                return self._artop_udpTpPort.uuid
        return
