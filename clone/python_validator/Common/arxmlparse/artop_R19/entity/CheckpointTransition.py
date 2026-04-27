# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CheckpointTransition.py
from .Identifiable import Identifiable

class CheckpointTransition(Identifiable):

    def __init__(self):
        super().__init__()
        from .LocalSupervision import LocalSupervision
        from .SupervisionCheckpoint import SupervisionCheckpoint
        self._artop_localSupervision = None
        self._artop_sourceRef = None
        self._artop_targetRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_localSupervision':"LOCAL-SUPERVISION", 
         '_artop_sourceRef':"SUPERVISION-CHECKPOINT", 
         '_artop_targetRef':"SUPERVISION-CHECKPOINT"})

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
    def ref_source_(self):
        return self._artop_sourceRef

    @property
    def source_(self):
        if self._artop_sourceRef is not None:
            if hasattr(self._artop_sourceRef, "uuid"):
                return self._artop_sourceRef.uuid
        return

    @property
    def ref_target_(self):
        return self._artop_targetRef

    @property
    def target_(self):
        if self._artop_targetRef is not None:
            if hasattr(self._artop_targetRef, "uuid"):
                return self._artop_targetRef.uuid
        return
