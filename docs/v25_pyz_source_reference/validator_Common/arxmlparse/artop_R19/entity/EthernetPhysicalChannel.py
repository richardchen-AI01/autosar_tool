# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetPhysicalChannel.py
from .PhysicalChannel import PhysicalChannel

class EthernetPhysicalChannel(PhysicalChannel):

    def __init__(self):
        super().__init__()
        from .NetworkEndpoint import NetworkEndpoint
        from .SoAdConfig import SoAdConfig
        from .VlanConfig import VlanConfig
        self._artop_networkEndpoint = []
        self._artop_soAdConfig = None
        self._artop_vlan = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkEndpoint':"NETWORK-ENDPOINT", 
         '_artop_soAdConfig':"SO-AD-CONFIG", 
         '_artop_vlan':"VLAN-CONFIG"})

    @property
    def networkEndpoints_NetworkEndpoint(self):
        return self._artop_networkEndpoint

    @property
    def ref_soAdConfig_(self):
        return self._artop_soAdConfig

    @property
    def soAdConfig_(self):
        if self._artop_soAdConfig is not None:
            if hasattr(self._artop_soAdConfig, "uuid"):
                return self._artop_soAdConfig.uuid
        return

    @property
    def ref_vlan_(self):
        return self._artop_vlan

    @property
    def vlan_(self):
        if self._artop_vlan is not None:
            if hasattr(self._artop_vlan, "uuid"):
                return self._artop_vlan.uuid
        return
