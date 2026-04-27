# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipSdClientServiceInstanceConfig.py
from .ARElement import ARElement

class SomeipSdClientServiceInstanceConfig(ARElement):

    def __init__(self):
        super().__init__()
        from .InitialSdDelayConfig import InitialSdDelayConfig
        self._artop_serviceFindTimeToLive = None
        self._artop_initialFindBehavior = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_initialFindBehavior": "INITIAL-SD-DELAY-CONFIG"})

    @property
    def serviceFindTimeToLive_(self):
        return self._artop_serviceFindTimeToLive

    @property
    def ref_initialFindBehavior_(self):
        return self._artop_initialFindBehavior

    @property
    def initialFindBehavior_(self):
        if self._artop_initialFindBehavior is not None:
            if hasattr(self._artop_initialFindBehavior, "uuid"):
                return self._artop_initialFindBehavior.uuid
        return
