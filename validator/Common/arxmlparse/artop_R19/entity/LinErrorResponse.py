# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinErrorResponse.py
from .ARObject import ARObject

class LinErrorResponse(ARObject):

    def __init__(self):
        super().__init__()
        from .LinFrameTriggering import LinFrameTriggering
        from .ISignalTriggering import ISignalTriggering
        self._artop_responseErrorPosition = None
        self._artop_frameTriggeringRef = None
        self._artop_responseErrorRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_frameTriggeringRef':"LIN-FRAME-TRIGGERING", 
         '_artop_responseErrorRef':"I-SIGNAL-TRIGGERING"})

    @property
    def responseErrorPosition_(self):
        if self._artop_responseErrorPosition:
            return int(self._artop_responseErrorPosition)
        return self._artop_responseErrorPosition

    @property
    def ref_frameTriggering_(self):
        return self._artop_frameTriggeringRef

    @property
    def frameTriggering_(self):
        if self._artop_frameTriggeringRef is not None:
            if hasattr(self._artop_frameTriggeringRef, "uuid"):
                return self._artop_frameTriggeringRef.uuid
        return

    @property
    def ref_responseError_(self):
        return self._artop_responseErrorRef

    @property
    def responseError_(self):
        if self._artop_responseErrorRef is not None:
            if hasattr(self._artop_responseErrorRef, "uuid"):
                return self._artop_responseErrorRef.uuid
        return
