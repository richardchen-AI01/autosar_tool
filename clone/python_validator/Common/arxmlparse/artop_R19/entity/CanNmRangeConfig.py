# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanNmRangeConfig.py
from .ARObject import ARObject

class CanNmRangeConfig(ARObject):

    def __init__(self):
        super().__init__()
        from .CanNmNode import CanNmNode
        self._artop_lowerCanId = None
        self._artop_upperCanId = None
        self._artop_canNmNode = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_canNmNode": "CAN-NM-NODE"})

    @property
    def lowerCanId_(self):
        return self._artop_lowerCanId

    @property
    def upperCanId_(self):
        return self._artop_upperCanId

    @property
    def ref_canNmNode_(self):
        return self._artop_canNmNode

    @property
    def canNmNode_(self):
        if self._artop_canNmNode is not None:
            if hasattr(self._artop_canNmNode, "uuid"):
                return self._artop_canNmNode.uuid
        return
