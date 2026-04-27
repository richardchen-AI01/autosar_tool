# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TcpTp.py
from .TcpUdpConfig import TcpUdpConfig

class TcpTp(TcpUdpConfig):

    def __init__(self):
        super().__init__()
        from .HttpTp import HttpTp
        from .TpPort import TpPort
        self._artop_keepAliveInterval = None
        self._artop_keepAliveProbesMax = None
        self._artop_keepAliveTime = None
        self._artop_keepAlives = None
        self._artop_naglesAlgorithm = None
        self._artop_receiveWindowMin = None
        self._artop_httpTp = None
        self._artop_tcpTpPort = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_httpTp':"HTTP-TP", 
         '_artop_tcpTpPort':"TP-PORT"})

    @property
    def keepAliveInterval_(self):
        return self._artop_keepAliveInterval

    @property
    def keepAliveProbesMax_(self):
        return self._artop_keepAliveProbesMax

    @property
    def keepAliveTime_(self):
        return self._artop_keepAliveTime

    @property
    def keepAlives_(self):
        if self._artop_keepAlives:
            if self._artop_keepAlives == "true":
                return True
            return False
        else:
            return self._artop_keepAlives

    @property
    def naglesAlgorithm_(self):
        if self._artop_naglesAlgorithm:
            if self._artop_naglesAlgorithm == "true":
                return True
            return False
        else:
            return self._artop_naglesAlgorithm

    @property
    def receiveWindowMin_(self):
        return self._artop_receiveWindowMin

    @property
    def ref_httpTp_(self):
        return self._artop_httpTp

    @property
    def httpTp_(self):
        if self._artop_httpTp is not None:
            if hasattr(self._artop_httpTp, "uuid"):
                return self._artop_httpTp.uuid
        return

    @property
    def ref_tcpTpPort_(self):
        return self._artop_tcpTpPort

    @property
    def tcpTpPort_(self):
        if self._artop_tcpTpPort is not None:
            if hasattr(self._artop_tcpTpPort, "uuid"):
                return self._artop_tcpTpPort.uuid
        return
