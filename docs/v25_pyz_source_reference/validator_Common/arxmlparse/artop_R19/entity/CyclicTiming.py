# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\CyclicTiming.py
from .Describable import Describable

class CyclicTiming(Describable):

    def __init__(self):
        super().__init__()
        from .TransmissionModeTiming import TransmissionModeTiming
        from .TimeRangeType import TimeRangeType
        self._artop_transmissionModeTiming = None
        self._artop_timeOffset = None
        self._artop_timePeriod = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_transmissionModeTiming':"TRANSMISSION-MODE-TIMING", 
         '_artop_timeOffset':"TIME-RANGE-TYPE", 
         '_artop_timePeriod':"TIME-RANGE-TYPE"})

    @property
    def ref_transmissionModeTiming_(self):
        return self._artop_transmissionModeTiming

    @property
    def transmissionModeTiming_(self):
        if self._artop_transmissionModeTiming is not None:
            if hasattr(self._artop_transmissionModeTiming, "uuid"):
                return self._artop_transmissionModeTiming.uuid
        return

    @property
    def ref_timeOffset_(self):
        return self._artop_timeOffset

    @property
    def timeOffset_(self):
        if self._artop_timeOffset is not None:
            if hasattr(self._artop_timeOffset, "uuid"):
                return self._artop_timeOffset.uuid
        return

    @property
    def ref_timePeriod_(self):
        return self._artop_timePeriod

    @property
    def timePeriod_(self):
        if self._artop_timePeriod is not None:
            if hasattr(self._artop_timePeriod, "uuid"):
                return self._artop_timePeriod.uuid
        return
