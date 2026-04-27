# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\OrderedMaster.py
from .ARObject import ARObject

class OrderedMaster(ARObject):

    def __init__(self):
        super().__init__()
        from .TimeSyncClientConfiguration import TimeSyncClientConfiguration
        from .TimeSyncServerConfiguration import TimeSyncServerConfiguration
        self._artop_index = None
        self._artop_timeSyncClientConfiguration = None
        self._artop_timeSyncServerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_timeSyncClientConfiguration':"TIME-SYNC-CLIENT-CONFIGURATION", 
         '_artop_timeSyncServerRef':"TIME-SYNC-SERVER-CONFIGURATION"})

    @property
    def index_(self):
        return self._artop_index

    @property
    def ref_timeSyncClientConfiguration_(self):
        return self._artop_timeSyncClientConfiguration

    @property
    def timeSyncClientConfiguration_(self):
        if self._artop_timeSyncClientConfiguration is not None:
            if hasattr(self._artop_timeSyncClientConfiguration, "uuid"):
                return self._artop_timeSyncClientConfiguration.uuid
        return

    @property
    def ref_timeSyncServer_(self):
        return self._artop_timeSyncServerRef

    @property
    def timeSyncServer_(self):
        if self._artop_timeSyncServerRef is not None:
            if hasattr(self._artop_timeSyncServerRef, "uuid"):
                return self._artop_timeSyncServerRef.uuid
        return
