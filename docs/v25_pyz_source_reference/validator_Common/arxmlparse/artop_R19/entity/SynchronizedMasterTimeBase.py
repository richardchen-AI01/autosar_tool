# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SynchronizedMasterTimeBase.py
from .TimeBaseResource import TimeBaseResource

class SynchronizedMasterTimeBase(TimeBaseResource):

    def __init__(self):
        super().__init__()
        from .GlobalTimeMaster import GlobalTimeMaster
        from .TimeSyncCorrection import TimeSyncCorrection
        self._artop_networkTimeMasterRef = None
        self._artop_timeSyncCorrection = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkTimeMasterRef':"GLOBAL-TIME-MASTER", 
         '_artop_timeSyncCorrection':"TIME-SYNC-CORRECTION"})

    @property
    def ref_networkTimeMaster_(self):
        return self._artop_networkTimeMasterRef

    @property
    def networkTimeMaster_(self):
        if self._artop_networkTimeMasterRef is not None:
            if hasattr(self._artop_networkTimeMasterRef, "uuid"):
                return self._artop_networkTimeMasterRef.uuid
        return

    @property
    def ref_timeSyncCorrection_(self):
        return self._artop_timeSyncCorrection

    @property
    def timeSyncCorrection_(self):
        if self._artop_timeSyncCorrection is not None:
            if hasattr(self._artop_timeSyncCorrection, "uuid"):
                return self._artop_timeSyncCorrection.uuid
        return
