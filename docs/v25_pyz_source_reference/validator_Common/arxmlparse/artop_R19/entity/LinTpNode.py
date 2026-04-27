# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinTpNode.py
from .Identifiable import Identifiable

class LinTpNode(Identifiable):

    def __init__(self):
        super().__init__()
        from .LinTpConfig import LinTpConfig
        from .CommunicationConnector import CommunicationConnector
        from .TpAddress import TpAddress
        from .VariationPoint import VariationPoint
        self._artop_maxNumberOfRespPendingFrames = None
        self._artop_p2Max = None
        self._artop_p2Timing = None
        self._artop_linTpConfig = None
        self._artop_connectorRef = None
        self._artop_tpAddressRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_linTpConfig': '"LIN-TP-CONFIG"', 
         '_artop_connectorRef': '"COMMUNICATION-CONNECTOR"', 
         '_artop_tpAddressRef': '"TP-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def maxNumberOfRespPendingFrames_(self):
        if self._artop_maxNumberOfRespPendingFrames:
            return int(self._artop_maxNumberOfRespPendingFrames)
        return self._artop_maxNumberOfRespPendingFrames

    @property
    def p2Max_(self):
        return self._artop_p2Max

    @property
    def p2Timing_(self):
        return self._artop_p2Timing

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
    def ref_connector_(self):
        return self._artop_connectorRef

    @property
    def connector_(self):
        if self._artop_connectorRef is not None:
            if hasattr(self._artop_connectorRef, "uuid"):
                return self._artop_connectorRef.uuid
        return

    @property
    def ref_tpAddress_(self):
        return self._artop_tpAddressRef

    @property
    def tpAddress_(self):
        if self._artop_tpAddressRef is not None:
            if hasattr(self._artop_tpAddressRef, "uuid"):
                return self._artop_tpAddressRef.uuid
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
