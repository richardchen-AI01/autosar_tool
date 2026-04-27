# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Frame.py
from .FibexElement import FibexElement

class Frame(FibexElement):

    def __init__(self):
        super().__init__()
        from .PduToFrameMapping import PduToFrameMapping
        self._artop_frameLength = None
        self._artop_pduToFrameMapping = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_pduToFrameMapping": "PDU-TO-FRAME-MAPPING"})

    @property
    def frameLength_(self):
        if self._artop_frameLength:
            return int(self._artop_frameLength)
        return self._artop_frameLength

    @property
    def pduToFrameMappings_PduToFrameMapping(self):
        return self._artop_pduToFrameMapping
