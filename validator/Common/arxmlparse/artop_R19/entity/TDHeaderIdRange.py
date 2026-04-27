# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDHeaderIdRange.py
from .ARObject import ARObject

class TDHeaderIdRange(ARObject):

    def __init__(self):
        super().__init__()
        from .TDEventFrameEthernet import TDEventFrameEthernet
        self._artop_maxHeaderId = None
        self._artop_minHeaderId = None
        self._artop_tdEventFrameEthernet = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_tdEventFrameEthernet": "TD-EVENT-FRAME-ETHERNET"})

    @property
    def maxHeaderId_(self):
        if self._artop_maxHeaderId:
            return int(self._artop_maxHeaderId)
        return self._artop_maxHeaderId

    @property
    def minHeaderId_(self):
        if self._artop_minHeaderId:
            return int(self._artop_minHeaderId)
        return self._artop_minHeaderId

    @property
    def ref_tDEventFrameEthernet_(self):
        return self._artop_tdEventFrameEthernet

    @property
    def tDEventFrameEthernet_(self):
        if self._artop_tdEventFrameEthernet is not None:
            if hasattr(self._artop_tdEventFrameEthernet, "uuid"):
                return self._artop_tdEventFrameEthernet.uuid
        return
