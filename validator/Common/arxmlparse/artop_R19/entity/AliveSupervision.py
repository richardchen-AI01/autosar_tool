# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AliveSupervision.py
from .PhmSupervision import PhmSupervision

class AliveSupervision(PhmSupervision):

    def __init__(self):
        super().__init__()
        from .LocalSupervision import LocalSupervision
        from .SupervisionCheckpoint import SupervisionCheckpoint
        self._artop_aliveReferenceCycle = None
        self._artop_expectedAliveIndications = None
        self._artop_maxMargin = None
        self._artop_minMargin = None
        self._artop_localSupervision = None
        self._artop_checkpointRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_localSupervision':"LOCAL-SUPERVISION", 
         '_artop_checkpointRef':"SUPERVISION-CHECKPOINT"})

    @property
    def aliveReferenceCycle_(self):
        return self._artop_aliveReferenceCycle

    @property
    def expectedAliveIndications_(self):
        return self._artop_expectedAliveIndications

    @property
    def maxMargin_(self):
        return self._artop_maxMargin

    @property
    def minMargin_(self):
        return self._artop_minMargin

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
    def ref_checkpoint_(self):
        return self._artop_checkpointRef

    @property
    def checkpoint_(self):
        if self._artop_checkpointRef is not None:
            if hasattr(self._artop_checkpointRef, "uuid"):
                return self._artop_checkpointRef.uuid
        return
