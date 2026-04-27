# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeSynchronization.py
from .ARObject import ARObject

class TimeSynchronization(ARObject):

    def __init__(self):
        super().__init__()
        from .InfrastructureServices import InfrastructureServices
        from .TimeSyncClientConfiguration import TimeSyncClientConfiguration
        from .TimeSyncServerConfiguration import TimeSyncServerConfiguration
        self._artop_infrastructureServices = None
        self._artop_timeSyncClient = None
        self._artop_timeSyncServer = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_infrastructureServices':"INFRASTRUCTURE-SERVICES", 
         '_artop_timeSyncClient':"TIME-SYNC-CLIENT-CONFIGURATION", 
         '_artop_timeSyncServer':"TIME-SYNC-SERVER-CONFIGURATION"})

    @property
    def ref_infrastructureServices_(self):
        return self._artop_infrastructureServices

    @property
    def infrastructureServices_(self):
        if self._artop_infrastructureServices is not None:
            if hasattr(self._artop_infrastructureServices, "uuid"):
                return self._artop_infrastructureServices.uuid
        return

    @property
    def ref_timeSyncClient_(self):
        return self._artop_timeSyncClient

    @property
    def timeSyncClient_(self):
        if self._artop_timeSyncClient is not None:
            if hasattr(self._artop_timeSyncClient, "uuid"):
                return self._artop_timeSyncClient.uuid
        return

    @property
    def ref_timeSyncServer_(self):
        return self._artop_timeSyncServer

    @property
    def timeSyncServer_(self):
        if self._artop_timeSyncServer is not None:
            if hasattr(self._artop_timeSyncServer, "uuid"):
                return self._artop_timeSyncServer.uuid
        return
