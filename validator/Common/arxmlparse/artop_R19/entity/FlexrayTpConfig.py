# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayTpConfig.py
from .TpConfig import TpConfig

class FlexrayTpConfig(TpConfig):

    def __init__(self):
        super().__init__()
        from .FlexrayTpPduPool import FlexrayTpPduPool
        from .TpAddress import TpAddress
        from .FlexrayTpConnection import FlexrayTpConnection
        from .FlexrayTpConnectionControl import FlexrayTpConnectionControl
        from .FlexrayTpEcu import FlexrayTpEcu
        from .FlexrayTpNode import FlexrayTpNode
        self._artop_pduPool = []
        self._artop_tpAddress = []
        self._artop_tpConnection = []
        self._artop_tpConnectionControl = []
        self._artop_tpEcu = []
        self._artop_tpNode = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_pduPool': '"FLEXRAY-TP-PDU-POOL"', 
         '_artop_tpAddress': '"TP-ADDRESS"', 
         '_artop_tpConnection': '"FLEXRAY-TP-CONNECTION"', 
         '_artop_tpConnectionControl': '"FLEXRAY-TP-CONNECTION-CONTROL"', 
         '_artop_tpEcu': '"FLEXRAY-TP-ECU"', 
         '_artop_tpNode': '"FLEXRAY-TP-NODE"'})

    @property
    def pduPools_FlexrayTpPduPool(self):
        return self._artop_pduPool

    @property
    def tpAddress_TpAddress(self):
        return self._artop_tpAddress

    @property
    def tpConnections_FlexrayTpConnection(self):
        return self._artop_tpConnection

    @property
    def tpConnectionControls_FlexrayTpConnectionControl(self):
        return self._artop_tpConnectionControl

    @property
    def tpEcus_FlexrayTpEcu(self):
        return self._artop_tpEcu

    @property
    def tpNodes_FlexrayTpNode(self):
        return self._artop_tpNode
