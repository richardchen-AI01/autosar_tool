# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SwcModeSwitchEvent.py
from .RTEEvent import RTEEvent

class SwcModeSwitchEvent(RTEEvent):

    def __init__(self):
        super().__init__()
        from .RModeInAtomicSwcInstanceRef import RModeInAtomicSwcInstanceRef
        self._artop_activation = None
        self._artop_modeIref = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_modeIref": "R-MODE-IN-ATOMIC-SWC-INSTANCE-REF-IREF"})

    @property
    def activation_(self):
        return self._artop_activation

    @property
    def modes_RModeInAtomicSwcInstanceRef(self):
        return self._artop_modeIref
