# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayArTpConfig.py
from .TpConfig import TpConfig

class FlexrayArTpConfig(TpConfig):

    def __init__(self):
        super().__init__()
        from .TpAddress import TpAddress
        from .FlexrayArTpChannel import FlexrayArTpChannel
        from .FlexrayArTpNode import FlexrayArTpNode
        self._artop_tpAddress = []
        self._artop_tpChannel = []
        self._artop_tpNode = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_tpAddress':"TP-ADDRESS", 
         '_artop_tpChannel':"FLEXRAY-AR-TP-CHANNEL", 
         '_artop_tpNode':"FLEXRAY-AR-TP-NODE"})

    @property
    def tpAddress_TpAddress(self):
        return self._artop_tpAddress

    @property
    def tpChannels_FlexrayArTpChannel(self):
        return self._artop_tpChannel

    @property
    def tpNodes_FlexrayArTpNode(self):
        return self._artop_tpNode
