# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanTpConfig.py
from .TpConfig import TpConfig

class CanTpConfig(TpConfig):

    def __init__(self):
        super().__init__()
        from .CanTpAddress import CanTpAddress
        from .CanTpChannel import CanTpChannel
        from .CanTpConnection import CanTpConnection
        from .CanTpEcu import CanTpEcu
        from .CanTpNode import CanTpNode
        self._artop_tpAddress = []
        self._artop_tpChannel = []
        self._artop_tpConnection = []
        self._artop_tpEcu = []
        self._artop_tpNode = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_tpAddress': '"CAN-TP-ADDRESS"', 
         '_artop_tpChannel': '"CAN-TP-CHANNEL"', 
         '_artop_tpConnection': '"CAN-TP-CONNECTION"', 
         '_artop_tpEcu': '"CAN-TP-ECU"', 
         '_artop_tpNode': '"CAN-TP-NODE"'})

    @property
    def tpAddress_CanTpAddress(self):
        return self._artop_tpAddress

    @property
    def tpChannels_CanTpChannel(self):
        return self._artop_tpChannel

    @property
    def tpConnections_CanTpConnection(self):
        return self._artop_tpConnection

    @property
    def tpEcus_CanTpEcu(self):
        return self._artop_tpEcu

    @property
    def tpNodes_CanTpNode(self):
        return self._artop_tpNode
