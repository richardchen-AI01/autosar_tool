# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\VlanConfig.py
from .Identifiable import Identifiable

class VlanConfig(Identifiable):

    def __init__(self):
        super().__init__()
        from .EthernetPhysicalChannel import EthernetPhysicalChannel
        self._artop_vlanIdentifier = None
        self._artop_ethernetPhysicalChannel = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ethernetPhysicalChannel": "ETHERNET-PHYSICAL-CHANNEL"})

    @property
    def vlanIdentifier_(self):
        return self._artop_vlanIdentifier

    @property
    def ref_ethernetPhysicalChannel_(self):
        return self._artop_ethernetPhysicalChannel

    @property
    def ethernetPhysicalChannel_(self):
        if self._artop_ethernetPhysicalChannel is not None:
            if hasattr(self._artop_ethernetPhysicalChannel, "uuid"):
                return self._artop_ethernetPhysicalChannel.uuid
        return
