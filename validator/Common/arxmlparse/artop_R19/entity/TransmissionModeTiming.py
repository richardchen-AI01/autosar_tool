# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TransmissionModeTiming.py
from .ARObject import ARObject

class TransmissionModeTiming(ARObject):

    def __init__(self):
        super().__init__()
        from .CyclicTiming import CyclicTiming
        from .EventControlledTiming import EventControlledTiming
        self._artop_cyclicTiming = None
        self._artop_eventControlledTiming = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_cyclicTiming':"CYCLIC-TIMING", 
         '_artop_eventControlledTiming':"EVENT-CONTROLLED-TIMING"})

    @property
    def ref_cyclicTiming_(self):
        return self._artop_cyclicTiming

    @property
    def cyclicTiming_(self):
        if self._artop_cyclicTiming is not None:
            if hasattr(self._artop_cyclicTiming, "uuid"):
                return self._artop_cyclicTiming.uuid
        return

    @property
    def ref_eventControlledTiming_(self):
        return self._artop_eventControlledTiming

    @property
    def eventControlledTiming_(self):
        if self._artop_eventControlledTiming is not None:
            if hasattr(self._artop_eventControlledTiming, "uuid"):
                return self._artop_eventControlledTiming.uuid
        return
