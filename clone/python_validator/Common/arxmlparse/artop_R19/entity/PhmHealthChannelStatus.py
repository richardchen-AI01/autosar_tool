# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PhmHealthChannelStatus.py
from .AtpFeature import AtpFeature

class PhmHealthChannelStatus(AtpFeature):

    def __init__(self):
        super().__init__()
        from .PhmHealthChannelInterface import PhmHealthChannelInterface
        self._artop_statusId = None
        self._artop_phmHealthChannelInterface = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_phmHealthChannelInterface": "PHM-HEALTH-CHANNEL-INTERFACE"})

    @property
    def statusId_(self):
        return self._artop_statusId

    @property
    def ref_phmHealthChannelInterface_(self):
        return self._artop_phmHealthChannelInterface

    @property
    def phmHealthChannelInterface_(self):
        if self._artop_phmHealthChannelInterface is not None:
            if hasattr(self._artop_phmHealthChannelInterface, "uuid"):
                return self._artop_phmHealthChannelInterface.uuid
        return
