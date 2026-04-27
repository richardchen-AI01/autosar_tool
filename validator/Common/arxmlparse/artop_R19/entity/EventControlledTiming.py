# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EventControlledTiming.py
from .Describable import Describable

class EventControlledTiming(Describable):

    def __init__(self):
        super().__init__()
        from .TransmissionModeTiming import TransmissionModeTiming
        from .TimeRangeType import TimeRangeType
        self._artop_numberOfRepetitions = None
        self._artop_transmissionModeTiming = None
        self._artop_repetitionPeriod = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_transmissionModeTiming':"TRANSMISSION-MODE-TIMING", 
         '_artop_repetitionPeriod':"TIME-RANGE-TYPE"})

    @property
    def numberOfRepetitions_(self):
        if self._artop_numberOfRepetitions:
            return int(self._artop_numberOfRepetitions)
        return self._artop_numberOfRepetitions

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
    def ref_repetitionPeriod_(self):
        return self._artop_repetitionPeriod

    @property
    def repetitionPeriod_(self):
        if self._artop_repetitionPeriod is not None:
            if hasattr(self._artop_repetitionPeriod, "uuid"):
                return self._artop_repetitionPeriod.uuid
        return
