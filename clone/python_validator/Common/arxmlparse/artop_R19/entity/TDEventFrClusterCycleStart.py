# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventFrClusterCycleStart.py
from .TDEventCycleStart import TDEventCycleStart

class TDEventFrClusterCycleStart(TDEventCycleStart):

    def __init__(self):
        super().__init__()
        from .FlexrayCluster import FlexrayCluster
        self._artop_frClusterRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_frClusterRef": "FLEXRAY-CLUSTER"})

    @property
    def ref_frCluster_(self):
        return self._artop_frClusterRef

    @property
    def frCluster_(self):
        if self._artop_frClusterRef is not None:
            if hasattr(self._artop_frClusterRef, "uuid"):
                return self._artop_frClusterRef.uuid
        return
