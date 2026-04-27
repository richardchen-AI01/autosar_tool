# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LogicalSupervision.py
from .PhmSupervision import PhmSupervision

class LogicalSupervision(PhmSupervision):

    def __init__(self):
        super().__init__()
        from .LocalSupervision import LocalSupervision
        from .SupervisionCheckpoint import SupervisionCheckpoint
        from .CheckpointTransition import CheckpointTransition
        self._artop_localSupervision = None
        self._artop_initialCheckpointRef = []
        self._artop_finalCheckpointRef = []
        self._artop_transitionRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_localSupervision': '"LOCAL-SUPERVISION"', 
         '_artop_initialCheckpointRef': '"SUPERVISION-CHECKPOINT"', 
         '_artop_finalCheckpointRef': '"SUPERVISION-CHECKPOINT"', 
         '_artop_transitionRef': '"CHECKPOINT-TRANSITION"'})

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
    def ref_initialCheckpoints_(self):
        return self._artop_initialCheckpointRef

    @property
    def initialCheckpoints_(self):
        return self._artop_initialCheckpointRef

    @property
    def ref_finalCheckpoints_(self):
        return self._artop_finalCheckpointRef

    @property
    def finalCheckpoints_(self):
        return self._artop_finalCheckpointRef

    @property
    def ref_transitions_(self):
        return self._artop_transitionRef

    @property
    def transitions_(self):
        return self._artop_transitionRef
