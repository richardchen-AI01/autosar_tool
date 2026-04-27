# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimeBaseResource.py
from .Identifiable import Identifiable

class TimeBaseResource(Identifiable):

    def __init__(self):
        super().__init__()
        from .TimeSyncModuleInstantiation import TimeSyncModuleInstantiation
        self._artop_timeSyncModuleInstantiation = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_timeSyncModuleInstantiation": "TIME-SYNC-MODULE-INSTANTIATION"})

    @property
    def ref_timeSyncModuleInstantiation_(self):
        return self._artop_timeSyncModuleInstantiation

    @property
    def timeSyncModuleInstantiation_(self):
        if self._artop_timeSyncModuleInstantiation is not None:
            if hasattr(self._artop_timeSyncModuleInstantiation, "uuid"):
                return self._artop_timeSyncModuleInstantiation.uuid
        return
