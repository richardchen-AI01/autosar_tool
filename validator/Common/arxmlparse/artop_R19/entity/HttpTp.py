# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HttpTp.py
from .TransportProtocolConfiguration import TransportProtocolConfiguration

class HttpTp(TransportProtocolConfiguration):

    def __init__(self):
        super().__init__()
        from .TcpTp import TcpTp
        self._artop_contentType = None
        self._artop_protocolVersion = None
        self._artop_requestMethod = None
        self._artop_uri = None
        self._artop_tcpTpConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tcpTpConfig": "TCP-TP"})

    @property
    def contentType_(self):
        return self._artop_contentType

    @property
    def protocolVersion_(self):
        return self._artop_protocolVersion

    @property
    def requestMethod_(self):
        return self._artop_requestMethod

    @property
    def uri_(self):
        return self._artop_uri

    @property
    def ref_tcpTpConfig_(self):
        return self._artop_tcpTpConfig

    @property
    def tcpTpConfig_(self):
        if self._artop_tcpTpConfig is not None:
            if hasattr(self._artop_tcpTpConfig, "uuid"):
                return self._artop_tcpTpConfig.uuid
        return
