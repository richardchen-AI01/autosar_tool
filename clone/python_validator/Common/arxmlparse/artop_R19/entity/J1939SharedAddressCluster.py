# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939SharedAddressCluster.py
from .Identifiable import Identifiable

class J1939SharedAddressCluster(Identifiable):

    def __init__(self):
        super().__init__()
        from .System import System
        from .J1939Cluster import J1939Cluster
        from .VariationPoint import VariationPoint
        self._artop_system = None
        self._artop_participatingJ1939ClusterRef = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_system':"SYSTEM", 
         '_artop_participatingJ1939ClusterRef':"J-1939-CLUSTER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_system_(self):
        return self._artop_system

    @property
    def system_(self):
        if self._artop_system is not None:
            if hasattr(self._artop_system, "uuid"):
                return self._artop_system.uuid
        return

    @property
    def ref_participatingJ1939Clusters_(self):
        return self._artop_participatingJ1939ClusterRef

    @property
    def participatingJ1939Clusters_(self):
        return self._artop_participatingJ1939ClusterRef

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
