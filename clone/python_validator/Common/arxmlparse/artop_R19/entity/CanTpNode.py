# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanTpNode.py
from .Identifiable import Identifiable

class CanTpNode(Identifiable):

    def __init__(self):
        super().__init__()
        from .CanTpConfig import CanTpConfig
        from .CommunicationConnector import CommunicationConnector
        from .CanTpAddress import CanTpAddress
        from .VariationPoint import VariationPoint
        self._artop_maxFcWait = None
        self._artop_stMin = None
        self._artop_timeoutAr = None
        self._artop_timeoutAs = None
        self._artop_canTpConfig = None
        self._artop_connectorRef = None
        self._artop_tpAddressRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_canTpConfig': '"CAN-TP-CONFIG"', 
         '_artop_connectorRef': '"COMMUNICATION-CONNECTOR"', 
         '_artop_tpAddressRef': '"CAN-TP-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def maxFcWait_(self):
        if self._artop_maxFcWait:
            return int(self._artop_maxFcWait)
        return self._artop_maxFcWait

    @property
    def stMin_(self):
        return self._artop_stMin

    @property
    def timeoutAr_(self):
        return self._artop_timeoutAr

    @property
    def timeoutAs_(self):
        return self._artop_timeoutAs

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
