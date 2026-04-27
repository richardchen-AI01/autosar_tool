# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanTpAddress.py
from .Identifiable import Identifiable

class CanTpAddress(Identifiable):

    def __init__(self):
        super().__init__()
        from .CanTpConfig import CanTpConfig
        from .VariationPoint import VariationPoint
        self._artop_tpAddress = None
        self._artop_tpAddressExtensionValue = None
        self._artop_canTpConfig = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_canTpConfig':"CAN-TP-CONFIG", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def tpAddress_(self):
        if self._artop_tpAddress:
            return int(self._artop_tpAddress)
        return self._artop_tpAddress

    @property
    def tpAddressExtensionValue_(self):
        if self._artop_tpAddressExtensionValue:
            return int(self._artop_tpAddressExtensionValue)
        return self._artop_tpAddressExtensionValue

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
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
