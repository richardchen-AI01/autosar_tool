# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SoConIPduIdentifier.py
from .Referrable import Referrable

class SoConIPduIdentifier(Referrable):

    def __init__(self):
        super().__init__()
        from .SocketConnectionIpduIdentifierSet import SocketConnectionIpduIdentifierSet
        from .PduTriggering import PduTriggering
        self._artop_headerId = None
        self._artop_pduCollectionPduTimeout = None
        self._artop_pduCollectionSemantics = None
        self._artop_pduCollectionTrigger = None
        self._artop_socketConnectionIpduIdentifierSet = None
        self._artop_pduTriggeringRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_socketConnectionIpduIdentifierSet':"SOCKET-CONNECTION-IPDU-IDENTIFIER-SET", 
         '_artop_pduTriggeringRef':"PDU-TRIGGERING"})

    @property
    def headerId_(self):
        return self._artop_headerId

    @property
    def pduCollectionPduTimeout_(self):
        return self._artop_pduCollectionPduTimeout

    @property
    def pduCollectionSemantics_(self):
        return self._artop_pduCollectionSemantics

    @property
    def pduCollectionTrigger_(self):
        return self._artop_pduCollectionTrigger

    @property
    def ref_socketConnectionIpduIdentifierSet_(self):
        return self._artop_socketConnectionIpduIdentifierSet

    @property
    def socketConnectionIpduIdentifierSet_(self):
        if self._artop_socketConnectionIpduIdentifierSet is not None:
            if hasattr(self._artop_socketConnectionIpduIdentifierSet, "uuid"):
                return self._artop_socketConnectionIpduIdentifierSet.uuid
        return

    @property
    def ref_pduTriggering_(self):
        return self._artop_pduTriggeringRef

    @property
    def pduTriggering_(self):
        if self._artop_pduTriggeringRef is not None:
            if hasattr(self._artop_pduTriggeringRef, "uuid"):
                return self._artop_pduTriggeringRef.uuid
        return
