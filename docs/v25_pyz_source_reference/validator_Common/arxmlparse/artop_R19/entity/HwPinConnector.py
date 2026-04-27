# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwPinConnector.py
from .Describable import Describable

class HwPinConnector(Describable):

    def __init__(self):
        super().__init__()
        from .HwPin import HwPin
        from .VariationPoint import VariationPoint
        self._artop_hwPinRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_hwPinRef':"HW-PIN", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_hwPins_(self):
        return self._artop_hwPinRef

    @property
    def hwPins_(self):
        return self._artop_hwPinRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
