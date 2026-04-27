# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\AdaptiveApplicationSwComponentType.py
from .SwComponentType import SwComponentType

class AdaptiveApplicationSwComponentType(SwComponentType):

    def __init__(self):
        super().__init__()
        from .AdaptiveSwcInternalBehavior import AdaptiveSwcInternalBehavior
        self._artop_internalBehavior = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_internalBehavior": "ADAPTIVE-SWC-INTERNAL-BEHAVIOR"})

    @property
    def internalBehaviors_AdaptiveSwcInternalBehavior(self):
        return self._artop_internalBehavior
