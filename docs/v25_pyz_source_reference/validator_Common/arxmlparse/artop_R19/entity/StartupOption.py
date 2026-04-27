# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\StartupOption.py
from .ARObject import ARObject

class StartupOption(ARObject):

    def __init__(self):
        super().__init__()
        from .StartupConfig import StartupConfig
        self._artop_optionArgument = None
        self._artop_optionKind = None
        self._artop_optionName = None
        self._artop_startupConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_startupConfig": "STARTUP-CONFIG"})

    @property
    def optionArgument_(self):
        return self._artop_optionArgument

    @property
    def optionKind_(self):
        return self._artop_optionKind

    @property
    def optionName_(self):
        return self._artop_optionName

    @property
    def ref_startupConfig_(self):
        return self._artop_startupConfig

    @property
    def startupConfig_(self):
        if self._artop_startupConfig is not None:
            if hasattr(self._artop_startupConfig, "uuid"):
                return self._artop_startupConfig.uuid
        return
