# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DhcpServerConfiguration.py
from .ARObject import ARObject

class DhcpServerConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .Ipv4DhcpServerConfiguration import Ipv4DhcpServerConfiguration
        from .Ipv6DhcpServerConfiguration import Ipv6DhcpServerConfiguration
        self._artop_ipv4DhcpServerConfiguration = None
        self._artop_ipv6DhcpServerConfiguration = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ipv4DhcpServerConfiguration':"IPV-4-DHCP-SERVER-CONFIGURATION", 
         '_artop_ipv6DhcpServerConfiguration':"IPV-6-DHCP-SERVER-CONFIGURATION"})

    @property
    def ref_ipv4DhcpServerConfiguration_(self):
        return self._artop_ipv4DhcpServerConfiguration

    @property
    def ipv4DhcpServerConfiguration_(self):
        if self._artop_ipv4DhcpServerConfiguration is not None:
            if hasattr(self._artop_ipv4DhcpServerConfiguration, "uuid"):
                return self._artop_ipv4DhcpServerConfiguration.uuid
        return

    @property
    def ref_ipv6DhcpServerConfiguration_(self):
        return self._artop_ipv6DhcpServerConfiguration

    @property
    def ipv6DhcpServerConfiguration_(self):
        if self._artop_ipv6DhcpServerConfiguration is not None:
            if hasattr(self._artop_ipv6DhcpServerConfiguration, "uuid"):
                return self._artop_ipv6DhcpServerConfiguration.uuid
        return
