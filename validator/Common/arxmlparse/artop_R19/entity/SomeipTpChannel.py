# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipTpChannel.py
from .Identifiable import Identifiable

class SomeipTpChannel(Identifiable):

    def __init__(self):
        super().__init__()
        from .SomeipTpConfig import SomeipTpConfig
        self._artop_rxTimeoutTime = None
        self._artop_separationTime = None
        self._artop_someipTpConfig = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_someipTpConfig": "SOMEIP-TP-CONFIG"})

    @property
    def rxTimeoutTime_(self):
        return self._artop_rxTimeoutTime

    @property
    def separationTime_(self):
        return self._artop_separationTime

    @property
    def ref_someipTpConfig_(self):
        return self._artop_someipTpConfig

    @property
    def someipTpConfig_(self):
        if self._artop_someipTpConfig is not None:
            if hasattr(self._artop_someipTpConfig, "uuid"):
                return self._artop_someipTpConfig.uuid
        return
