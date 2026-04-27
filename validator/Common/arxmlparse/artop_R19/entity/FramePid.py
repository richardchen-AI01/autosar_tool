# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FramePid.py
from .ARObject import ARObject

class FramePid(ARObject):

    def __init__(self):
        super().__init__()
        from .AssignFrameIdRange import AssignFrameIdRange
        self._artop_index = None
        self._artop_pid = None
        self._artop_assignFrameIdRange = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_assignFrameIdRange": "ASSIGN-FRAME-ID-RANGE"})

    @property
    def index_(self):
        if self._artop_index:
            return int(self._artop_index)
        return self._artop_index

    @property
    def pid_(self):
        return self._artop_pid

    @property
    def ref_assignFrameIdRange_(self):
        return self._artop_assignFrameIdRange

    @property
    def assignFrameIdRange_(self):
        if self._artop_assignFrameIdRange is not None:
            if hasattr(self._artop_assignFrameIdRange, "uuid"):
                return self._artop_assignFrameIdRange.uuid
        return
