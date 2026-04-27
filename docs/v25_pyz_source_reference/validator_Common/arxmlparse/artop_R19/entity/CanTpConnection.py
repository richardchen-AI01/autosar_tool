# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanTpConnection.py
from .TpConnection import TpConnection

class CanTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .CanTpConfig import CanTpConfig
        from .CanTpChannel import CanTpChannel
        from .NPdu import NPdu
        from .CanTpAddress import CanTpAddress
        from .CanTpNode import CanTpNode
        from .IPdu import IPdu
        from .VariationPoint import VariationPoint
        self._artop_addressingFormat = None
        self._artop_cancellation = None
        self._artop_maxBlockSize = None
        self._artop_paddingActivation = None
        self._artop_taType = None
        self._artop_timeoutBr = None
        self._artop_timeoutBs = None
        self._artop_timeoutCr = None
        self._artop_timeoutCs = None
        self._artop_transmitCancellation = None
        self._artop_canTpConfig = None
        self._artop_canTpChannelRef = None
        self._artop_dataPduRef = None
        self._artop_flowControlPduRef = None
        self._artop_multicastRef = None
        self._artop_receiverRef = []
        self._artop_tpSduRef = None
        self._artop_transmitterRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_canTpConfig': '"CAN-TP-CONFIG"', 
         '_artop_canTpChannelRef': '"CAN-TP-CHANNEL"', 
         '_artop_dataPduRef': '"N-PDU"', 
         '_artop_flowControlPduRef': '"N-PDU"', 
         '_artop_multicastRef': '"CAN-TP-ADDRESS"', 
         '_artop_receiverRef': '"CAN-TP-NODE"', 
         '_artop_tpSduRef': '"I-PDU"', 
         '_artop_transmitterRef': '"CAN-TP-NODE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def addressingFormat_(self):
        return self._artop_addressingFormat

    @property
    def cancellation_(self):
        if self._artop_cancellation:
            if self._artop_cancellation == "true":
                return True
            return False
        else:
            return self._artop_cancellation

    @property
    def maxBlockSize_(self):
        if self._artop_maxBlockSize:
            return int(self._artop_maxBlockSize)
        return self._artop_maxBlockSize

    @property
    def paddingActivation_(self):
        if self._artop_paddingActivation:
            if self._artop_paddingActivation == "true":
                return True
            return False
        else:
            return self._artop_paddingActivation

    @property
    def taType_(self):
        return self._artop_taType

    @property
    def timeoutBr_(self):
        return self._artop_timeoutBr

    @property
    def timeoutBs_(self):
        return self._artop_timeoutBs

    @property
    def timeoutCr_(self):
        return self._artop_timeoutCr

    @property
    def timeoutCs_(self):
        return self._artop_timeoutCs

    @property
    def transmitCancellation_(self):
        if self._artop_transmitCancellation:
            if self._artop_transmitCancellation == "true":
                return True
            return False
        else:
            return self._artop_transmitCancellation

    @property
    def ref_canTpConfig_(self):
        return self._artop_canTpConfig

    @property
    def canTpConfig_(self):
        if self._artop_canTpConfig is not None:
            if hasattr(self._artop_canTpConfig, "uuid"):
                return self._artop_canTpConfig.uuid
        return

    @property
    def ref_canTpChannel_(self):
        return self._artop_canTpChannelRef

    @property
    def canTpChannel_(self):
        if self._artop_canTpChannelRef is not None:
            if hasattr(self._artop_canTpChannelRef, "uuid"):
                return self._artop_canTpChannelRef.uuid
        return

    @property
    def ref_dataPdu_(self):
        return self._artop_dataPduRef

    @property
    def dataPdu_(self):
        if self._artop_dataPduRef is not None:
            if hasattr(self._artop_dataPduRef, "uuid"):
                return self._artop_dataPduRef.uuid
        return

    @property
    def ref_flowControlPdu_(self):
        return self._artop_flowControlPduRef

    @property
    def flowControlPdu_(self):
        if self._artop_flowControlPduRef is not None:
            if hasattr(self._artop_flowControlPduRef, "uuid"):
                return self._artop_flowControlPduRef.uuid
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
    def ref_tpSdu_(self):
        return self._artop_tpSduRef

    @property
    def tpSdu_(self):
        if self._artop_tpSduRef is not None:
            if hasattr(self._artop_tpSduRef, "uuid"):
                return self._artop_tpSduRef.uuid
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
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
