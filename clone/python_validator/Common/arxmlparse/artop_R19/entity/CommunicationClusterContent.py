# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CommunicationClusterContent.py
from .ARObject import ARObject

class CommunicationClusterContent(ARObject):

    def __init__(self):
        super().__init__()
        from .PhysicalChannel import PhysicalChannel
        self._artop_baudrate = None
        self._artop_protocolName = None
        self._artop_protocolVersion = None
        self._artop_speed = None
        self._artop_physicalChannel = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_physicalChannel": "PHYSICAL-CHANNEL"})

    @property
    def baudrate_(self):
        return self._artop_baudrate

    @property
    def protocolName_(self):
        return self._artop_protocolName

    @property
    def protocolVersion_(self):
        return self._artop_protocolVersion

    @property
    def speed_(self):
        if self._artop_speed:
            return int(self._artop_speed)
        return self._artop_speed

    @property
    def physicalChannels_PhysicalChannel(self):
        return self._artop_physicalChannel
