# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TDEventBsw.py
from .TimingDescriptionEvent import TimingDescriptionEvent

class TDEventBsw(TimingDescriptionEvent):

    def __init__(self):
        super().__init__()
        from .BswModuleDescription import BswModuleDescription
        self._artop_bswModuleDescriptionRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_bswModuleDescriptionRef": "BSW-MODULE-DESCRIPTION"})

    @property
    def ref_bswModuleDescription_(self):
        return self._artop_bswModuleDescriptionRef

    @property
    def bswModuleDescription_(self):
        if self._artop_bswModuleDescriptionRef is not None:
            if hasattr(self._artop_bswModuleDescriptionRef, "uuid"):
                return self._artop_bswModuleDescriptionRef.uuid
        return
