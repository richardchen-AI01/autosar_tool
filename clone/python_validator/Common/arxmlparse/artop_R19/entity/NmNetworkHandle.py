# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\NmNetworkHandle.py
from .Referrable import Referrable

class NmNetworkHandle(Referrable):

    def __init__(self):
        super().__init__()
        from .NmInstantiation import NmInstantiation
        from .PncMappingIdent import PncMappingIdent
        from .EthernetCommunicationConnector import EthernetCommunicationConnector
        self._artop_nmInstantiation = None
        self._artop_partialNetworkRef = []
        self._artop_vlanRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_nmInstantiation':"NM-INSTANTIATION", 
         '_artop_partialNetworkRef':"PNC-MAPPING-IDENT", 
         '_artop_vlanRef':"ETHERNET-COMMUNICATION-CONNECTOR"})

    @property
    def ref_nmInstantiation_(self):
        return self._artop_nmInstantiation

    @property
    def nmInstantiation_(self):
        if self._artop_nmInstantiation is not None:
            if hasattr(self._artop_nmInstantiation, "uuid"):
                return self._artop_nmInstantiation.uuid
        return

    @property
    def ref_partialNetworks_(self):
        return self._artop_partialNetworkRef

    @property
    def partialNetworks_(self):
        return self._artop_partialNetworkRef

    @property
    def ref_vlans_(self):
        return self._artop_vlanRef

    @property
    def vlans_(self):
        return self._artop_vlanRef
