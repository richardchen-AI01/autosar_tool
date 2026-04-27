# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VlanMembership.py
from .ARObject import ARObject

class VlanMembership(ARObject):

    def __init__(self):
        super().__init__()
        from .CouplingPort import CouplingPort
        from .DhcpServerConfiguration import DhcpServerConfiguration
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        self._artop_defaultPriority = None
        self._artop_sendActivity = None
        self._artop_couplingPort = None
        self._artop_dhcpAddressAssignment = None
        self._artop_vlanRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_couplingPort':"COUPLING-PORT", 
         '_artop_dhcpAddressAssignment':"DHCP-SERVER-CONFIGURATION", 
         '_artop_vlanRef':"ETHERNET-PHYSICAL-CHANNEL"})

    @property
    def defaultPriority_(self):
        return self._artop_defaultPriority

    @property
    def sendActivity_(self):
        return self._artop_sendActivity

    @property
    def ref_couplingPort_(self):
        return self._artop_couplingPort

    @property
    def couplingPort_(self):
        if self._artop_couplingPort is not None:
            if hasattr(self._artop_couplingPort, "uuid"):
                return self._artop_couplingPort.uuid
        return

    @property
    def ref_dhcpAddressAssignment_(self):
        return self._artop_dhcpAddressAssignment

    @property
    def dhcpAddressAssignment_(self):
        if self._artop_dhcpAddressAssignment is not None:
            if hasattr(self._artop_dhcpAddressAssignment, "uuid"):
                return self._artop_dhcpAddressAssignment.uuid
        return

    @property
    def ref_vlan_(self):
        return self._artop_vlanRef

    @property
    def vlan_(self):
        if self._artop_vlanRef is not None:
            if hasattr(self._artop_vlanRef, "uuid"):
                return self._artop_vlanRef.uuid
        return
