# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthTpConnection.py
from .TpConnection import TpConnection

class EthTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .EthTpConfig import EthTpConfig
        from .PduTriggering import PduTriggering
        self._artop_ethTpConfig = None
        self._artop_tpSduRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ethTpConfig':"ETH-TP-CONFIG", 
         '_artop_tpSduRef':"PDU-TRIGGERING"})

    @property
    def ref_ethTpConfig_(self):
        return self._artop_ethTpConfig

    @property
    def ethTpConfig_(self):
        if self._artop_ethTpConfig is not None:
            if hasattr(self._artop_ethTpConfig, "uuid"):
                return self._artop_ethTpConfig.uuid
        return

    @property
    def ref_tpSdus_(self):
        return self._artop_tpSduRef

    @property
    def tpSdus_(self):
        return self._artop_tpSduRef
