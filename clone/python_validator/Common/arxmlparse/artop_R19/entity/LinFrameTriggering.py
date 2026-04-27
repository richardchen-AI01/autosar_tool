# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinFrameTriggering.py
from .FrameTriggering import FrameTriggering

class LinFrameTriggering(FrameTriggering):

    def __init__(self):
        super().__init__()
        self._artop_identifier = None
        self._artop_linChecksum = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def identifier_(self):
        if self._artop_identifier:
            return int(self._artop_identifier)
        return self._artop_identifier

    @property
    def linChecksum_(self):
        return self._artop_linChecksum
