# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\HwPinGroupConnector.py
from .Describable import Describable

class HwPinGroupConnector(Describable):

    def __init__(self):
        super().__init__()
        from .HwElementConnector import HwElementConnector
        from .HwPinConnector import HwPinConnector
        from .HwPinGroup import HwPinGroup
        from .VariationPoint import VariationPoint
        self._artop_hwElementConnector = None
        self._artop_hwPinConnection = []
        self._artop_hwPinGroupRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_hwElementConnector': '"HW-ELEMENT-CONNECTOR"', 
         '_artop_hwPinConnection': '"HW-PIN-CONNECTOR"', 
         '_artop_hwPinGroupRef': '"HW-PIN-GROUP"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_hwElementConnector_(self):
        return self._artop_hwElementConnector

    @property
    def hwElementConnector_(self):
        if self._artop_hwElementConnector is not None:
            if hasattr(self._artop_hwElementConnector, "uuid"):
                return self._artop_hwElementConnector.uuid
        return

    @property
    def hwPinConnections_HwPinConnector(self):
        return self._artop_hwPinConnection

    @property
    def ref_hwPinGroups_(self):
        return self._artop_hwPinGroupRef

    @property
    def hwPinGroups_(self):
        return self._artop_hwPinGroupRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
