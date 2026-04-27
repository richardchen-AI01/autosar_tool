# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthTpConfig.py
from .TpConfig import TpConfig

class EthTpConfig(TpConfig):

    def __init__(self):
        super().__init__()
        from .EthTpConnection import EthTpConnection
        self._artop_tpConnection = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tpConnection": "ETH-TP-CONNECTION"})

    @property
    def tpConnections_EthTpConnection(self):
        return self._artop_tpConnection
