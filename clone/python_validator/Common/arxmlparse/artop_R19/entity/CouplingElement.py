# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CouplingElement.py
from .FibexElement import FibexElement

class CouplingElement(FibexElement):

    def __init__(self):
        super().__init__()
        from .EthernetCluster import EthernetCluster
        from .CouplingPort import CouplingPort
        from .EcuInstance import EcuInstance
        self._artop_couplingType = None
        self._artop_communicationClusterRef = None
        self._artop_couplingPort = []
        self._artop_ecuInstanceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_communicationClusterRef':"ETHERNET-CLUSTER", 
         '_artop_couplingPort':"COUPLING-PORT", 
         '_artop_ecuInstanceRef':"ECU-INSTANCE"})

    @property
    def couplingType_(self):
        return self._artop_couplingType

    @property
    def ref_communicationCluster_(self):
        return self._artop_communicationClusterRef

    @property
    def communicationCluster_(self):
        if self._artop_communicationClusterRef is not None:
            if hasattr(self._artop_communicationClusterRef, "uuid"):
                return self._artop_communicationClusterRef.uuid
        return

    @property
    def couplingPorts_CouplingPort(self):
        return self._artop_couplingPort

    @property
    def ref_ecuInstance_(self):
        return self._artop_ecuInstanceRef

    @property
    def ecuInstance_(self):
        if self._artop_ecuInstanceRef is not None:
            if hasattr(self._artop_ecuInstanceRef, "uuid"):
                return self._artop_ecuInstanceRef.uuid
        return
