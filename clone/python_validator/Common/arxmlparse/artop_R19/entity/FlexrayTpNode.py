# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayTpNode.py
from .Identifiable import Identifiable

class FlexrayTpNode(Identifiable):

    def __init__(self):
        super().__init__()
        from .FlexrayTpConfig import FlexrayTpConfig
        from .CommunicationConnector import CommunicationConnector
        from .TpAddress import TpAddress
        from .VariationPoint import VariationPoint
        self._artop_flexrayTpConfig = None
        self._artop_connectorRef = []
        self._artop_tpAddressRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flexrayTpConfig': '"FLEXRAY-TP-CONFIG"', 
         '_artop_connectorRef': '"COMMUNICATION-CONNECTOR"', 
         '_artop_tpAddressRef': '"TP-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

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
    def ref_connectors_(self):
        return self._artop_connectorRef

    @property
    def connectors_(self):
        return self._artop_connectorRef

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
