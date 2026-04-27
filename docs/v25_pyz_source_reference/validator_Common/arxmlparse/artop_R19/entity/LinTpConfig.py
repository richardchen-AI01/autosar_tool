# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinTpConfig.py
from .TpConfig import TpConfig

class LinTpConfig(TpConfig):

    def __init__(self):
        super().__init__()
        from .TpAddress import TpAddress
        from .LinTpConnection import LinTpConnection
        from .LinTpNode import LinTpNode
        self._artop_tpAddress = []
        self._artop_tpConnection = []
        self._artop_tpNode = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tpAddress':"TP-ADDRESS", 
         '_artop_tpConnection':"LIN-TP-CONNECTION", 
         '_artop_tpNode':"LIN-TP-NODE"})

    @property
    def tpAddress_TpAddress(self):
        return self._artop_tpAddress

    @property
    def tpConnections_LinTpConnection(self):
        return self._artop_tpConnection

    @property
    def tpNodes_LinTpNode(self):
        return self._artop_tpNode
