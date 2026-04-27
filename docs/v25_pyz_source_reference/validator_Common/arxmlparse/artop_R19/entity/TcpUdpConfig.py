# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TcpUdpConfig.py
from .TransportProtocolConfiguration import TransportProtocolConfiguration

class TcpUdpConfig(TransportProtocolConfiguration):

    def __init__(self):
        super().__init__()
        from .RtpTp import RtpTp
        self._artop_rtpTp = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_rtpTp": "RTP-TP"})

    @property
    def ref_rtpTp_(self):
        return self._artop_rtpTp

    @property
    def rtpTp_(self):
        if self._artop_rtpTp is not None:
            if hasattr(self._artop_rtpTp, "uuid"):
                return self._artop_rtpTp.uuid
        return
