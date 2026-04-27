# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventBswInternalBehavior.py
from .TimingDescriptionEvent import TimingDescriptionEvent

class TDEventBswInternalBehavior(TimingDescriptionEvent):

    def __init__(self):
        super().__init__()
        from .BswModuleEntity import BswModuleEntity
        self._artop_tdEventBswInternalBehaviorType = None
        self._artop_bswModuleEntityRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_bswModuleEntityRef": "BSW-MODULE-ENTITY"})

    @property
    def tdEventBswInternalBehaviorType_(self):
        return self._artop_tdEventBswInternalBehaviorType

    @property
    def ref_bswModuleEntity_(self):
        return self._artop_bswModuleEntityRef

    @property
    def bswModuleEntity_(self):
        if self._artop_bswModuleEntityRef is not None:
            if hasattr(self._artop_bswModuleEntityRef, "uuid"):
                return self._artop_bswModuleEntityRef.uuid
        return
