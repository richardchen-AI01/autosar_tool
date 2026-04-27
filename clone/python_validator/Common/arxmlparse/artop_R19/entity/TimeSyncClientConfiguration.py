# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeSyncClientConfiguration.py
from .ARObject import ARObject

class TimeSyncClientConfiguration(ARObject):

    def __init__(self):
        super().__init__()
        from .TimeSynchronization import TimeSynchronization
        from .OrderedMaster import OrderedMaster
        self._artop_timeSyncTechnology = None
        self._artop_timeSynchronization = None
        self._artop_orderedMaster = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_timeSynchronization':"TIME-SYNCHRONIZATION", 
         '_artop_orderedMaster':"ORDERED-MASTER"})

    @property
    def timeSyncTechnology_(self):
        return self._artop_timeSyncTechnology

    @property
    def ref_timeSynchronization_(self):
        return self._artop_timeSynchronization

    @property
    def timeSynchronization_(self):
        if self._artop_timeSynchronization is not None:
            if hasattr(self._artop_timeSynchronization, "uuid"):
                return self._artop_timeSynchronization.uuid
        return

    @property
    def orderedMasters_OrderedMaster(self):
        return self._artop_orderedMaster
