# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LinEventTriggeredFrame.py
from .LinFrame import LinFrame

class LinEventTriggeredFrame(LinFrame):

    def __init__(self):
        super().__init__()
        from .LinScheduleTable import LinScheduleTable
        from .LinUnconditionalFrame import LinUnconditionalFrame
        self._artop_collisionResolvingScheduleRef = None
        self._artop_linUnconditionalFrameRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_collisionResolvingScheduleRef':"LIN-SCHEDULE-TABLE", 
         '_artop_linUnconditionalFrameRef':"LIN-UNCONDITIONAL-FRAME"})

    @property
    def ref_collisionResolvingSchedule_(self):
        return self._artop_collisionResolvingScheduleRef

    @property
    def collisionResolvingSchedule_(self):
        if self._artop_collisionResolvingScheduleRef is not None:
            if hasattr(self._artop_collisionResolvingScheduleRef, "uuid"):
                return self._artop_collisionResolvingScheduleRef.uuid
        return

    @property
    def ref_linUnconditionalFrames_(self):
        return self._artop_linUnconditionalFrameRef

    @property
    def linUnconditionalFrames_(self):
        return self._artop_linUnconditionalFrameRef
