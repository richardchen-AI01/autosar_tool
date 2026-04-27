# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\StartupConfig.py
from .Identifiable import Identifiable

class StartupConfig(Identifiable):

    def __init__(self):
        super().__init__()
        from .StartupConfigSet import StartupConfigSet
        from .TagWithOptionalValue import TagWithOptionalValue
        from .StartupOption import StartupOption
        from .EnterExitTimeout import EnterExitTimeout
        self._artop_schedulingPolicy = None
        self._artop_schedulingPriority = None
        self._artop_startupConfigSet = None
        self._artop_environmentVariable = []
        self._artop_startupOption = []
        self._artop_timeout = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_startupConfigSet': '"STARTUP-CONFIG-SET"', 
         '_artop_environmentVariable': '"TAG-WITH-OPTIONAL-VALUE"', 
         '_artop_startupOption': '"STARTUP-OPTION"', 
         '_artop_timeout': '"ENTER-EXIT-TIMEOUT"'})

    @property
    def schedulingPolicy_(self):
        return self._artop_schedulingPolicy

    @property
    def schedulingPriority_(self):
        if self._artop_schedulingPriority:
            return int(self._artop_schedulingPriority)
        return self._artop_schedulingPriority

    @property
    def ref_startupConfigSet_(self):
        return self._artop_startupConfigSet

    @property
    def startupConfigSet_(self):
        if self._artop_startupConfigSet is not None:
            if hasattr(self._artop_startupConfigSet, "uuid"):
                return self._artop_startupConfigSet.uuid
        return

    @property
    def environmentVariables_TagWithOptionalValue(self):
        return self._artop_environmentVariable

    @property
    def startupOptions_StartupOption(self):
        return self._artop_startupOption

    @property
    def ref_timeout_(self):
        return self._artop_timeout

    @property
    def timeout_(self):
        if self._artop_timeout is not None:
            if hasattr(self._artop_timeout, "uuid"):
                return self._artop_timeout.uuid
        return
