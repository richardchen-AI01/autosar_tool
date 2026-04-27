# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AbstractCanClusterContent.py
from .CommunicationClusterContent import CommunicationClusterContent

class AbstractCanClusterContent(CommunicationClusterContent):

    def __init__(self):
        super().__init__()
        from .CanClusterBusOffRecovery import CanClusterBusOffRecovery
        self._artop_canFdBaudrate = None
        self._artop_busOffRecovery = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_busOffRecovery": "CAN-CLUSTER-BUS-OFF-RECOVERY"})

    @property
    def canFdBaudrate_(self):
        return self._artop_canFdBaudrate

    @property
    def ref_busOffRecovery_(self):
        return self._artop_busOffRecovery

    @property
    def busOffRecovery_(self):
        if self._artop_busOffRecovery is not None:
            if hasattr(self._artop_busOffRecovery, "uuid"):
                return self._artop_busOffRecovery.uuid
        return
