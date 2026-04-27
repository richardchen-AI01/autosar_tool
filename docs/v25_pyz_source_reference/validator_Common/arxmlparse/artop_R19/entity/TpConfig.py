# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TpConfig.py
from .FibexElement import FibexElement

class TpConfig(FibexElement):

    def __init__(self):
        super().__init__()
        from .CommunicationCluster import CommunicationCluster
        self._artop_communicationClusterRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_communicationClusterRef": "COMMUNICATION-CLUSTER"})

    @property
    def ref_communicationCluster_(self):
        return self._artop_communicationClusterRef

    @property
    def communicationCluster_(self):
        if self._artop_communicationClusterRef is not None:
            if hasattr(self._artop_communicationClusterRef, "uuid"):
                return self._artop_communicationClusterRef.uuid
        return
