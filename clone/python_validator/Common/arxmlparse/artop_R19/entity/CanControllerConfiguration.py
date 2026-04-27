# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CanControllerConfiguration.py
from .AbstractCanCommunicationControllerAttributes import AbstractCanCommunicationControllerAttributes

class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):

    def __init__(self):
        super().__init__()
        self._artop_propSeg = None
        self._artop_syncJumpWidth = None
        self._artop_timeSeg1 = None
        self._artop_timeSeg2 = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def propSeg_(self):
        if self._artop_propSeg:
            return int(self._artop_propSeg)
        return self._artop_propSeg

    @property
    def syncJumpWidth_(self):
        if self._artop_syncJumpWidth:
            return int(self._artop_syncJumpWidth)
        return self._artop_syncJumpWidth

    @property
    def timeSeg1_(self):
        if self._artop_timeSeg1:
            return int(self._artop_timeSeg1)
        return self._artop_timeSeg1

    @property
    def timeSeg2_(self):
        if self._artop_timeSeg2:
            return int(self._artop_timeSeg2)
        return self._artop_timeSeg2
