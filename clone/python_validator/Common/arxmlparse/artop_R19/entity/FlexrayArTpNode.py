# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayArTpNode.py
from .Identifiable import Identifiable

class FlexrayArTpNode(Identifiable):

    def __init__(self):
        super().__init__()
        from .FlexrayArTpConfig import FlexrayArTpConfig
        from .FlexrayCommunicationConnector import FlexrayCommunicationConnector
        from .TpAddress import TpAddress
        from .VariationPoint import VariationPoint
        self._artop_flexrayArTpConfig = None
        self._artop_connectorRef = []
        self._artop_tpAddressRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flexrayArTpConfig': '"FLEXRAY-AR-TP-CONFIG"', 
         '_artop_connectorRef': '"FLEXRAY-COMMUNICATION-CONNECTOR"', 
         '_artop_tpAddressRef': '"TP-ADDRESS"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_flexrayArTpConfig_(self):
        return self._artop_flexrayArTpConfig

    @property
    def flexrayArTpConfig_(self):
        if self._artop_flexrayArTpConfig is not None:
            if hasattr(self._artop_flexrayArTpConfig, "uuid"):
                return self._artop_flexrayArTpConfig.uuid
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
