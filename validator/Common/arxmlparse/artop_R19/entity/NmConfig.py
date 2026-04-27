# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmConfig.py
from .FibexElement import FibexElement

class NmConfig(FibexElement):

    def __init__(self):
        super().__init__()
        from .NmCluster import NmCluster
        from .NmClusterCoupling import NmClusterCoupling
        from .NmEcu import NmEcu
        self._artop_nmCluster = []
        self._artop_nmClusterCoupling = []
        self._artop_nmIfEcu = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nmCluster':"NM-CLUSTER", 
         '_artop_nmClusterCoupling':"NM-CLUSTER-COUPLING", 
         '_artop_nmIfEcu':"NM-ECU"})

    @property
    def nmClusters_NmCluster(self):
        return self._artop_nmCluster

    @property
    def nmClusterCouplings_NmClusterCoupling(self):
        return self._artop_nmClusterCoupling

    @property
    def nmIfEcus_NmEcu(self):
        return self._artop_nmIfEcu
