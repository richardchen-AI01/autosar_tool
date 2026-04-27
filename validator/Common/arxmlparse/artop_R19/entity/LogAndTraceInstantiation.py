# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\LogAndTraceInstantiation.py
from .NonOsModuleInstantiation import NonOsModuleInstantiation

class LogAndTraceInstantiation(NonOsModuleInstantiation):

    def __init__(self):
        super().__init__()
        from .NetworkConfiguration import NetworkConfiguration
        from .TimeBaseResource import TimeBaseResource
        self._artop_networkConfiguration = []
        self._artop_timeBaseResourceRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_networkConfiguration':"NETWORK-CONFIGURATION", 
         '_artop_timeBaseResourceRef':"TIME-BASE-RESOURCE"})

    @property
    def networkConfigurations_NetworkConfiguration(self):
        return self._artop_networkConfiguration

    @property
    def ref_timeBaseResource_(self):
        return self._artop_timeBaseResourceRef

    @property
    def timeBaseResource_(self):
        if self._artop_timeBaseResourceRef is not None:
            if hasattr(self._artop_timeBaseResourceRef, "uuid"):
                return self._artop_timeBaseResourceRef.uuid
        return
