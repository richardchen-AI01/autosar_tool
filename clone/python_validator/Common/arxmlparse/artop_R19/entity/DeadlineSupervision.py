# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DeadlineSupervision.py
from .PhmSupervision import PhmSupervision

class DeadlineSupervision(PhmSupervision):

    def __init__(self):
        super().__init__()
        from .LocalSupervision import LocalSupervision
        from .CheckpointTransition import CheckpointTransition
        self._artop_maxDeadline = None
        self._artop_minDeadline = None
        self._artop_localSupervision = None
        self._artop_checkpointTransitionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_localSupervision':"LOCAL-SUPERVISION", 
         '_artop_checkpointTransitionRef':"CHECKPOINT-TRANSITION"})

    @property
    def maxDeadline_(self):
        return self._artop_maxDeadline

    @property
    def minDeadline_(self):
        return self._artop_minDeadline

    @property
    def ref_localSupervision_(self):
        return self._artop_localSupervision

    @property
    def localSupervision_(self):
        if self._artop_localSupervision is not None:
            if hasattr(self._artop_localSupervision, "uuid"):
                return self._artop_localSupervision.uuid
        return

    @property
    def ref_checkpointTransition_(self):
        return self._artop_checkpointTransitionRef

    @property
    def checkpointTransition_(self):
        if self._artop_checkpointTransitionRef is not None:
            if hasattr(self._artop_checkpointTransitionRef, "uuid"):
                return self._artop_checkpointTransitionRef.uuid
        return
