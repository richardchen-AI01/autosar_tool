# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939TpConnection.py
from .TpConnection import TpConnection

class J1939TpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .J1939TpConfig import J1939TpConfig
        from .NPdu import NPdu
        from .J1939TpNode import J1939TpNode
        from .J1939TpPg import J1939TpPg
        from .IPdu import IPdu
        from .VariationPoint import VariationPoint
        self._artop_broadcast = None
        self._artop_bufferRatio = None
        self._artop_cancellation = None
        self._artop_dynamicBs = None
        self._artop_maxBs = None
        self._artop_maxExpBs = None
        self._artop_retry = None
        self._artop_j1939TpConfig = None
        self._artop_dataPduRef = None
        self._artop_directPduRef = None
        self._artop_flowControlPduRef = []
        self._artop_receiverRef = []
        self._artop_tpPg = []
        self._artop_tpSduRef = []
        self._artop_transmitterRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_j1939TpConfig': '"J-1939-TP-CONFIG"', 
         '_artop_dataPduRef': '"N-PDU"', 
         '_artop_directPduRef': '"N-PDU"', 
         '_artop_flowControlPduRef': '"N-PDU"', 
         '_artop_receiverRef': '"J-1939-TP-NODE"', 
         '_artop_tpPg': '"J-1939-TP-PG"', 
         '_artop_tpSduRef': '"I-PDU"', 
         '_artop_transmitterRef': '"J-1939-TP-NODE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def broadcast_(self):
        if self._artop_broadcast:
            if self._artop_broadcast == "true":
                return True
            return False
        else:
            return self._artop_broadcast

    @property
    def bufferRatio_(self):
        return self._artop_bufferRatio

    @property
    def cancellation_(self):
        if self._artop_cancellation:
            if self._artop_cancellation == "true":
                return True
            return False
        else:
            return self._artop_cancellation

    @property
    def dynamicBs_(self):
        if self._artop_dynamicBs:
            if self._artop_dynamicBs == "true":
                return True
            return False
        else:
            return self._artop_dynamicBs

    @property
    def maxBs_(self):
        return self._artop_maxBs

    @property
    def maxExpBs_(self):
        return self._artop_maxExpBs

    @property
    def retry_(self):
        if self._artop_retry:
            if self._artop_retry == "true":
                return True
            return False
        else:
            return self._artop_retry

    @property
    def ref_j1939TpConfig_(self):
        return self._artop_j1939TpConfig

    @property
    def j1939TpConfig_(self):
        if self._artop_j1939TpConfig is not None:
            if hasattr(self._artop_j1939TpConfig, "uuid"):
                return self._artop_j1939TpConfig.uuid
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
    def ref_directPdu_(self):
        return self._artop_directPduRef

    @property
    def directPdu_(self):
        if self._artop_directPduRef is not None:
            if hasattr(self._artop_directPduRef, "uuid"):
                return self._artop_directPduRef.uuid
        return

    @property
    def ref_flowControlPdus_(self):
        return self._artop_flowControlPduRef

    @property
    def flowControlPdus_(self):
        return self._artop_flowControlPduRef

    @property
    def ref_receivers_(self):
        return self._artop_receiverRef

    @property
    def receivers_(self):
        return self._artop_receiverRef

    @property
    def tpPgs_J1939TpPg(self):
        return self._artop_tpPg

    @property
    def ref_tpSdus_(self):
        return self._artop_tpSduRef

    @property
    def tpSdus_(self):
        return self._artop_tpSduRef

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
