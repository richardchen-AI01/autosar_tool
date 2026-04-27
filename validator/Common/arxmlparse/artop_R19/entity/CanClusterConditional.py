# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanClusterConditional.py
from .CanClusterContent import CanClusterContent

class CanClusterConditional(CanClusterContent):

    def __init__(self):
        super().__init__()
        from .CanCluster import CanCluster
        from .VariationPoint import VariationPoint
        self._artop_canCluster = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_canCluster':"CAN-CLUSTER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_canCluster_(self):
        return self._artop_canCluster

    @property
    def canCluster_(self):
        if self._artop_canCluster is not None:
            if hasattr(self._artop_canCluster, "uuid"):
                return self._artop_canCluster.uuid
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
