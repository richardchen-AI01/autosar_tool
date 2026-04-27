# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\J1939Cluster.py
from .AbstractCanCluster import AbstractCanCluster

class J1939Cluster(AbstractCanCluster):

    def __init__(self):
        super().__init__()
        from .J1939ClusterConditional import J1939ClusterConditional
        self._artop_j1939ClusterVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_j1939ClusterVariant": "J-1939-CLUSTER-CONDITIONAL"})

    @property
    def J1939ClusterVariants_J1939ClusterConditional(self):
        return self._artop_j1939ClusterVariant
