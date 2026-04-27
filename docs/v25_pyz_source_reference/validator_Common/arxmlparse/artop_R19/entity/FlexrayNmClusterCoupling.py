# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlexrayNmClusterCoupling.py
from .NmClusterCoupling import NmClusterCoupling

class FlexrayNmClusterCoupling(NmClusterCoupling):

    def __init__(self):
        super().__init__()
        from .FlexrayNmCluster import FlexrayNmCluster
        self._artop_nmControlBitVectorEnabled = None
        self._artop_nmDataDisabled = None
        self._artop_nmScheduleVariant = None
        self._artop_coupledClusterRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_coupledClusterRef": "FLEXRAY-NM-CLUSTER"})

    @property
    def nmControlBitVectorEnabled_(self):
        if self._artop_nmControlBitVectorEnabled:
            if self._artop_nmControlBitVectorEnabled == "true":
                return True
            return False
        else:
            return self._artop_nmControlBitVectorEnabled

    @property
    def nmDataDisabled_(self):
        if self._artop_nmDataDisabled:
            if self._artop_nmDataDisabled == "true":
                return True
            return False
        else:
            return self._artop_nmDataDisabled

    @property
    def nmScheduleVariant_(self):
        return self._artop_nmScheduleVariant

    @property
    def ref_coupledClusters_(self):
        return self._artop_coupledClusterRef

    @property
    def coupledClusters_(self):
        return self._artop_coupledClusterRef
