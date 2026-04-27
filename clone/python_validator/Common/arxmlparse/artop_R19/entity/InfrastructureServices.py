# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\InfrastructureServices.py
from .ARObject import ARObject

class InfrastructureServices(ARObject):

    def __init__(self):
        super().__init__()
        from .NetworkEndpoint import NetworkEndpoint
        from .DhcpServerConfiguration import DhcpServerConfiguration
        from .DoIpEntity import DoIpEntity
        from .TimeSynchronization import TimeSynchronization
        self._artop_networkEndpoint = None
        self._artop_dhcpServerConfiguration = None
        self._artop_doIpEntity = None
        self._artop_timeSynchronization = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_networkEndpoint': '"NETWORK-ENDPOINT"', 
         '_artop_dhcpServerConfiguration': '"DHCP-SERVER-CONFIGURATION"', 
         '_artop_doIpEntity': '"DO-IP-ENTITY"', 
         '_artop_timeSynchronization': '"TIME-SYNCHRONIZATION"'})

    @property
    def ref_networkEndpoint_(self):
        return self._artop_networkEndpoint

    @property
    def networkEndpoint_(self):
        if self._artop_networkEndpoint is not None:
            if hasattr(self._artop_networkEndpoint, "uuid"):
                return self._artop_networkEndpoint.uuid
        return

    @property
    def ref_dhcpServerConfiguration_(self):
        return self._artop_dhcpServerConfiguration

    @property
    def dhcpServerConfiguration_(self):
        if self._artop_dhcpServerConfiguration is not None:
            if hasattr(self._artop_dhcpServerConfiguration, "uuid"):
                return self._artop_dhcpServerConfiguration.uuid
        return

    @property
    def ref_doIpEntity_(self):
        return self._artop_doIpEntity

    @property
    def doIpEntity_(self):
        if self._artop_doIpEntity is not None:
            if hasattr(self._artop_doIpEntity, "uuid"):
                return self._artop_doIpEntity.uuid
        return

    @property
    def ref_timeSynchronization_(self):
        return self._artop_timeSynchronization

    @property
    def timeSynchronization_(self):
        if self._artop_timeSynchronization is not None:
            if hasattr(self._artop_timeSynchronization, "uuid"):
                return self._artop_timeSynchronization.uuid
        return
