# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BusMirrorChannel.py
from .ARObject import ARObject

class BusMirrorChannel(ARObject):

    def __init__(self):
        super().__init__()
        from .PhysicalChannelRefConditional import PhysicalChannelRefConditional
        self._artop_busMirrorNetworkId = None
        self._artop_channel = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_channel": "PHYSICAL-CHANNEL-REF-CONDITIONAL"})

    @property
    def busMirrorNetworkId_(self):
        return self._artop_busMirrorNetworkId

    @property
    def channels_PhysicalChannelRefConditional(self):
        return self._artop_channel
