# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UdpNmNode.py
from .NmNode import NmNode

class UdpNmNode(NmNode):

    def __init__(self):
        super().__init__()
        from .EthernetCommunicationConnector import EthernetCommunicationConnector
        self._artop_allNmMessagesKeepAwake = None
        self._artop_nmMsgCycleOffset = None
        self._artop_communicationConnectorRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_communicationConnectorRef": "ETHERNET-COMMUNICATION-CONNECTOR"})

    @property
    def allNmMessagesKeepAwake_(self):
        if self._artop_allNmMessagesKeepAwake:
            if self._artop_allNmMessagesKeepAwake == "true":
                return True
            return False
        else:
            return self._artop_allNmMessagesKeepAwake

    @property
    def nmMsgCycleOffset_(self):
        return self._artop_nmMsgCycleOffset

    @property
    def ref_communicationConnector_(self):
        return self._artop_communicationConnectorRef

    @property
    def communicationConnector_(self):
        if self._artop_communicationConnectorRef is not None:
            if hasattr(self._artop_communicationConnectorRef, "uuid"):
                return self._artop_communicationConnectorRef.uuid
        return
