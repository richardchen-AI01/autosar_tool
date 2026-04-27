# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwPin.py
from .HwDescriptionEntity import HwDescriptionEntity
from .Identifiable import Identifiable

class HwPin(Identifiable, HwDescriptionEntity):

    def __init__(self):
        super().__init__()
        from .HwPinGroupContent import HwPinGroupContent
        from .VariationPoint import VariationPoint
        self._artop_pinNumber = None
        self._artop_hwPinGroupContent = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_hwPinGroupContent':"HW-PIN-GROUP-CONTENT", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def pinNumber_(self):
        if self._artop_pinNumber:
            return int(self._artop_pinNumber)
        return self._artop_pinNumber

    @property
    def ref_hwPinGroupContent_(self):
        return self._artop_hwPinGroupContent

    @property
    def hwPinGroupContent_(self):
        if self._artop_hwPinGroupContent is not None:
            if hasattr(self._artop_hwPinGroupContent, "uuid"):
                return self._artop_hwPinGroupContent.uuid
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
