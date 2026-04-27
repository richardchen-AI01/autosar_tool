# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\MacMulticastGroup.py
from .Identifiable import Identifiable

class MacMulticastGroup(Identifiable):

    def __init__(self):
        super().__init__()
        from .EthernetClusterContent import EthernetClusterContent
        self._artop_macMulticastAddress = None
        self._artop_ethernetClusterContent = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_ethernetClusterContent": "ETHERNET-CLUSTER-CONTENT"})

    @property
    def macMulticastAddress_(self):
        return self._artop_macMulticastAddress

    @property
    def ref_ethernetClusterContent_(self):
        return self._artop_ethernetClusterContent

    @property
    def ethernetClusterContent_(self):
        if self._artop_ethernetClusterContent is not None:
            if hasattr(self._artop_ethernetClusterContent, "uuid"):
                return self._artop_ethernetClusterContent.uuid
        return
