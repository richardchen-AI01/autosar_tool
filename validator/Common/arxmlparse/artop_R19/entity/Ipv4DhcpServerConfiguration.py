# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Ipv4DhcpServerConfiguration.py
from .Describable import Describable

class Ipv4DhcpServerConfiguration(Describable):

    def __init__(self):
        super().__init__()
        from .DhcpServerConfiguration import DhcpServerConfiguration
        self._artop_addressRangeLowerBound = None
        self._artop_addressRangeUpperBound = None
        self._artop_defaultGateway = None
        self._artop_defaultLeaseTime = None
        self._artop_dnsServerAddress = None
        self._artop_networkMask = None
        self._artop_dhcpServerConfiguration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_dhcpServerConfiguration": "DHCP-SERVER-CONFIGURATION"})

    @property
    def addressRangeLowerBound_(self):
        return self._artop_addressRangeLowerBound

    @property
    def addressRangeUpperBound_(self):
        return self._artop_addressRangeUpperBound

    @property
    def defaultGateway_(self):
        return self._artop_defaultGateway

    @property
    def defaultLeaseTime_(self):
        return self._artop_defaultLeaseTime

    @property
    def dnsServerAddress_(self):
        return self._artop_dnsServerAddress

    @property
    def networkMask_(self):
        return self._artop_networkMask

    @property
    def ref_dhcpServerConfiguration_(self):
        return self._artop_dhcpServerConfiguration

    @property
    def dhcpServerConfiguration_(self):
        if self._artop_dhcpServerConfiguration is not None:
            if hasattr(self._artop_dhcpServerConfiguration, "uuid"):
                return self._artop_dhcpServerConfiguration.uuid
        return
