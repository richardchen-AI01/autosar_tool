# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetClusterContent.py
from .CommunicationClusterContent import CommunicationClusterContent

class EthernetClusterContent(CommunicationClusterContent):

    def __init__(self):
        super().__init__()
        from .CouplingPortConnection import CouplingPortConnection
        from .MacMulticastGroup import MacMulticastGroup
        self._artop_couplingPortSwitchoffDelay = None
        self._artop_couplingPortConnection = []
        self._artop_macMulticastGroup = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_couplingPortConnection':"COUPLING-PORT-CONNECTION", 
         '_artop_macMulticastGroup':"MAC-MULTICAST-GROUP"})

    @property
    def couplingPortSwitchoffDelay_(self):
        return self._artop_couplingPortSwitchoffDelay

    @property
    def couplingPortConnections_CouplingPortConnection(self):
        return self._artop_couplingPortConnection

    @property
    def macMulticastGroups_MacMulticastGroup(self):
        return self._artop_macMulticastGroup
