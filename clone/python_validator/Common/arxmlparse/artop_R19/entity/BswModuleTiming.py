# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModuleTiming.py
from .TimingExtension import TimingExtension

class BswModuleTiming(TimingExtension):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        self._artop_behaviorRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_behaviorRef": "BSW-INTERNAL-BEHAVIOR"})

    @property
    def ref_behavior_(self):
        return self._artop_behaviorRef

    @property
    def behavior_(self):
        if self._artop_behaviorRef is not None:
            if hasattr(self._artop_behaviorRef, "uuid"):
                return self._artop_behaviorRef.uuid
        return
