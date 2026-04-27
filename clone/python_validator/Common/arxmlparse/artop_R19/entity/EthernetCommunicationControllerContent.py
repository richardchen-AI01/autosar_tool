# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EthernetCommunicationControllerContent.py
from .CommunicationControllerContent import CommunicationControllerContent

class EthernetCommunicationControllerContent(CommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .CouplingPort import CouplingPort
        self._artop_macLayerType = None
        self._artop_macUnicastAddress = None
        self._artop_maximumReceiveBufferLength = None
        self._artop_maximumTransmissionUnit = None
        self._artop_maximumTransmitBufferLength = None
        self._artop_couplingPort = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_couplingPort": "COUPLING-PORT"})

    @property
    def macLayerType_(self):
        return self._artop_macLayerType

    @property
    def macUnicastAddress_(self):
        return self._artop_macUnicastAddress

    @property
    def maximumReceiveBufferLength_(self):
        if self._artop_maximumReceiveBufferLength:
            return int(self._artop_maximumReceiveBufferLength)
        return self._artop_maximumReceiveBufferLength

    @property
    def maximumTransmissionUnit_(self):
        return self._artop_maximumTransmissionUnit

    @property
    def maximumTransmitBufferLength_(self):
        if self._artop_maximumTransmitBufferLength:
            return int(self._artop_maximumTransmitBufferLength)
        return self._artop_maximumTransmitBufferLength

    @property
    def couplingPorts_CouplingPort(self):
        return self._artop_couplingPort
