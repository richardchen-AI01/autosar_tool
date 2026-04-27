# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwElementConnector.py
from .Describable import Describable

class HwElementConnector(Describable):

    def __init__(self):
        super().__init__()
        from .HwElement import HwElement
        from .HwPinGroupConnector import HwPinGroupConnector
        from .HwPinConnector import HwPinConnector
        from .VariationPoint import VariationPoint
        self._artop_hwElement = None
        self._artop_hwElementRef = []
        self._artop_hwPinGroupConnection = []
        self._artop_hwPinConnection = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_hwElement': '"HW-ELEMENT"', 
         '_artop_hwElementRef': '"HW-ELEMENT"', 
         '_artop_hwPinGroupConnection': '"HW-PIN-GROUP-CONNECTOR"', 
         '_artop_hwPinConnection': '"HW-PIN-CONNECTOR"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_hwElement_(self):
        return self._artop_hwElement

    @property
    def hwElement_(self):
        if self._artop_hwElement is not None:
            if hasattr(self._artop_hwElement, "uuid"):
                return self._artop_hwElement.uuid
        return

    @property
    def ref_hwElements_(self):
        return self._artop_hwElementRef

    @property
    def hwElements_(self):
        return self._artop_hwElementRef

    @property
    def hwPinGroupConnections_HwPinGroupConnector(self):
        return self._artop_hwPinGroupConnection

    @property
    def hwPinConnections_HwPinConnector(self):
        return self._artop_hwPinConnection

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
