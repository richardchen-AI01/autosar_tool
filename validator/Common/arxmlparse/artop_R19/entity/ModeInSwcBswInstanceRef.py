# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ModeInSwcBswInstanceRef.py
from .ARObject import ARObject

class ModeInSwcBswInstanceRef(ARObject):

    def __init__(self):
        super().__init__()
        from .TimingModeInstance import TimingModeInstance
        self._artop_timingModeInstance = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_timingModeInstance": "TIMING-MODE-INSTANCE"})

    @property
    def ref_timingModeInstance_(self):
        return self._artop_timingModeInstance

    @property
    def timingModeInstance_(self):
        if self._artop_timingModeInstance is not None:
            if hasattr(self._artop_timingModeInstance, "uuid"):
                return self._artop_timingModeInstance.uuid
        return
