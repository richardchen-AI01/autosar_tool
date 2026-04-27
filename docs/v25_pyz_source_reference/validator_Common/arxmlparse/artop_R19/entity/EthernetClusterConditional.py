# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetClusterConditional.py
from .EthernetClusterContent import EthernetClusterContent

class EthernetClusterConditional(EthernetClusterContent):

    def __init__(self):
        super().__init__()
        from .EthernetCluster import EthernetCluster
        from .VariationPoint import VariationPoint
        self._artop_ethernetCluster = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ethernetCluster':"ETHERNET-CLUSTER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_ethernetCluster_(self):
        return self._artop_ethernetCluster

    @property
    def ethernetCluster_(self):
        if self._artop_ethernetCluster is not None:
            if hasattr(self._artop_ethernetCluster, "uuid"):
                return self._artop_ethernetCluster.uuid
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
