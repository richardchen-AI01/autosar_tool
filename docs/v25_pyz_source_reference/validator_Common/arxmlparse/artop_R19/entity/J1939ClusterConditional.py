# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939ClusterConditional.py
from .J1939ClusterContent import J1939ClusterContent

class J1939ClusterConditional(J1939ClusterContent):

    def __init__(self):
        super().__init__()
        from .J1939Cluster import J1939Cluster
        from .VariationPoint import VariationPoint
        self._artop_j1939Cluster = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_j1939Cluster':"J-1939-CLUSTER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_j1939Cluster_(self):
        return self._artop_j1939Cluster

    @property
    def j1939Cluster_(self):
        if self._artop_j1939Cluster is not None:
            if hasattr(self._artop_j1939Cluster, "uuid"):
                return self._artop_j1939Cluster.uuid
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
