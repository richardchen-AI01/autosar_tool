# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AssignFrameIdRange.py
from .LinConfigurationEntry import LinConfigurationEntry

class AssignFrameIdRange(LinConfigurationEntry):

    def __init__(self):
        super().__init__()
        from .FramePid import FramePid
        self._artop_startIndex = None
        self._artop_framePid = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_framePid": "FRAME-PID"})

    @property
    def startIndex_(self):
        if self._artop_startIndex:
            return int(self._artop_startIndex)
        return self._artop_startIndex

    @property
    def framePids_FramePid(self):
        return self._artop_framePid
