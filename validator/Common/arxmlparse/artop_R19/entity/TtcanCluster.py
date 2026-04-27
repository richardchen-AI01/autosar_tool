# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TtcanCluster.py
from .AbstractCanCluster import AbstractCanCluster

class TtcanCluster(AbstractCanCluster):

    def __init__(self):
        super().__init__()
        from .TtcanClusterConditional import TtcanClusterConditional
        self._artop_ttcanClusterVariant = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ttcanClusterVariant": "TTCAN-CLUSTER-CONDITIONAL"})

    @property
    def TtcanClusterVariants_TtcanClusterConditional(self):
        return self._artop_ttcanClusterVariant
