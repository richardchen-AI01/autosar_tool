# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayTpEcu.py
from .ARObject import ARObject

class FlexrayTpEcu(ARObject):

    def __init__(self):
        super().__init__()
        from .FlexrayTpConfig import FlexrayTpConfig
        from .EcuInstance import EcuInstance
        from .VariationPoint import VariationPoint
        self._artop_cancellation = None
        self._artop_cycleTimeMainFunction = None
        self._artop_fullDuplexEnabled = None
        self._artop_transmitCancellation = None
        self._artop_flexrayTpConfig = None
        self._artop_ecuInstanceRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_flexrayTpConfig':"FLEXRAY-TP-CONFIG", 
         '_artop_ecuInstanceRef':"ECU-INSTANCE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def cancellation_(self):
        if self._artop_cancellation:
            if self._artop_cancellation == "true":
                return True
            return False
        else:
            return self._artop_cancellation

    @property
    def cycleTimeMainFunction_(self):
        return self._artop_cycleTimeMainFunction

    @property
    def fullDuplexEnabled_(self):
        if self._artop_fullDuplexEnabled:
            if self._artop_fullDuplexEnabled == "true":
                return True
            return False
        else:
            return self._artop_fullDuplexEnabled

    @property
    def transmitCancellation_(self):
        if self._artop_transmitCancellation:
            if self._artop_transmitCancellation == "true":
                return True
            return False
        else:
            return self._artop_transmitCancellation

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
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
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
