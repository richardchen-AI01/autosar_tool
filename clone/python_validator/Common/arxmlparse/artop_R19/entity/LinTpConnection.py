# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinTpConnection.py
from .TpConnection import TpConnection

class LinTpConnection(TpConnection):

    def __init__(self):
        super().__init__()
        from .LinTpConfig import LinTpConfig
        from .NPdu import NPdu
        from .IPdu import IPdu
        from .TpAddress import TpAddress
        from .LinTpNode import LinTpNode
        from .VariationPoint import VariationPoint
        self._artop_dropNotRequestedNad = None
        self._artop_maxNumberOfRespPendingFrames = None
        self._artop_p2Max = None
        self._artop_p2Timing = None
        self._artop_timeoutAs = None
        self._artop_timeoutCr = None
        self._artop_timeoutCs = None
        self._artop_linTpConfig = None
        self._artop_dataPduRef = None
        self._artop_flowControlRef = None
        self._artop_linTpNSduRef = None
        self._artop_multicastRef = None
        self._artop_receiverRef = []
        self._artop_transmitterRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_linTpConfig': '"LIN-TP-CONFIG"', 
         '_artop_dataPduRef': '"N-PDU"', 
         '_artop_flowControlRef': '"N-PDU"', 
         '_artop_linTpNSduRef': '"I-PDU"', 
         '_artop_multicastRef': '"TP-ADDRESS"', 
         '_artop_receiverRef': '"LIN-TP-NODE"', 
         '_artop_transmitterRef': '"LIN-TP-NODE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def dropNotRequestedNad_(self):
        if self._artop_dropNotRequestedNad:
            if self._artop_dropNotRequestedNad == "true":
                return True
            return False
        else:
            return self._artop_dropNotRequestedNad

    @property
    def maxNumberOfRespPendingFrames_(self):
        return self._artop_maxNumberOfRespPendingFrames

    @property
    def p2Max_(self):
        return self._artop_p2Max

    @property
    def p2Timing_(self):
        return self._artop_p2Timing

    @property
    def timeoutAs_(self):
        return self._artop_timeoutAs

    @property
    def timeoutCr_(self):
        return self._artop_timeoutCr

    @property
    def timeoutCs_(self):
        return self._artop_timeoutCs

    @property
    def ref_linTpConfig_(self):
        return self._artop_linTpConfig

    @property
    def linTpConfig_(self):
        if self._artop_linTpConfig is not None:
            if hasattr(self._artop_linTpConfig, "uuid"):
                return self._artop_linTpConfig.uuid
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
    def ref_flowControl_(self):
        return self._artop_flowControlRef

    @property
    def flowControl_(self):
        if self._artop_flowControlRef is not None:
            if hasattr(self._artop_flowControlRef, "uuid"):
                return self._artop_flowControlRef.uuid
        return

    @property
    def ref_linTpNSdu_(self):
        return self._artop_linTpNSduRef

    @property
    def linTpNSdu_(self):
        if self._artop_linTpNSduRef is not None:
            if hasattr(self._artop_linTpNSduRef, "uuid"):
                return self._artop_linTpNSduRef.uuid
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
