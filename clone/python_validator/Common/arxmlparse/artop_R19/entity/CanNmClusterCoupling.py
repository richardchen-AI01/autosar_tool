# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanNmClusterCoupling.py
from .NmClusterCoupling import NmClusterCoupling

class CanNmClusterCoupling(NmClusterCoupling):

    def __init__(self):
        super().__init__()
        from .CanNmCluster import CanNmCluster
        self._artop_nmBusloadReductionEnabled = None
        self._artop_nmImmediateRestartEnabled = None
        self._artop_coupledClusterRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_coupledClusterRef": "CAN-NM-CLUSTER"})

    @property
    def nmBusloadReductionEnabled_(self):
        if self._artop_nmBusloadReductionEnabled:
            if self._artop_nmBusloadReductionEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmBusloadReductionEnabled

    @property
    def nmImmediateRestartEnabled_(self):
        if self._artop_nmImmediateRestartEnabled:
            if self._artop_nmImmediateRestartEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmImmediateRestartEnabled

    @property
    def ref_coupledClusters_(self):
        return self._artop_coupledClusterRef

    @property
    def coupledClusters_(self):
        return self._artop_coupledClusterRef
