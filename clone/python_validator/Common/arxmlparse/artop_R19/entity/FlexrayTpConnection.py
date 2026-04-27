# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayTpConnection.py
from .TpConnection import TpConnection

class FlexrayTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .FlexrayTpConfig import FlexrayTpConfig
        from .IPdu import IPdu
        from .TpAddress import TpAddress
        from .FlexrayTpNode import FlexrayTpNode
        from .FlexrayTpPduPool import FlexrayTpPduPool
        from .FlexrayTpConnectionControl import FlexrayTpConnectionControl
        from .VariationPoint import VariationPoint
        self._artop_bandwidthLimitation = None
        self._artop_flexrayTpConfig = None
        self._artop_directTpSduRef = None
        self._artop_multicastRef = None
        self._artop_receiverRef = []
        self._artop_reversedTpSduRef = None
        self._artop_rxPduPoolRef = None
        self._artop_tpConnectionControlRef = None
        self._artop_transmitterRef = None
        self._artop_txPduPoolRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flexrayTpConfig': '"FLEXRAY-TP-CONFIG"', 
         '_artop_directTpSduRef': '"I-PDU"', 
         '_artop_multicastRef': '"TP-ADDRESS"', 
         '_artop_receiverRef': '"FLEXRAY-TP-NODE"', 
         '_artop_reversedTpSduRef': '"I-PDU"', 
         '_artop_rxPduPoolRef': '"FLEXRAY-TP-PDU-POOL"', 
         '_artop_tpConnectionControlRef': '"FLEXRAY-TP-CONNECTION-CONTROL"', 
         '_artop_transmitterRef': '"FLEXRAY-TP-NODE"', 
         '_artop_txPduPoolRef': '"FLEXRAY-TP-PDU-POOL"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def bandwidthLimitation_(self):
        if self._artop_bandwidthLimitation:
            if self._artop_bandwidthLimitation == "true":
                return True
            return False
        else:
            return self._artop_bandwidthLimitation

    @property
    def ref_flexrayTpConfig_(self):
        return self._artop_flexrayTpConfig

    @property
    def flexrayTpConfig_(self):
        if self._artop_flexrayTpConfig is not None:
            if hasattr(self._artop_flexrayTpConfig, "uuid"):
                return self._artop_flexrayTpConfig.uuid
        return

    @property
    def ref_directTpSdu_(self):
        return self._artop_directTpSduRef

    @property
    def directTpSdu_(self):
        if self._artop_directTpSduRef is not None:
            if hasattr(self._artop_directTpSduRef, "uuid"):
                return self._artop_directTpSduRef.uuid
        return

    @property
    def ref_multicast_(self):
        return self._artop_multicastRef

    @property
    def multicast_(self):
        if self._artop_multicastRef is not None:
            if hasattr(self._artop_multicastRef, "uuid"):
                return self._artop_multicastRef.uuid
        return

    @property
    def ref_receivers_(self):
        return self._artop_receiverRef

    @property
    def receivers_(self):
        return self._artop_receiverRef

    @property
    def ref_reversedTpSdu_(self):
        return self._artop_reversedTpSduRef

    @property
    def reversedTpSdu_(self):
        if self._artop_reversedTpSduRef is not None:
            if hasattr(self._artop_reversedTpSduRef, "uuid"):
                return self._artop_reversedTpSduRef.uuid
        return

    @property
    def ref_rxPduPool_(self):
        return self._artop_rxPduPoolRef

    @property
    def rxPduPool_(self):
        if self._artop_rxPduPoolRef is not None:
            if hasattr(self._artop_rxPduPoolRef, "uuid"):
                return self._artop_rxPduPoolRef.uuid
        return

    @property
    def ref_tpConnectionControl_(self):
        return self._artop_tpConnectionControlRef

    @property
    def tpConnectionControl_(self):
        if self._artop_tpConnectionControlRef is not None:
            if hasattr(self._artop_tpConnectionControlRef, "uuid"):
                return self._artop_tpConnectionControlRef.uuid
        return

    @property
    def ref_transmitter_(self):
        return self._artop_transmitterRef

    @property
    def transmitter_(self):
        if self._artop_transmitterRef is not None:
            if hasattr(self._artop_transmitterRef, "uuid"):
                return self._artop_transmitterRef.uuid
        return

    @property
    def ref_txPduPool_(self):
        return self._artop_txPduPoolRef

    @property
    def txPduPool_(self):
        if self._artop_txPduPoolRef is not None:
            if hasattr(self._artop_txPduPoolRef, "uuid"):
                return self._artop_txPduPoolRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
